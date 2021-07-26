"""
A taste of things to come
In this exercise, you'll explore both the Non-Pythonic and Pythonic ways of looping over a list.

names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']

Suppose you wanted to collect the names in the above list that have six letters or more. In other programming languages, the typical
approach is to create an index variable (i), use i to iterate over the list, and use an if statement to collect the names with six
letters or more:

i = 0
new_list= []
while i < len(names):
    if len(names[i]) >= 6:
        new_list.append(names[i])
    i += 1

Let's explore some more Pythonic ways of doing this.

Instructions:
1.) Print the list, new_list, that was created using a Non-Pythonic approach.
2.) A more Pythonic approach would loop over the contents of names, rather than using an index variable. Print better_list.
3.) The best Pythonic way of doing this is by using list comprehension. Print best_list.
"""

names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']


def non_pythonic():
    # Print the list created using the Non-Pythonic approach
    i = 0
    new_list = []
    while i < len(names):
        if len(names[i]) >= 6:
            new_list.append(names[i])
        i += 1
    print(new_list)


def better_list():
    # Print the list created by looping over the contents of names
    better = []
    for name in names:
        if len(name) >= 6:
            better.append(name)
    print(better)


def pythonic():
    # Print the list created by using list comprehension
    best_list = [name for name in names if len(name) >= 6]
    print(best_list)

    """
    Great work! Don't get too caught up in the coding concepts just yet (you'll practice using lists, for loops, and list 
    comprehensions later on). The important thing to notice here is that following some of Python's guiding principles allows 
    you to write cleaner and more efficient code.

    Remember, Pythonic code == efficient code. You'll explore these, and other, Pythonic concepts later on in the course, but for now, 
    this is just a taste of things to come!
    """


def built_in_practice_range():
    """
    Built-in practice: range()
    In this exercise, you will practice using Python's built-in function range(). Remember that you can use range() in a
    few different ways:

    1) Create a sequence of numbers from 0 to a stop value (which is exclusive). This is useful when you want to create a simple
    sequence of numbers starting at zero:

            range(stop)

            # Customer
            list(range(11))

            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    2) Create a sequence of numbers from a start value to a stop value (which is exclusive) with a step size. This is useful when
    you want to create a sequence of numbers that increments by some value other than one. For example, a list of even numbers:

            range(start, stop, step)

            # Customer
            list(range(2,11,2))

            [2, 4, 6, 8, 10]

    Instructions:
    + Create a range object that starts at zero and ends at five. Only use a stop argument.
    + Convert the nums variable into a list called nums_list.
    + Create a new list called nums_list2 that starts at one, ends at eleven, and increments by two by unpacking a range object using
      the star character (*).
    """
    # Create a range object that goes from 0 to 5
    nums = range(6)
    print(type(nums))

    # Convert nums to a list
    nums_list = list(nums)
    print(nums_list)

    # Create a new list of odd numbers from 1 to 11 by unpacking a range object
    nums_list2 = [*range(1, 12, 2)]
    print(nums_list2)

    """
    Nicely done! Notice that using Python's range() function allows you to create a range object of numbers without explicitly 
    typing them out. You can convert the range object into a list by using the list() function or by unpacking it into a list using 
    the star character (*). Cool!
    """


def built_in_practice_enumerate():
    """
    Built-in practice: enumerate()
    In this exercise, you'll practice using Python's built-in function enumerate(). This function is useful for obtaining an indexed list. For example, suppose you had a list of people that arrived at a party you are hosting. The list is ordered by arrival (Jerry was the first to arrive, followed by Kramer, etc.):

            names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']

    If you wanted to attach an index representing a person's arrival order, you could use the following for loop:

            indexed_names = []
            for i in range(len(names)):
                index_name = (i, names[i])
                indexed_names.append(index_name)

            [(0,'Jerry'),(1,'Kramer'),(2,'Elaine'),(3,'George'),(4,'Newman')]

    But, that's not the most efficient solution. Let's explore how to use enumerate() to make this more efficient.

    Instructions:
    + Instead of using for i in range(len(names)), update the for loop to use i as the index variable and name as the iterator
      variable and use enumerate().
    + Rewrite the previous for loop using enumerate() and list comprehension to create a new list, indexed_names_comp.
    + Create another list (indexed_names_unpack) by using the star character (*) to unpack the enumerate object created from
      using enumerate() on names. This time, start the index for enumerate() at one instead of zero.
    """

    # Rewrite the for loop to use enumerate
    indexed_names = []
    for i, name in enumerate(names):
        index_name = (i, name)
        indexed_names.append(index_name)
    print(indexed_names)

    # Rewrite the above for loop using list comprehension
    indexed_names_comp = [(i, name) for i, name in enumerate(names)]
    print(indexed_names_comp)

    # Unpack an enumerate object with a starting index of one
    indexed_names_unpack = [*enumerate(names, 1)]
    print(indexed_names_unpack)

    """
    Awesome! Using Python's built-in enumerate() function allows you to create an index for each item in the object you give it. 
    You can use list comprehension, or even unpack the enumerate object directly into a list, to write a nice simple one-liner.
    """


def built_in_practice_map():
    """
    Built-in practice: map()
    In this exercise, you'll practice using Python's built-in map() function to apply a function to every element of an object.
    Let's look at a list of party guests:

            names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']

    Suppose you wanted to create a new list (called names_uppercase) that converted all the letters in each name to uppercase.
    You could accomplish this with the below for loop:

            names_uppercase = []

            for name in names:
              names_uppercase.append(name.upper())

            ['JERRY', 'KRAMER', 'ELAINE', 'GEORGE', 'NEWMAN']

    Let's explore using the map() function to do this more efficiently in one line of code.

    Instructions:
    + Use map() and the method str.upper() to convert each name in the list names to uppercase. Save this to the variable names_map.
    + Print the data type of names_map.
    + Unpack the contents of names_map into a list called names_uppercase using the star character (*).
    + Print names_uppercase and observe its contents.
    """
    # Use map to apply str.upper to each element in names
    names_map = map(str.upper, names)

    # Print the type of the names_map
    print(type(names_map))

    # Unpack names_map into a list
    names_uppercase = [*names_map]

    # Print the list created above
    print(names_uppercase)

    """
    Well done! You used Python's built-in map() function to apply the str.upper() method to each element in the names object. 
    Later on in the course, you'll explore how using map() can provide some efficiency improvements to your code.
    """


def practice_with_numpy_arrays_1():
    """
    Practice with NumPy arrays
    Let's practice slicing numpy arrays and using NumPy's broadcasting concept. Remember, broadcasting refers to a numpy array's
    ability to vectorize operations, so they are performed on all elements of an object at once.

    A two-dimensional numpy array has been loaded into your session (called nums) and printed into the console for your convenience.
    numpy has been imported into your session as np.

    Instructions:
    + Print the second row of nums.
    + Print the items of nums that are greater than six.
    + Create nums_dbl that doubles each number in nums.
    + Replace the third column in nums with a new column that adds 1 to each item in the original column.
    """
    import numpy as np
    nums = np.array([[1,  2,  3,  4,  5], [6,  7,  8,  9, 10]])

    # Print second row of nums
    print(nums[0, 1])

    # Print all elements of nums that are greater than six
    print(nums[nums > 6])

    # Double every element of nums
    nums_dbl = nums * 2
    print(nums_dbl)

    # Replace the third column of nums
    nums[:, 2] = nums[:, 2] + 1
    print(nums)

    """
    Well done! You're slicing numpy arrays like a pro and learning how to take advantage of NumPy's broadcasting concept. Using numpy 
    arrays allows you to take advantage of an array's memory efficient nature and easily perform mathematical operations on your data.
    """


def bringing_it_all_together_festivus():
    """
    Bringing it all together: Festivus!
    In this exercise, you will be throwing a party—a Festivus if you will!

    You have a list of guests (the names list). Each guest, for whatever reason, has decided to show up to the party in 10-minute
    increments. For example, Jerry shows up to Festivus 10 minutes into the party's start time, Kramer shows up 20 minutes into the
    party, and so on and so forth.

    We want to write a few simple lines of code, using the built-ins we have covered, to welcome each of your guests and let them
    know how many minutes late they are to your party. Note that numpy has been imported into your session as np and the names list
    has been loaded as well.

    Let's welcome your guests!

    Instructions:

    1.) Use range() to create a list of arrival times (10 through 50 incremented by 10). Create the list arrival_times by unpacking
    the range object.

    2.) You realize your clock is three minutes fast. Convert the arrival_times list into a numpy array (called arrival_times_np)
    and use NumPy broadcasting to subtract three minutes from each arrival time.

    3.) Use list comprehension with enumerate() to pair each guest in the names list to their updated arrival time in the new_times
    array. You'll need to use the index variable created from using enumerate() on new_times to index the names list.

    4.) A function named welcome_guest() has been pre-loaded into your session. Use map() to apply this function to each element of
    the guest_arrivals list and save it as the variable welcome_map.
    """
    import numpy as np
    # Create a list of arrival times
    arrival_times = [*range(10, 60, 10)]

    print(arrival_times)

    # Create a list of arrival times
    arrival_times = [*range(10, 60, 10)]

    # Convert arrival_times to an array and update the times
    arrival_times_np = np.array(arrival_times)
    new_times = arrival_times_np - 3

    print(new_times)

    # Use list comprehension and enumerate to pair guests to new times
    guest_arrivals = [(names[i], time) for i, time in enumerate(new_times)]

    print(guest_arrivals)

    # Map the welcome_guest function to each (guest,time) pair
    welcome_map = map(welcome_guest, guest_arrivals)

    guest_welcomes = [*welcome_map]
    print(*guest_welcomes, sep='\n')

    """
    Congratulations and happy Festivus! You're using Python built-ins like a pro and well on your way to writing efficient Python 
    code. Believe it or not, there is a way to make these simple lines of code even more efficient! We'll cover this in a future 
    chapter, so continue on to see how!
    """


def welcome_guest(argument):
    """Helper for bringing_it_all_together_festivus

    :returns:
    A sentence from the tuple argument
    """
    return f"Welcome to Festivus {argument[0]}... You're {argument[1]} min late."


def main():
    # non_pythonic()
    # better_list()
    # pythonic()
    # built_in_practice_range()
    # built_in_practice_enumerate()
    # built_in_practice_map()
    # practice_with_numpy_arrays_1()
    bringing_it_all_together_festivus()


if __name__ == '__main__':
    main()
