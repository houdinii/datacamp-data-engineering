import numpy as np
import pandas as pd
import time


# Utility function to hash dictionary in memoize
def freeze(d):
    if isinstance(d, dict):
        return frozenset((key, freeze(value)) for key, value in d.items())
    elif isinstance(d, list):
        return tuple(freeze(value) for value in d)
    return d


"""
More On Decorators - Now that you understand how decorators work under the hood, this chapter gives you a bunch of real-world examples 
of when and how you would write decorators in your own code. You will also learn advanced decorator concepts like how to preserve the 
metadata of your decorated functions and how to write decorators that take arguments.

Real-world Examples:

- The timer() decorator runs the decorated function and then prints how long it took for the function to run.
    - All decorators have fairly-similar doctrings because they return a single function.
    - wrapper() takes any number of positional and kw args so that it can be used to decorate any function.
    - The first thing the new func will do is record the time that it was called with the time() function.
    - Then wrapper() gets the result of calling the decorated function.
    - After calling decorated function, wrapper() checks the time again and prints time elapsed.
    - Once we've done that, we need to return the value that the decorated function calculated
"""


def timer(func):
    """A decorator that prints how long a function took to run

    Args:
        func (callable): The function being decorated.

    Returns:
        callable: The decorated function
    """

    # Define the wrapper function to return
    def wrapper(*args, **kwargs):
        # When wrapper() is called, get the current time.
        t_start = time.time()
        # Call the decorated function and store results.
        result = func(*args, **kwargs)
        # Get the total time it took to run, and print it.
        t_total = time.time() - t_start
        print(f"{func.__name__} took {t_total}sec.")
        return result
    return wrapper


def using_timer():
    @timer
    def sleep_n_sec(n=20):
        time.sleep(n)

    sleep_n_sec(5)


"""
Memoizing - The process of storing the results of a function so that the next time the function is 
called with the same arguments, you can just look up the answer. (I.e. cacheing)

- Start by setting up a dictionary that will map arguments to results
- Then we create wrapper() to be the new decorated function that this decorator returns.
- When the new function gets called, we check to see if we've seen these args before.
    - If we haven't, send them to the decorated function and store result in the cache dictionary.
        - Now we can look up the return value quickly in a dictionary of results.
    - If we have, simply return cache[(args, kwargs)] since it's already in the dictionary, negating the need to rerun func().
"""


def memoize(func):
    """Store the results of the decorated function for fast lookup
    """

    # Store results in a dict that maps arguments to results
    cache = {}

    def wrapper(*args, **kwargs):
        # If these arguments haven't been seen before,
        if (freeze(args), freeze(kwargs)) not in cache:
            # Call func() and store the result
            cache[(freeze(args), freeze(kwargs))] = func(*args, **kwargs)
        return cache[(freeze(args), freeze(kwargs))]
    return wrapper


def using_memoize():
    @timer
    @memoize
    def slow_function(a, b):
        print('Sleeping...')
        time.sleep(5)
        return a + b

    print(slow_function(1, 1))
    print(slow_function(1, 1))
    print(slow_function(1, 1))
    print(slow_function(1, 1))
    print(slow_function(1, 1))


"""
When to use decorators: When adding common cbehavior to multiple functions
"""


"""
Decorators and metadata:

When we use decorators, they obscure a function's metadata (like __doc__ and __name__). Thankfully, the module wraps() in functools
provides us with a way to pass this metadata along. It also gives us easy access to the original undecorated function via the 
__wrapped__ attribute. 
"""

from functools import wraps


def timer_2(func):
    """A decorator that prints how long a function took to run"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        t_start = time.time()
        result = func(*args, **kwargs)
        t_total = time.time() - t_start
        print(f"{func.__name__} took {t_total}")
        return result
    return wrapper


@timer_2
def sleep_n_sec(n=20):
    """Pause processing for n seconds

    Args:
        n (int): The number of seconds to pause for.
    """
    time.sleep(n)


def decorators_and_metadata():
    print(sleep_n_sec.__doc__)
    print(sleep_n_sec)              # The decorated function
    print(sleep_n_sec.__wrapped__)  # The original undecorated function
    sleep_n_sec.__wrapped__(2)


"""
Decorators that take arguments:

Consider the silly function, run_three_times below, which takes a function and runs it three times. If we decorate print_sum with
a=1, b=2, it will print 3 three times. 

A second consideration is run_n_times. How do we pass a value to range(n)

"""


def run_n_times_bad_example(func):
    def wrapper(*args, **kwargs):
        # How do we pass 'n' into this function?
        for i in range(1):
            func(*args, **kwargs)
    return wrapper


def run_three_times(func):
    def wrapper(*args, **kwargs):
        for i in range(3):
            func(*args, **kwargs)
    return wrapper


"""
The solution is to use a decorator factory
"""


def run_n_times(n):
    """Define and return a decorator"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator


def a_decorator_factory():
    @run_n_times(3)
    def print_sum(a, b):
        print(a + b)
    print_sum(3, 5)


"""
Timeout(): A Real World Customer

Suppose we have some functions that run for a long time or hangs and doesn't return.

def function_1():
    # This is a function that sometimes runs for a LONNNNG time.

def function_2():
    # This is a function that hangs and doesn't return.
    
It would be nice if we could add some kind of timeout() decorator to throw an error if runs for longer than expected

Timeout - background info. We are going to be using some modules from the signal built-in
"""

import signal


def raise_timeout(*args, **kwargs):
    raise TimeoutError()


def timeout_background_info():
    # Doesn't work in windows
    # When an 'alarm' signal goes off, call raise_timeout()
    signal.signal(__signalnum=signal.SIGALRM, __handler=raise_timeout())
    # Set off an alarm in 5 seconds
    signal.alarm(5)


def timeout_in_5s(func):
    # WILL NOT WORK IN WINDOWS
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Set an alarm for 5 seconds
        signal.alarm(5)
        try:
            # Call the decorated func
            return func(*args, **kwargs)
        finally:
            # Cancel Alarm
            signal.alarm(0)
    return wrapper


def timeout(n_seconds):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Set an alarm for n seconds
            signal.alarm(n_seconds)
            try:
                # Call decorated func
                return func(*args, **kwargs)
            finally:
                # Cancel Alarm
                signal.alarm(0)
        return wrapper


@timeout_in_5s
def foobar():
    time.sleep(10)
    print('foo')


def tag(*tags):
    """Decorator to tag functions"""
    # Define a new decorator, named "decorator", to return
    def decorator(func):
        # Ensure the decorated function keeps its metadata
        @wraps(func)
        def wrapper(*args, **kwargs):
          # Call the function being decorated and return the result
          return func(*args, **kwargs)
        wrapper.tags = tags
        return wrapper
    # Return the new decorator
    return decorator


def tag_your_functions():
    @tag('test', 'this is a tag')
    def foo():
        pass

    print(foo.tags)


def returns(return_type):
  # Complete the returns() decorator
  def decorator(func):
    def wrapper(*args, **kwargs):
      result = func(*args, **kwargs)
      assert type(result) == return_type
      return result
    return wrapper
  return decorator


def check_returns_ii():
    @returns(dict)
    def foo(value):
        return value

    try:
        print(foo([1, 2, 3]))
    except AssertionError:
        print('foo() did not return a dict!')


def main():
    # using_timer()
    # using_memoize()
    # decorators_and_metadata()
    # a_decorator_factory()
    # timeout_background_info()
    # tag_your_functions()
    check_returns_ii()


if __name__ == '__main__':
    main()
