import numpy as np


def using_timeit_your_turn():
    """
Using %timeit: your turn!
You'd like to create a list of integers from 0 to 50 using the range() function. However, you are unsure whether using list comprehension or unpacking the range object into a list is faster. Let's use %timeit to find the best implementation.

For your convenience, a reference table of time orders of magnitude is provided below (faster at the top).

symbol	    name	        unit (s)
------      ----            --------
ns	        nanosecond	    10^-9
µs (us)	    microsecond	    10^-6
ms	        millisecond	    10^-3
s	        second	        100

Instructions:
 1.) Use list comprehension and range() to create a list of integers from 0 to 50 called nums_list_comp.
 2.) Use range() to create a list of integers from 0 to 50 and unpack its contents into a list called nums_unpack.
    """
    # Create a list of integers (0-50) using list comprehension
    nums_list_comp = [num for num in range(0, 51)]
    print(nums_list_comp)

    # Create a list of integers (0-50) by unpacking range
    nums_unpack = [*range(0, 51)]
    print(nums_unpack)


def using_timeit_formal_name_or_literal_syntax():
    """
Using %timeit: formal name or literal syntax
Python allows you to create data structures using either a formal name or a literal syntax. In this exercise, you'll explore how
using a literal syntax for creating a data structure can speed up runtimes.

data structure	 formal name  literal syntax
list	         list()	      []
dictionary	     dict()	      {}
tuple	         tuple()	  ()

Instructions:
Create an empty list called formal_list using the formal name (list()).
Create an empty list called literal_list using the literal syntax ([]).
Print out the type of formal_list and literal_list to show that both naming conventions create a list.

"""
    # Create a list using the formal name
    formal_list = list()
    print(formal_list)

    # Create a list using the literal syntax
    literal_list = []
    print(literal_list)

    # Print out the type of formal_list
    print(type(formal_list))

    # Print out the type of literal_list
    print(type(literal_list))


def main():
    # using_timeit_your_turn()
    using_timeit_formal_name_or_literal_syntax()


if __name__ == '__main__':
    main()
