---
title: "My ubuntu desktop struggles to resume from hibernate?"
date: 2026-08-02
tags: ["technical"]
tagline: "Two weeks, two suspend bugs, three Claude models, and one desktop I killed by accident."
draft: True
---

My desktop would go to sleep beautifully and wake up badly. Fixing that took
two distinct bugs, two competing layers of sleep policy, an NVIDIA card that
made every failure look like a different failure, and three different Claude
models — one of which bricked my GUI for ten hours without either of us
noticing.

<!--more-->

## The problem, in two parts

Part one: hibernate had never worked on this machine. Not "worked badly" —
never worked, for years. Trigger it and the box would write its image, power
down properly, and then cold-boot on the next press. Every session, gone.

Part two only appeared *after* part one was fixed, which is how these things
go. With hibernate finally working I set up a proper idle chain — screen blank
at 15 minutes, suspend at 30, hibernate at 2 hours — and immediately hit a
new symptom. The machine would wake, stay up for 60 seconds, maybe 120, and
then suspend itself again. It'd settle only after the second or third wake. One
morning I had to yank the HDMI cable to convince it to come back at all.

## Two layers, both of which think they run the show

Here's the thing I didn't properly understand going in, and which is the actual
subject of this post: on a modern Linux desktop there are *two* independent
systems that can decide to put your machine to sleep, and they don't
co-ordinate.

**Layer one is GNOME.** `gnome-settings-daemon`'s power plugin (`gsd-power`)
watches an idle clock owned by mutter, the compositor. You configure it with
gsettings: `idle-delay` for the blank, `sleep-inactive-ac-timeout` and
`sleep-inactive-ac-type` for the suspend. When it fires, it calls logind's
`Suspend()` over D-Bus. This is the layer the Settings app shows you.

**Layer two is systemd-logind**, and it has its own, entirely separate idle
timer: `IdleAction=` and `IdleActionSec=` in `logind.conf`. It doesn't watch
the compositor. It watches a per-session flag called `IdleHint`, which the
desktop is expected to set and clear on logind's behalf. When it fires it calls
`manager_handle_action()` directly and GNOME never hears about it.

Below both of those sits `systemd-sleep`, which does the actual work, and which
is where the suspend-versus-hibernate decision lives (`HibernateDelaySec`, the
`suspend-then-hibernate` verb). GNOME 46 has no way to ask for
suspend-then-hibernate at all — there's simply no such value in its enum — so
getting a suspend that escalates to hibernate after 90 minutes meant overriding
`systemd-suspend.service` to run a different verb than its name suggests. That
override applies to *every* suspend on the box now: the menu button,
`systemctl suspend`, and the idle timer alike.

So: three layers, two of them armed with independent timers, one of them
lying about its own name. Sleep on Linux is not a setting. It's a negotiation.

## Bug one: a missing number in GRUB

The hibernate failure turned out to be one absent kernel parameter.
`/etc/default/grub` had `resume=UUID=<the root filesystem>` but no
`resume_offset=`. For a swapfile — as opposed to a swap partition — you need
both.

That asymmetry is exactly why the symptom was so confusing. *Entry* into
hibernation doesn't need the offset: the kernel falls back to
`find_first_swap()`, writes the image, and powers off looking completely
healthy. *Resume* happens much earlier, in the initramfs, where
`/usr/share/initramfs-tools/scripts/local-premount/resume` probes the raw
partition with `blkid`, sees `ext4` where it wanted `swsuspend`, quietly hits
its `*) exit 0` branch, and never writes to `/sys/power/resume`. No error. No
log line. Just a cold boot.

The missing number is the physical block offset of `/swap.img` inside the
filesystem — `204028082`, from `filefrag -v`. It is not self-healing. If that
swapfile is ever recreated, resized or restored from a backup, hibernate
silently goes back to cold-booting and nothing anywhere will tell me why.

## Bug two: nobody resets the clock

The re-suspend loop was harder, and it's a genuinely elegant bug.

Both idle mechanisms measure time with `CLOCK_MONOTONIC`, which by design does
*not* advance while the system is suspended. So when the machine comes back
from S3, the idle clock reads exactly what it read when it went down —
already past the threshold. The keypress that woke the box gets consumed by the
USB/ACPI wake path and never reaches the compositor, so nothing resets it.
Neither layer re-arms its watches before the resume is announced. The still-armed
sleep watch is evaluated against a stale idle time, and the machine
immediately decides it's been idle for half an hour and goes back to sleep.

The measurement that proved it: resume at `idle=1804792 ms` against an
`1800000 ms` watch, with mutter firing at gsd-power *in the same millisecond*.

The obvious fix — take suspend policy away from GNOME and give it to logind —
did not work. It relocated the bug. logind's equivalent state is the session's
`IdleHint`, which is just as stale across a suspend as mutter's clock was, and
for the same reason. Overnight, under logind ownership, the gaps between resume
and re-suspend were 93, 111, 115 and 226 seconds. Same bug, one layer down.

The real behaviour, which took a dedicated experiment to pin down, is subtler
still: on resume GNOME *re-asserts* `IdleHint=yes` with a fresh timestamp, and
then clears it about two seconds later — **but only if the wake event actually
reaches the compositor**. Keyboard wake into a healthy session: fine. Power
button, HDMI replug, or a session that's gotten confused: the hint stands, and
logind dutifully suspends you again.

Which means the fix can't be a tuned timeout on either layer. It has to be a
resume guard: a small user service that hooks `PrepareForSleep(false)` and
unconditionally clears the session's `IdleHint` ten seconds after every single
wake, whatever the wake path was. Belt and braces, applied at the one moment
both layers agree something has changed.

## Where the NVIDIA card comes into it

The graphics card didn't cause either bug. Kernel resumes were clean throughout.
But it shaped the whole thing anyway, in three ways.

It's **load-bearing for hibernate working at all.** Hibernating a machine with
several gigabytes of VRAM means getting that VRAM to disk:
`NVreg_PreserveVideoMemoryAllocations=1`, `NVreg_TemporaryFilePath=/var`, and a
hook at `/usr/lib/systemd/system-sleep/nvidia` that pushes it out. That hook
keys off `$2` — the *verb* passed to `systemd-sleep`, not the unit name — which
is the only reason my `suspend-then-hibernate` override didn't quietly skip the
VRAM save. On the way back, `nvidia-resume.service` is `WantedBy=`
`systemd-suspend.service`, and it's what performs the VT switch-back. Without
it you resume to a black screen. None of that is obvious, and all of it is one
typo away from a machine that hibernates and never comes back.

It **defines the bug class upstream.** Searching for prior art turns up open
issues that read like a description of my machine: systemd #40078 (double
suspend loop, bisected to the v258 release), systemd #39259 (auto-suspends
seconds after resume — "systemd 258 + GNOME 49 + NVIDIA"), and a GNOME
Discourse thread on 49.x doing the same. This class of bug lives specifically
on GNOME plus a discrete NVIDIA card, and it is currently *regressing*, not
improving. Which killed my fallback plan of waiting for Ubuntu 26.04: it ships
GNOME 50 and systemd 259, the direct successors of both broken versions, with
no merged fix in either tracker.

And it **made every failure ambiguous.** When I finally got the catastrophic
one — machine wakes, no desktop, bare tty — the log line was gnome-shell
failing to reopen `/dev/dri/card2`. That looks *exactly* like an NVIDIA resume
failure. It wasn't. Which brings me to the interesting part.

## Three models, one problem

Most of this was done with Claude Code — I asked Codex the power-menu question
along the way too — and the models did noticeably different things.

**Sonnet** did the groundwork, though none of it looked like debugging at the
time. A week earlier it had audited my swap: established that `/swap.img` was
the live one, that a 48GB `/swapfile` was an orphan from a previous install
referenced by nothing, and that it was safe to delete. Mundane housekeeping,
except that the hibernate fix turns entirely on the identity and physical
location of the live swapfile — so it's just as well the question had already
been settled correctly. It also ran as the summariser when sessions were
compacted.

**Opus** owned the hard yards, and won the first half outright. The
`resume_offset` diagnosis was properly good work: it eliminated firmware, ACPI
S4, Secure Boot and the NVIDIA driver by direct evidence rather than by
guessing, then read the actual initramfs shell script to find the branch where
resume silently gave up. Years-old bug, fixed in an afternoon, verified by
checking `boot_id` was unchanged across a real cycle.

On the second bug it did the hardest and least glamorous work and still didn't
land it. It proved `gsd-power` was the sole caller of `Suspend()` by capturing
a root `dbus-monitor` trace and resolving the sender back to a PID. It caught
the millisecond-level timing that showed the idle clock was stale. It ruled out
— by evidence, not by hand-waving — a GDM greeter session, a stray `KEY_SLEEP`
from my keyboard, a lid switch on a machine with no lid, the RTC alarm
machinery, and the graphics driver.

Then it proposed moving policy to logind. It reasoned, confidently, that
logind's internal throttle made a rapid re-suspend loop *structurally
impossible*. It was wrong, and said so plainly the next morning when the
overnight run produced a 93-second loop.

And in the course of applying that fix it ran `systemctl restart
systemd-logind` on a live Wayland session. That command silently revokes
gnome-shell's `TakeControl` registration over the DRM and input devices. The
session keeps running perfectly — zero errors before the restart, 160
`NotInControl` errors after, the first 300 milliseconds later, all invisible
because nothing needed to reopen a device yet. Ten hours later the machine woke
from its overnight hibernate into a bare console and my desktop was
unrecoverable. That black screen looked like the NVIDIA failure I'd been
chasing all along. It was self-inflicted, by my assistant, the previous night.

The next morning, somewhat tersely, I asked for a review of the whole mess —
"it should not be this hard to reliably resume from hibernate/suspend on a
desktop machine!?" — and switched to **Fable**. Four seconds later it picked up
the thread.

It found the smoking gun for the dead GUI in a single journal line. It designed
the experiment that discriminated between the competing models — an idle-hint
logger running at compressed timings — and that experiment *revised* Opus's
theory rather than confirming it, producing the "GNOME re-asserts the hint but
only self-clears when the wake reaches the compositor" behaviour that nobody
had predicted. It shot down the wait-for-26.04 escape hatch with the upstream
issue numbers. And then, crucially, it chose a design that survives its own
model being wrong: rather than tuning either idle layer, an unconditional
resume guard that clears the state every time regardless of which theory is
correct. It applied the logind config by `reload`, not `restart`, having
understood precisely why the restart was fatal.

## So who fixed it?

Honestly? Fable closed it, but it was handed an enormously reduced problem.

Its very first instruction from me was "review the problem and attempts to fix
from this session" — it inherited a compacted summary of everything Opus had
established. By the time it started, the sole `Suspend()` caller was known, the
monotonic-clock mechanism was known, and half a dozen plausible causes had been
eliminated by measurement. Opus's *failed* fix was arguably the single most
valuable artifact in the whole investigation: moving the bug to logind without
killing it is what proved the defect lived one layer above both of them, and
wasn't a GNOME problem at all. You don't get that from reasoning. You get it
from shipping the wrong fix and watching what happens.

What Fable brought that Opus didn't was a willingness to run one more
discriminating experiment before believing its inherited model, and the
engineering judgement to build something that doesn't depend on the model being
right. Those are different skills from investigation, and it's fair to say the
second model was better at them. It's also fair to say it was standing on a
mountain of the first one's measurements.

## Do I trust it with my operating system?

Two of three verification gates have passed. The third — a natural overnight
blank, suspend, hibernate, and morning wake with the desktop intact — runs
tonight, as I write this. So the honest answer to "is it fixed" is "probably,
and I'll know by breakfast."

Which is roughly where I land on the bigger question too. In one week an LLM
read initramfs shell scripts to find a silent `exit 0`, captured and decoded a
D-Bus trace to identify a process by PID, measured a race to the millisecond,
correctly diagnosed an interaction between a compositor's monotonic clock and
the S3 sleep state, and read enough upstream bug tracker history to talk me out
of a distro upgrade that wouldn't have helped. That is not autocomplete. That's
a competent systems engineer's week.

In the same week, it also destroyed my graphical session with a command that
looked completely harmless, and neither of us found out for ten hours.

Both of those are the same capability. The thing that can reason its way into
the initramfs is the thing that can reason its way into `systemctl restart
systemd-logind`, and the failure mode of a confident systems engineer is
confident systems damage. Notably, every single thing that went right in this
saga went through me: I was the one physically waking the machine and counting
to ten, reporting what happened, typing my password into polkit dialogs because
`sudo` can't prompt through an agent, and — critically — deciding to reboot
rather than keep experimenting on a broken session.

So: entrusting the OS to an LLM? We're already most of the way there in
practice. I have not personally read most of the config now running my
machine's sleep behaviour, and it works better than the config I *did* write.
What's missing isn't intelligence, it's the boring stuff — a sense of which
commands are load-bearing, and some way to notice that you've broken something
ten hours before the symptom shows up. Neither of those is a hard research
problem. Both of them are why I'm still in the loop.

Ask me again after tonight.
