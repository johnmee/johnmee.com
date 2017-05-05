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

`factorial = lambda n: n * factorial(n) if n != 0 else 1`
