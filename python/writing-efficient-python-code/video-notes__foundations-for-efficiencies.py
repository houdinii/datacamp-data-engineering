"""
Welcome Video:

Course Overview:
+ Your code should be a tool used to gain insights.
    + Not something that leaves you waiting for results.
+ In this course, you will learn:
    + How to write clean, fast, and efficient Python code.
    + How to profile your code for bottlenecks.
    + How to eliminate bottlenecks and bad design patterns.

Defining Efficient:
+ Writing efficient Python code means:
    + Minimal completion time (fast runtime).
    + Minimal resource consumption (small memory footprint).

Defining Pythonic:
+ Writing efficient Python code:
    + Focuses on readability.
    + Using Python's constructs as intended (i.e. Pythonic).

Things I Should Know:
+ Data types typically used in Data Science (Course: Data Types for Data Science)
+ Writing and using your own functions (Course: Python Data Science Toolbox Part 1)
+ Anonymous Functions - lambda Expressions (Course: Python Data Science Toolbox Part 1)
+ Writing and using list comprehensions (Course: Python Data Science Toolbox Part 2)
"""


def pythonic_vs_non_pythonic_example():
    # Non-Pythonic
    doubled_numbers = []

    for i in range(len(numbers)):
        doubled_numbers.append(numbers[i] * 2)

    # Pythonic
    doubled_numbers = [x * 2 for x in numbers]


"""
Building with built-ins:

The Python Standard Library:
+ Python 3.6 Standard Library
    + Part of every standard Python installation.
+ Built-in types:
    + list, tuple, set, dict, and others
+ Built-in functions:
    + print(), len(), range(), round(), enumerate(), map(), zip(), and others.
+ Built-in modules:
    + os, sys, itertools, collections, math, and others.

Built-in function: range()
Explicitly typing a list of numbers vs built in:
Explicit: nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
or using range:
"""


def using_range_example():
    # range(start, stop)
    nums = range(0, 11)
    nums_list = list(nums)
    print(type(nums))
    print(nums_list)

    # range(stop)
    nums = range(11)
    nums_list = list(nums)
    print(type(nums))
    print(nums_list)

    # range(start, stop, step) step is number to add inbetween each point in the range (i.e. step of 2: 0, 2, 4, 6...)
    even_nums = range(2, 11, 2)
    even_nums_list = list(even_nums)
    print(type(even_nums))
    print(even_nums_list)

    # Create a new list of odd numbers from 1 to 11 by unpacking a range object using *
    nums_list2 = [*range(1, 12, 2)]
    print(type(nums_list2))
    print(nums_list2)


"""
Built-in function: enumerate()

enumerate() creates an indexed list of objects:
"""


def using_enumerate_example():
    letters = ['a', 'b', 'c', 'd']
    indexed_letters = enumerate(letters)
    print(indexed_letters)
    print(type(indexed_letters))
    indexed_letters_list = list(indexed_letters)
    print(indexed_letters_list)

    # Specifying a start value:
    indexed_letters2 = enumerate(letters, start=5)
    print(indexed_letters2)
    print(type(indexed_letters2))
    indexed_letters_list = list(indexed_letters2)
    print(indexed_letters_list)


"""
Built-in function: map()
map() applies a function over an object:
"""


def using_map_example():
    nums = [1.5, 2.3, 3.4, 4.6, 5.0]
    rnd_nums = map(round, nums)
    print(rnd_nums)
    print(type(rnd_nums))
    print(list(rnd_nums))

    # map with lambda (anonymous function)
    nums = [1, 2, 3, 4, 5]
    sqrd_nums = map(lambda x: x ** 2, nums)
    print(sqrd_nums)
    print(type(sqrd_nums))
    print(list(sqrd_nums))


"""
The Power of NumPy Arrays:

NumPy array overview:
+ Alternative to Python lists
"""


def numpy_array_overview_example():
    nums_list = list(range(5))
    print(nums_list)
    import numpy as np
    nums_np = np.array(range(5))
    print(nums_np)

    # NumPy array homogeneity
    nums_np_ints = np.array([1, 2, 3])
    print(nums_np_ints)
    print(nums_np_ints.dtype)
    nums_np_floats = np.array([1, 2.5, 3])
    print(nums_np_floats)
    print(nums_np_floats.dtype)


"""
NumPy array broadcasting:
+ Python lists don't support broadcasting
"""


def numpy_array_broadcasting_example():
    import numpy as np
    nums = [-2, -1, 0, 1, 2]
    # nums ** 2 throws an TypeError here

    # List approach
    # For loop (inefficient option)
    sqrd_nums = []
    for num in nums:
        sqrd_nums.append(num**2)
    print(sqrd_nums)

    # List comprehension (Better, but not best)
    sqrd_nums = [num ** 2 for num in nums]
    print(sqrd_nums)

    # NumPy array broadcasting for the win!
    sqrd_nums = np.array(nums) ** 2
    print(sqrd_nums)


"""
Array indexing:
multi-dimension lists: example[0][1]
multi-dimension np array: example[0,1]
"""


def numpy_array_indexing_vs_lists():
    import numpy as np
    # 2D List
    nums2 = [[1, 2, 3],
             [4, 5, 6]]

    print(nums2[0][1])
    print([row[0] for row in nums2])

    # 2D NumPy Array
    nums2_np = np.array(nums2)
    print(nums2_np[0, 1])
    print(nums2_np[:, 0])


"""
NumPy array boolean indexing
Boolean indexing uses inequalities
"""


def boolean_indexing_example():
    import numpy as np
    nums = [-2, -1, 0, 1, 2]
    nums_np = np.array(nums)
    print(nums_np > 0)           # returns boolean mask array of T/F values
    print(nums_np[nums_np > 0])  # returns an array of True values, or values > 0 in this case

    # The same thing but done with an inefficient for loop
    pos = []
    for num in nums:
        if num > 0:
            pos.append(num)
    print(pos)


def main():
    numpy_array_indexing_vs_lists()


if __name__ == '__main__':
    main()
