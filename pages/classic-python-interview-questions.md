title: Classic Python Interview Questions
published: 2017-04-28
tag: technical
disqus: http://johnmee.com/classic-python-interview-questions


# Classic Python Interview Questions

> If you want a job working with Python, get ready for these classic interview questions...

## The "GIL"

The [Global Interpreter Lock](https://wiki.python.org/moin/GlobalInterpreterLock) will always come up at some point.

CPython (the standard default official interpreter) is not thread-safe when it comes to memory management.  So, if
you're running multiple threads, the GIL is a bottleneck; it only allows one thread to access memory at a time.
If everything is happening in one thread, then you're fine.  But if multi-threading then, when one thread accesses memory,
the GIL blocks all the other threads.  This is a problem for multi-threaded python programs. It is not a problem for
multi-processing python since each process has it's own memory.

Key words to say are "bottleneck", "multi-threading" and "memory management".

Solutions are to use multi-processing, use extensions written in C, or use other Python implementations like IronPython,
or Cython.

In seven years of (web-centric) Python programming I've used multi-processing but never multi-threading.  Nonetheless I
always get asked this question in interviews.


## mutable vs immutable

An **immutable** type cannot be changed. Examples are integers, floats, strings, tuples.
A **mutable** type can change.  Examples are lists, dictionaries, sets, classes.

If you reel this off with ease they should dig deeper and try to expose your understanding of how immutable types point to
actual values, whereas immutable types are pointers to locations in memory so, obviously, are subject to change.

This is actually a reasonable question.  Mostly impractical but a little unique to python so anyone professing to be a
python guru needs to understand it.

## generators vs iterators

An **iterator** has the whole sequence in memory before it returns the first result.  An iterator uses the "return".
A **generator** calculates each result in the moment it is called for. The _next_ result is unknown.  A generator uses "yield".

* You'd use a generator when processing a stream, or when memory consumption is important.
* Generators are iterators, but iterators are not generators.

A *list comprehension* is an iteration. eg: `[x for x in range(1, 100)]`
A *generator expression* is a generator. eg: `(x for x in range(1, 100))`

**that's a perfect example because you can go on to explain the range function is an iterator in python 2 and a
generator in python 3.  By this point the interviewer will be already seeking another way to trip you up but, if they're
onto you, you will look stupid if you don't know anything about the `xrange` function.

## single and double underscores?

A single underscore is *private*.  eg: \_foo is not intended for access from outside the current scope.
A double underscore is a reserved language construct. eg: \_\_init\_\_ is a python constructor, and \_\_iter\_\_ is the python
iterator.

Note that the single underscore is only a convention; and not a rule enforced by the the language interpreter.
You can access these variables/methods if you want to. The single underscore only indicates that you weren't supposed to do that.


## Scopes

*Local* is restricted to the function or class.
*Enclosed*, like a javascript *closure*, exposes names to functions inside this function, but not functions outside it.
*Global* means you can use it anywhere in the module/script.

In practice, scope is a non-issue in python, so interviewers can find it very useful to frustrate and fluster candidates
into subordination and insecurity.

## lambdas

A lambda is a shortcut way to create a function. The key words to say are "*anonymous function*".

For extra credit, you might be asked to create a recursive function with a lambda. Surprisingly enough you can actually
refer to the name you're declaring. eg:

`factorial = lambda n: n * factorial(n-1) if n != 0 else 1`

## More interview questions

[These questions, and my answers, for an engineering
role associated with google](/html/google-evaluation.html) might be interesting, and my answers, since you've come this far.


## Non-Technical Interview Questions

Plus it wouldn't hurt to be ready for these general classics:

#### What prompted you to apply for this job?

> I’m excited by the possibilities presented by your company. I’d like to be a part of its future success, and I want
to help it to continue to grow by…

> This role offers exactly the types of challenges and responsibilities I’m looking for and is ideally suited to my
skills and experience…

* Focus on emphasising the match between your skills and experience and the operations and culture of the company you’re applying to.
* Be honest and upfront about your motivations, while explaining why you’re passionate about the role. These qualities will shine through in your answer and impress much more than simply trying to tell them what you think they want to hear.
* Demonstrate your understanding of the company, show that you’ve researched your potential employer thoroughly, and have good reasons for wanting to work there.


#### Why are you the best person for this job?

> This job is perfectly matched to my core competencies. I really feel like your company is the ideal fit for my
interests, qualifications and passions...

> My years of experience have given me the organisational / teamwork / sales / managerial skills to make me an
invaluable employee for this company…

* Referring to the specific requirements of the role, emphasise what you can offer to your potential employer,
rather than what they can do for you.
* Choose two of your most unique qualities that you think set you apart from other candidates and use them as
compelling reasons to employ you.


#### Why did you leave your previous role?

> I found myself a little ‘stuck’ and decided I needed new challenges that weren’t readily available in my previous role…

> I’m interested in a job with greater responsibility, and feel that a role like this would better offer those kinds
of opportunities...

> I was laid off due to a company restructure...

* Whatever your reasons for leaving your last job, resist the urge to bad-mouth your previous employer as it can
appear unprofessional and disloyal.
* Focus on the future, and ensure you sound positive and optimistic as you elaborate on your chosen career goals.

#### What would you describe as your key strengths?

> I’m organised, efficient and take great pride in doing the best work possible, and exceeding expectations…

> My previous employer often commented on my ability to motivate and manage my team members – and I was even
commended on my abilities with an industry award…

* There’s no point reeling off a list of strengths that aren’t relevant to the actual role in question. Think about
the types of skills your potential employer is looking for (i.e. from the job ad) and then select from your list of
strengths, to illustrate exactly how you’re the ideal candidate.
* Elaborate on your named strengths and demonstrate how they’re useful in action by using real examples from your
past experience. Make sure you highlight the actual benefits of each strength in ways that are relevant to the employer.

#### What would you describe as your main weaknesses?

> I know that public speaking is the number one phobia for most people, and I’d say that’s the main area I’d like to
work on, especially as I know it’s part of the job description for this role...

> I’m very detail oriented and meticulous, which means that I can sometimes take a little longer to get a task done,
but I’m working on getting the right balance between attending to the detail and being as efficient as possible…

* It can be tricky, but presenting some of your more minor weaknesses – obviously not ones that will greatly
impact your ability to do the job – is the best tactic for answering this question.
* Alternatively, mention areas that you were once slightly weaker at, but which you’ve been working on
improving (successfully).
* You could also mention tasks you know are a part of the role you’re applying for, which you’d like some
further training or support with – for example, a particular software program. If you can be honest and ask
for help where you feel you need it, this demonstrates that you’re keen to continually learn and improve yourself.
* With any weakness you mention, emphasise your awareness, willingness and efforts to improve.
* If possible, try to avoid overly clichéd answers such as “I’m too much of a perfectionist” or “I work too hard”.
