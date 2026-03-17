title: nvLock client timed out taking the lock
published: 2019-05-11
tag: technical
disqus: http://johnmee.com/nvlock-nvidia-linux-8700


# Nvidia driver setup for Ubuntu

> How to set up linux to use both an nvidia graphics card _and_ the GPU on the motherboard.  
  It all started with a little graphics glitch which I had a moment to, hopefully, fix.  
  It ended up maximizing two GPUs.  
  In between was a whole lot of pain.

The whole desktop freezes for a moment, usually when flipping between window tiles, and especially when trying to
drag folders around Nautilus.  The syslog reveals:

    /usr/lib/gdm3/gdm-x-session[1867]: nvLock: client timed out, taking the lock

It's only a minor irritation; not a show stopper.  I could live with it.  And I can do a quick search.  Perhaps
there's an easy fix.  

These are some notes about how to configure Ubuntu Linux and the Intel i7 8700, which has a GPU built into it,
to work in tandom with an Nvidia PCIe graphics card/chip.  I'm on a desktop, but you might also have a laptop.

# TL;DR?

Set a global env variable by adding `__GL_MaxFramesAllowed=1` to the file `/etc/environment` and restart.

 **Don't search google/duckduck/whatever.  Go directly to the NVidia documentation.**  
  eg: http://us.download.nvidia.com/XFree86/Linux-x86_64/418.74/README/

# What is Nvidia Prime?  Optimus?

To start at the end, I've discovered that Optimus is some glossy marketing crap for laptops that will actually work
for me on my desktop.  It is supposed to save power for people who have laptops with nvidia chips ("discrete graphics") 
in them, as well as some sort of onboard ("integrated graphics") GPU, like inside the Intel i7 8700 CPU.  It does
this by using the integrated graphics primarily, then "offloading" the processing when things start to get
busy.

It means I can leverage the fancy Nvidia GTX-1070Ti graphics card when I play games, but have it automatically turn
itself off when it isn't necessary.  I like it!

But it was a bit tricky to set up.  Mostly because I didn't understand all the of the above.


# Install the nvidia driver.

Actually it all started with an upgrade cycle.  Somehow, under 18.04, I had stumbled into the above config already.  
Then Ubuntu released 19.04 and, against my better judgement, I thought "sure why not" when it prompted to update.  
That broke things.

At the end of the day, I have installed the Nvidia driver via "Software & Updates" app.  See under the 
"Additional Drivers" tab.  I suspect this is the same as saying **`sudo ubuntu-drivers install`**.

```{.bash}
john@bigbox:~/projects/johnmee/src$ ubuntu-drivers list
nvidia-driver-418
nvidia-driver-390
john@bigbox:~/projects/johnmee/src$ ubuntu-drivers devices
== /sys/devices/pci0000:00/0000:00:01.0/0000:01:00.0 ==
modalias : pci:v000010DEd00001B82sv00001043sd00008623bc03sc00i00
vendor   : NVIDIA Corporation
model    : GP104 [GeForce GTX 1070 Ti]
driver   : nvidia-driver-390 - distro non-free
driver   : nvidia-driver-418 - distro non-free recommended
driver   : xserver-xorg-video-nouveau - distro free builtin
``` 

Note the contents of **`/var/log/gpu-manager.log`**.

# But I can't login to X? Only Wayland.

*X* or X11, xorg, x-server, has been around forever.  I do mean, _forever_. Like, since I was a lad, and linux didn't
exist yet, and the personal computer wasn't a thing yet.  It was build to solve different problems in a different
world and it is astonishing that it is still around running modern graphics desktops.  
Wayland, as I understand it, was an attempt to bring linux into the new world by rebuilding that 
Graphical environment.  Apparently it has also failed to gain enough support to replace X.  

**Wayland doesn't work with the nvidia driver.**  Not at all.  If you're seeing something, it's using something else.
Like the intel driver and the UHD630 inside the CPU. If you try to play a game it will run like a dog; because it
is not offloading any work to the video card.

When you try to log into Ubuntu (gnome/gdm3) and it:

* goes into a "login loop", or just throws you back to the login, or
* displays a blank screen with a cursor, or
* just goes completely blank

this, almost certainly, means X is failing to start.  Unfortunately there can be a few reasons for this.  Fortunately
you might not have to work out which specific reason applies.

# Check your BIOS

My bios detects the PCIe graphics installation and provides a graphics option with "auto", "integrated", "PCIe".
Meaning I can tell it to ignore any monitor plugged into HDMI port on the graphics card, motherboard, or just
probe them both and choose for itself.

** Choose the integrated CPU option and  
plug the HDMI cable into the motherboard **

We want the GPU on the motherboard to be dominant, and passoff tasks to the GPU on the nvidia card.

# Blacklist the Nouveau driver!

This is when I finally made some progress; I had seen it around, but didn't pay enough attention to it.

**Nouveau** is an alternative Nvidia driver!  You don't want it.  It is a reverse-engineered community driver born because 
Nvidia refuse to open their source code.  It is the default for that reason; it's open source and can be freely
distributed.  But it's not the latest and greatest and doesn't implement any of the fancy features you saw on the
marketing brochures.

The best approach is to disable it the way Nvidia prescribe. See the very bottom of "Common Problems" of the README
for the NVidia driver.

Create a specific file to disable it in `/etc/modprobe.d/`.

```{.bash}
% sudo bash
% vi /etc/modprobe.d/disable-nouveau.conf
blacklist nouveau
options nouveau modeset=0
```

# Manually edit the xorg.conf

Yep. Sad but true.  I went around and around and around.  Nothing was being consistent (ie working).  
Not even nvidia's own `nvidia-xconfig` utility.  I had to edit.  I used the nvidia README to guide me.
"Chapter 33. Offloading Graphics Display with RandR 1.4".

I thought xrandr was unrelated, old, and unnecessary.  I was wrong.

1. Add the BusID to the 'nvidia' Device
1. Add "Option AllowEmptyInitialConfiguration" to the "Screen" section
1. Add "Driver modesetting" to the 'intel' Device.

# Create a '$HOME/.xinitrc'

You need this to enable the Intel graphics device in X.  This is why you're getting a blank screen, or cursor, if
you login and X is actually starting, but the signal is coming from the nvidia and hdmi cable is attached to 
the Intel device.  Or some oddity like that.

```{.bash}
$ vi ~/.xinitrc
xrandr --setprovideroutputsource modesetting NVIDIA-0
xrandr --auto
```
 
# Some commands that helped

Inxi is not installed by default, but was worth it.  It's just a harmless script which gathers useful information.

```{.bash}
john@bigbox:~$ inxi -Gx
Graphics:  Device-1: Intel UHD Graphics 630 vendor: ASUSTeK driver: i915 v: kernel bus ID: 00:02.0 
           Device-2: NVIDIA GP104 [GeForce GTX 1070 Ti] vendor: ASUSTeK driver: nvidia v: 418.56 bus ID: 01:00.0 
           Display: x11 server: X.Org 1.20.4 driver: nvidia resolution: 3840x2160~30Hz 
           OpenGL: renderer: GeForce GTX 1070 Ti/PCIe/SSE2 v: 4.6.0 NVIDIA 418.56 direct render: Yes 
```

Here I can see I have two GPUs configured (Intel UHD630 and NVidia GTX 1070), and which driver each is using, and 
what version.  Also that X is running, version etc. and THE KICKER which renderer OpenGL is using.  We want it to
use the Nvidia.

Sometimes I couldn't tell if I was logged into X, or Wayland...

```{.bash}
john@bigbox:~$ loginctl
SESSION  UID USER SEAT  TTY 
      2 1000 john seat0 tty2

1 sessions listed.
john@bigbox:~$ loginctl show-session 2 -p Type
Type=x11
```

Then there are all the nvidia utils.  If you run nvidia-settings and get a blank, then the nvidia driver is not
installed correctly; you're probably running off the intel and don't realize it.

```{.bash}
john@bigbox:~$ nvidia-
nvidia-bug-report.sh     nvidia-cuda-mps-server   nvidia-detector          nvidia-settings          nvidia-xconfig           
nvidia-cuda-mps-control  nvidia-debugdump         nvidia-persistenced      nvidia-smi               
john@bigbox:~$ nvidia-smi
Sat May 11 18:04:22 2019       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 418.56       Driver Version: 418.56       CUDA Version: 10.1     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  GeForce GTX 107...  Off  | 00000000:01:00.0 Off |                  N/A |
| 24%   53C    P8     9W / 180W |    888MiB /  8119MiB |     14%      Default |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                       GPU Memory |
|  GPU       PID   Type   Process name                             Usage      |
|=============================================================================|
|    0      1869      G   /usr/lib/xorg/Xorg                           366MiB |
|    0      2069      G   /usr/bin/gnome-shell                         251MiB |

```

This one was interesting at the start of this problem, but I didn't really understand what Prime was all about.
I thought it was part of Optimus and determined which GPU is dominant, but now I have it all working that's wrong.
It's currently set to nvidia.  Go figure.

```{.bash}
john@bigbox:~$ prime-
prime-offload    prime-select     prime-supported  prime-switch     
john@bigbox:~$ prime-select query
nvidia
```

LightDM

Somewhere along the way I figured out that there is a difference between login, or "Display" managers. They throw up
the initial login screen, but then X is runs entirely separately! It's just a login shell.  The default ubuntu/gnome one is gdm3.  
For troubleshooting X, it turned out worthwhile
to install LightDM (aka Unity, basically Gnome 2) just for the different perspective: that X was failing to start
after login.

