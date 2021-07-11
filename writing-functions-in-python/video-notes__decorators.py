import pandas as pd
import numpy as np


"""
Decorators:

Decorators are an extremely powerful concept in Python. They allow you to modify the behavior of a function without changing the code 
of the function itself. This chapter will lay the foundational concepts needed to thoroughly understand decorators (functions as 
objects, scope, and closures), and give you a good introduction into how decorators are used and defined. This deep dive into Python 
internals will set you up to be a superstar Pythonista.


"""


"""
Closures: A closure in Python is a tuple of variables that are no longer in scope, but that a function needs in order to run.


Attaching nonlocal variables to nested functions:
The function foo() defines a nested function bar() that prints the value of "a". foo() returns this new function, so when we say
"func=foo()" we are assigning the bar() function to the variable "func". Now what happens when we call func()? As expected, it prints 
the value of variable "a", which is 5. But wait a minute, how does function "func()" know anything about variable "a"? "a" is defined 
in foo()'s scope, not bar()'s. You would think that "a" would not be observable outside of the scope of foo(). That's where closures 
come in. When foo() returned the new bar() function, Python helpfully attached any nonlocal variable that bar() was going to need to
the function object. Those variables get stored in a tuple in the "__closure__" attribute of the function. The closure for "func" 
has one variable, and you can view the value of that variable by accessing the "cell_contents" of the item.
"""


def foo():
  a = 5

  def bar():
    print(a)

  return bar


def closures_first_example():
  func = foo()
  func()
  print(f"Type of func(): {str(type(func))}")
  print(f"Type of func.__closure__: {str(type(func.__closure__))}")
  print(f"func.__closure:\n{func.__closure__[0].cell_contents}")


"""
Closures and deletion
x = 25
def foo():
  def bar():
    print(value)
  return bar

my_func = foo(x)
my_func()
"""


def closures_and_deletion():
  x = 25

  def foo(value):
    def bar():
      print(value)
    return bar
  my_func = foo(x)
  my_func()
  del(x)
  my_func()
  print(len(my_func.__closure__))
  print(my_func.__closure__[0].cell_contents)


def closures_and_overwriting():
  x = 25

  def foo(value):
    def bar():
      print(value)
    return bar

  x = foo(x)
  x()
  print(len(x.__closure__))
  print(x.__closure__[0].cell_contents)


"""
Key Concepts:

Nested function - A function defined inside another function:

# outer function
def parent():
  # nested function
  def child():
    pass
  return child
  
Nonlocal variables - Variables defined in the parent function that are used by the child function:

def parent(arg_1, arg_2):
  # From child()'s point of view,
  # 'value' and 'my_dict' are nonlocal variables,
  # as are 'arg_1' and 'arg_2'
  value = 22
  my_dict = {'chocolate': 'yummy'}
  
  def child():
    print(2 * value)
    print(my_dict['chocolate'])
    print(arg_1 + arg_2)
  return child
  
Closure - Nonlocal variables attached to a returned function:

def parent(arg_1, arg_2):
  value = 22
  my_dict = {'chocolate': 'yummy'}
  
  def child():
    print(2 * value)
    print(my_dict['chocolate'])
    print(arg_1 + arg_2)
  return child
  
new_function = parents(3, 4)
print([cell.cell_contents for cell in new_function.__closure__])

Why does all this matter?
Decorators use:
  + Functions as objects
  + Nested functions
  + Nonlocal scope
  + Closures
"""


"""
Decorators - A wrapper that you can place around a function that changes that function's behavior. They can modify the inputs, 
  outputs, and even the functionality.

Normal functions:   {inputs} >>> function() >>> {outputs}
Decorated functions: {inputs} >>> @decorator >>> function() >>> @decorator >>> {outputs}

What does a decorator look like? Here the double_args decorator modifies the behavior of the multiply() function. double_args is a
  decorator that multiplies every argument by two before passing them to the decorated function.

Step one: Stub out the decorator function
def multiply(a, b):
  return a * b
  
def double_args(func):
  # Define a new function that we can modify
  def wrapper(a, b):
    # For now just call the unmodified function
    return func(a, b)
  # return the new function
  return wrapper
  
new_multiply = double_args(multiply)
new_multiply(1, 5)  # >>> 5

Step two: Perform the actual modifications
def multiply(a, b):
  return a * b
  
def double_args(func):
  # Define a new function that we can modify
  def wrapper(a, b):
    # Call the passed in function, but double each argument
    return func(a * 2, b * 2) 
  return wrapper
new_multiply = double_args(multiply)
new_multiply(1, 5)  
"""


def decorators_first_example():
  def double_args(func):
    # Define a new function that we can modify
    def wrapper(a, b):
      # Call the passed in function, but double each argument
      return func(a * 2, b * 2)

    return wrapper

  @double_args
  def multiply(a, b):
    return a * b

  # new_multiply = double_args(multiply)
  print(multiply(1, 5))


def defining_a_decorator():
  def print_before_and_after(func):
    def wrapper(*args):
      print('Before {}'.format(func.__name__))
      # Call the function being decorated with *args
      func(*args)
      print('After {}'.format(func.__name__))

    # Return the nested function
    return wrapper

  @print_before_and_after
  def multiply(a, b):
    print(a * b)

  multiply(5, 10)

  """
  What a darling decorator! The decorator print_before_and_after() defines a nested function wrapper() that calls whatever function 
  gets passed to print_before_and_after(). wrapper() adds a little something else to the function call by printing one message before 
  the decorated function is called and another right afterwards. Since print_before_and_after() returns the new wrapper() function, 
  we can use it as a decorator to decorate the multiply() function.
  """


def main():
  # closures_first_example()
  # closures_and_deletion()
  # closures_and_overwriting()
  # decorators_first_example()
  defining_a_decorator()


if __name__ == '__main__':
    main()
