import pandas as pd
import numpy as np

"""
Docstrings:
 + Docstrings are a Python best practice that will make your code much easier to use, read, and maintain.
 
Docstring Formats:
 + Google Style (*)
 + Numpydoc (*)
 + reStructuredText
 + EpyText
 + (*) Indicates Popular Format
"""


def google_style(arg_1, arg_2=42):
    """Description of what the function does.

    Args:
        arg_1 (str): Description of arg_1 that can break onto the next line
        if needed.
        arg_2 (int, optional): Write optional when an argument has a default value.

    Returns:
        bool: Optional description of the return value
        Extra lines are not indented.

    Raises:
        ValueError: Include any error types that the function intentionally raises.

    Notes:
        See https://www.datacamp.com/community/tutorials/docstrings-python for more info.
    """


def numpydoc(arg_1, arg_2=42):
    """
    Description of what the function does.

    Parameters
    ----------
    arg_1 : str
        Description of arg_1
    arg_2 : int, optional
        Write optional when an argument has a default value.
        Default=42.

    Returns
    -------
    bool
        Can include a description of return value
        Replace "Returns" with "Yields" if this function is a generator.
    """


def anatomy_of_a_docstring():
    """
    Description of what the function does.

    Description of the arguments, if any.

    Description of the return value(s), if any.

    Description of errors raised, if any.

    Optional extra notes or example of usage.
    """


def a_complex_function_in_need_of_docstring(df, new_names):
    """Split a DataFrame's columns into two halves and then stack them vertically,
    returning a new DataFrame with 'new_names' as the column names.

    :param df: (DataFrame) The DataFrame to split.
    :param new_names: (iterable of str) The column names for the new DataFrame
    :return: DataFrame
    """
    half = int(len(df.columns) / 2)
    left = df.iloc[:, :half]
    right = df.iloc[:, half:]
    return pd.DataFrame(data=np.vstack([left.values, right.values]), columns=new_names)


def the_answer():
    """Return the answer to life, the universe, and everything.

    Returns:
        int
    """
    return 42


def retrieving_docstrings():
    print(the_answer.__doc__)


def retrieving_docstrings_with_getdoc():
    import inspect
    print(inspect.getdoc(the_answer))


"""
DRY and "Do One Thing"

Advantages of doing one thing:
 + The code becomes more:
    + More flexible
    + More easily understood
    + Simpler to test
    + Simpler to debug
    + Easier to change
    
Code smells and refactoring:
 + Repeating yourself and doing more than one thing are examples of code smells that need refactoring!
 
 
Pass By Assignment:

A surprising example:
"""


def a_surprising_example():
    # List are mutable
    my_list = [1, 2, 3]
    foo(my_list)
    print(my_list)

    # Vars are not
    my_var = 3
    bar(my_var)
    print(my_var)


def foo(x):
    x[0] = 99


def bar(x):
    x = x + 90


"""
Immutable Objects:
 + int
 + float
 + bool
 + string
 + bytes
 + tuple
 + frozenset
 + None
 
Mutable Objects:
 + list
 + dict
 + set
 + bytearray
 + objects
 + functions
 + almost everything else!
 
Mutable default arguments are dangerous as hell! like an empty list... I'm looking at you Brian!
Default to None and then set to empty list inside the function!
"""


def main():
    # retrieving_docstrings()
    # retrieving_docstrings_with_getdoc()
    a_surprising_example()


if __name__ == '__main__':
    main()
