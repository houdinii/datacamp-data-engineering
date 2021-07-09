import contextlib
import os

import numpy as np
import pandas as pd


"""
Using Context Managers:

Context Manager - a type of function that sets up a context for your code to run in, runs your code, 
and then removes the context.

Catered party as a context:
Context managers:             Caterers:
-----------------             ---------
+ Set up a context            + Set up the tables with food and drink
+ Run your code               + Let you and your friends have a party
+ Remove the context          + Cleaned up and removed the tables

A real-world example:
open() does three things below:
+ Sets up a context by opening a file
+ Lets you run any code you want on that file
+ Removes the context by closing the file
"""


def a_real_world_example(file=None):
  if file is not None:
    with open(file) as my_file:
      text = my_file.read()
      length = len(text)
    print(f'The file is {length} characters long!')


"""
Using a context manager:
with <context-manager>(<args>) as <variable-name>:
  # Run your code here
  # This code is running "inside the context"
# This code runs after context is removed

Writing Context Managers:

Two ways to define a context manager:
 + Class-based
    + A class that has special __enter__() and __exit__() methods
 + (*) Function Based
    + Decorating a certain kind of function.
    
Five steps to creating a context manager:
 1.) Define a function
 2.) (optional) Add any set up code your context needs.
 3.) Use the "yield" keyword
 4.) (optional) Add any teardown code your context needs.
 5.) Add the '@contextlib.contextmanager' deorator.
"""


@contextlib.contextmanager
def my_context():
  # Add any set up code you need
  print('hello')
  yield 42
  # Add any teardown code you need
  print('goodbye')


@contextlib.contextmanager
def database(url):
  """An example of setup and teardown"""
  # Setup database connection
  db = postgres.connect(url)
  yield db
  # Tear down database connect
  db.disconnect()


@contextlib.contextmanager
def in_dir(path):
  # Save current working directory
  old_dir = os.getcwd()

  # Switch to new working directory
  os.chdir(path)

  yield

  # Change back to previous working directory
  os.chdir(old_dir)


def using_context_managers():
  # with my_context() as foo:
  #   print(f'foo is {foo}')
  #
  # url = 'https://datacamp.com/data'
  # with database(url) as my_db:
  #   # noinspection SqlNoDataSourceInspection,SqlDialectInspection
  #   course_list = my_db.execute('SELECT * FROM courses')

  with in_dir('../writing-functions-in-python/'):
    print(os.listdir())


def bad_copy(src, dst):
  # can copy but breaks down if the file doesn't fit in memory:
  with open(src) as f_src:
    contents = f_src.read()
  with open(dst) as f_dst:
    f_dst.write(contents)


def nested_context_copy(src, dst):
  with open(src) as f_src:
    with open(dst) as f_dst:
      # Read and wriite each line, one at a time
      for line in f_src:
        f_dst.write(line)


"""Handling Errors"""


def connect_to_printer(ip):
  return "KKKK"


def get_printer(ip):
  """Stub function to display how to handle errors"""
  p = connect_to_printer(ip)

  try:
    yield
  finally:
    # This MUST be called or no one else will
    # be able to connect to the printer
    # Putting it the finally guarantees it gets done even if a sloppy
    # programmer gets a KeyError
    p.disconnect()
    print('disconnected from printer')


def handling_errors():
  doc = {'text': 'This is my text.'}
  with get_printer('127.0.0.1') as printer:
    printer.print_page(doc['txt'])  # Throws KeyError


"""
Context manager patterns:
Open    Close
Lock    Release
Change  Reset
Enter   Exit
Start   Stop
Setup   Teardown
Connect Disconnect
"""


def main():
  using_context_managers()
  handling_errors()


if __name__ == '__main__':
  main()
