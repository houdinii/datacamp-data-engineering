import numpy as np
import pandas as pd


def print_the_return_type_example():
    def print_return_type(func):
        # Define wrapper(), the decorated function
        def wrapper(*args, **kwargs):
            # Call the function being decorated
            result = func(*args, **kwargs)
            print('{}() returned type {}'.format(func.__name__, type(result)))
            return result

        # Return the decorated function
        return wrapper

    @print_return_type
    def foo(value):
        return value

    print(foo(42))
    print(foo([1, 2, 3]))
    print(foo({'a': 42}))


def counter_example():
    def counter(func):
        def wrapper(*args, **kwargs):
            wrapper.count += 1
            # Call the function being decorated and return the result
            return func(*args, **kwargs)

        wrapper.count = 0
        # Return the new decorated function
        return wrapper

    # Decorate foo() with the counter() decorator
    @counter
    def foo():
        print('calling foo()')

    foo()
    foo()

    print('foo() was called {} times.'.format(foo.count))

    """
    Cool counting! Now you can go decorate a bunch of functions with the counter() decorator, let your program run for a while, and 
    then print out how many times each function was called.

    It seems a little magical that you can reference the wrapper() function from inside the definition of wrapper() as we do here on 
    line 3. That's just one of the many neat things about functions in Python -- any function, not just decorators.
    """


def preserving_docstrings_when_decorating_functions1():
    from functools import wraps

    def add_hello(func):
        # Decorate wrapper() so that it keeps func()'s metadata
        @wraps(func)
        def wrapper(*args, **kwargs):
            """Print 'hello' and then call the decorated function."""
            print('Hello')
            return func(*args, **kwargs)

        return wrapper

    # Decorate print_sum() with the add_hello() decorator
    @add_hello
    def print_sum(a, b):
        """Adds two numbers and prints the sum"""
        print(a + b)

    print_sum(10, 20)
    print_sum_docstring = print_sum.__doc__
    print(print_sum_docstring)


def check_inputs(a, *args, **kwargs):
    import time
    for value in a:
        time.sleep(0.01)
        print('Finished checking inputs')


def check_outputs(a, *args, **kwargs):
    import time
    for value in a:
        time.sleep(0.01)
    print('Finished checking outputs')


def check_everything(func):
    from functools import wraps

    @wraps(func)
    def wrapper(*args, **kwargs):
        check_inputs(*args, **kwargs)
        result = func(*args, **kwargs)
        check_outputs(result)
        return result

    return wrapper


def measuring_decorator_overhead():
    import time
    @check_everything
    def duplicate(my_list):
        """Return a new list that repeats the input twice"""
        return my_list + my_list

    t_start = time.time()
    duplicated_list = duplicate(list(range(50)))
    t_end = time.time()
    decorated_time = t_end - t_start

    t_start = time.time()
    # Call the original function instead of the decorated one
    duplicated_list = duplicate.__wrapped__(list(range(50)))
    t_end = time.time()
    undecorated_time = t_end - t_start

    print('Decorated time: {:.5f}s'.format(decorated_time))
    print('Undecorated time: {:.5f}s'.format(undecorated_time))


def main():
    # print_the_return_type_example()
    # counter_example()
    # preserving_docstrings_when_decorating_functions1()
    measuring_decorator_overhead()


if __name__ == '__main__':
    main()
