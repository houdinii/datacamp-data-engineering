"""
In this chapter, you'll learn how to make sure that objects that store the same data are considered equal, how to define and
customize string representations of objects, and even how to create new error types. Through interactive exercises, you’ll learn
how to further customize your classes to make them work more like standard Python data types.
"""

"""
Operator Overloading: Comparison
--------------------------------

Overloading __eq__()
+ __eq__() is called when 2 objects of a class are compared using ==
+ accepts 2 arguments, self and other - objects to compare
+ returns a boolean

Other Comparison Operators:
---------------------------

|----------------|-------------|
|  Operator      |  Method     |
|----------------|-------------|
| ==             | __eq__()    |
| !=             | __ne__()    |
| >=             | __ge__()    |
| <=             | __le__()    |
| >              | __gt__()    |
| <              | __lt__()    |
|----------------|-------------|

+ __hash__() to use objects as dictionary keys and in sets


String Representation Overloading:
----------------------------------
__str__()
+ print(obj), str(obj)
+ informal, for end user
+ (Str)ing representation

    print(np.array([1,2,3]))
    >>> [1 2 3]
    str(np.array([1,2,3]))
    >>> [1 2 3]
    
__repr__()
+ repr(obj), printing in console
+ formal, for developer 
+ (Repr)oducible (Repr)esentation
+ fallback for print()

    repr(np.array([1,2,3]))
    >>> array([1,2,3])
    np.array([1,2,3])
    
    
Exceptions:
-----------
+ Prevent the program from terminating when an exception is raised
+ try - except - finally

    try:
      # Try running some code
    except ExceptionNameHere:
      # Run this if ExceptionNameHere happens
    except AnotherExceptionNameHere:
      # Run this if AnotherExceptionNameHere happens
    ...
    finally:  # <--- optional
      # Run this code no matter what
      
      
Exceptions Are Classes:
+ Standard exceptions are inherited from BaseException or Exception

BaseException
+-- Exception
    +-- ArithmeticError
    |   +-- FloatingPointError
    |   +-- OverflowError
    |   +-- ZeroDivisionError
    +--TypeError
    +--ValueError
    |   +-- UnicodeError
    |       +-- UnicodeDecodeError
    |       +-- UnicodeEncodeError
    |       +-- UicodeTranslateError
    +-- RuntimeError
   ...
+-- SystemExit
...    

Custom Exceptions:
+ Inherit from Exception or one of its subclasses
+ Usually an empty class

    class BalanceError(Exception): pass
"""


class BalanceError(Exception): pass


class Customer:
    def __init__(self, id, name, balance=0):
        if balance < 0:
            raise BalanceError("Balance has to be non-negative")
        else:
            self.id, self.name, self.balance = id, name, balance

    def __eq__(self, other):
        print("__eq__() is called")

        # Returns True if all attributes match
        return (self.id == other.id) and (self.name == other.name)

    def __str__(self):
        cust_str = """
Customer: {name}
Balance:  ${balance}.00
        """.format(name=self.name, balance=self.balance)
        return cust_str

    def __repr__(self):
        # Notice the '...' around name
        return "Customer('{name}', {balance})".format(name=self.name, balance=self.balance)


def variables_are_references():
    customer1 = Customer()
    customer2 = Customer()
    print(customer1 == customer2)  # Outputs False
    print(customer1)               # <__main__.Customer object at 0x00000136029D6070>
    print(customer2)               # <__main__.Customer object at 0x00000136029D60A0>


def comparion_of_objects():
    customer1 = Customer(123, "Maryam Azar")
    customer2 = Customer(123, "Maryam Azar")
    print(customer1 == customer2)  # Outputs True now that we overloaded __eq__

    customer1 = Customer(321, "Maryam Azar")
    customer2 = Customer(123, "Maryam Azar")
    print(customer1 == customer2)  # Outputs True now that we overloaded __eq__


def implementation_str():
    cust = Customer(1001, "Maryam Azar", 3000)
    print(cust)


def make_list_of_ones(length):
    if length <= 0:
        raise ValueError('Invalid Length!')  # Stops execution and raises an error
    return [1] * length


def raising_exceptions():
    make_list_of_ones(-1)


def custom_exceptions():
    # a = Customer(1, "Brian Barnes", -1)
    try:
        a = Customer(1, "Brian Barnes", -1)
    except BalanceError:
        a = Customer(1, "Brian Barnes", 0)
    print(a)


def main():
    # variables_are_references()
    # comparion_of_objects()
    # implementation_str()
    # raising_exceptions()
    custom_exceptions()


if __name__ == '__main__':
    main()
