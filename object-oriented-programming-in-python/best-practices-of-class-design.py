"""
Liskov Substitution Priniciple: Base class should be interchangleable with any of its
subclasses without altering any properties of the program.

Syntactically
+ Function signatures are compatible
    - Arguments, returned values
Semantically
+ The state of the object and the program remains constant.
    - Subclass method doesn't strengthen input conditions.
    - Subclass method doesn't weaken output conditions.
    - No additional exceptions.

Violating LSP
-> Syntactic Incompatibility
    BankAccount.withdraw() requires 1 parameter, but CheckingAccount.withdraw() requires 2

-> Subclass strengthening input conditions
    BankAccount.withdraw() accepts any amount, but CheckingAccount.withdraw() assumes
    that the amount is limited

-> Subclass weakening output conditions
    BankAccount.withdraw() can only leave a positive balance or cause an error,
    CheckingAccount.withdraw() can leave balance negative.

-> Changing additional attributes in subclass's method
-> Throwing additional exceptions in subclass's method

If it violates LSP, then it shouldn't be using inheritance or should be rewritten.

Restricting Access to Class Members:
+ Naming conventions
+ Use @property to customize access
+ Overriding __getattr__() and __setattr__()

Naming Convention: Internal Attributes

obj._att_name, obj._method_name()
+ Starts with a single '_' which means 'internal'
+ Not a part of the public API
+ As a class user: "don't touch this"
+ As a class developer: use for implementation details, helper functions...
+ df._is_mixed_type, datetime._ymd2ord()

Naming Convention: Pseudoprivate Attributes

obj.__attr_name, obj.__method_name()
+ Starts but doesn't end with __ -> 'private'
+ Not inherited
+ Name mangling: obj.__attr_name is interpreted as obj._MyClass__attr_name
+ Used to prevent name clashes in inherited classes
+ Leading and trailing __ are ONLY used for built-in Python methods (like __init__)

Properties
==========
+ Use 'protected' attribute with leading _ to store data
+ Use @property on a method whose name is exactly the name of the restricted attribute;
    - return the internal attribute.
+ Use @attr.setter on a method attr() that will be called on obj.attr = value
    - The value to assign passed as argument.

class Employer:
    def __init__(self, name, new_salary):
        self._salary = new_salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        if new_salary < 0:
            raise ValueError("Invalid Salary")
        self._salary = new_salary

emp = Employee("Miriam Azari", 35000)
# accessing the 'property'
emp.salary          # >>> 35000
emp.salary = 60000  # @salary.setter
emp.salary = -1000  # ValueError!


Why use @property?
+ User-facing: Behave like attributes
+ Developer-facing: Give control of access

Other Possibilities:
+ Do not add @attr.setter
+ Instead, create a read-only property
    + Add @attr.getter
        - Use for the method that is called when the property's value is retrieved.
    + Add @attr.deleter
        - Use for the method that is called when the property is deleted using del


What's Next?

Functionality
+ Multiple inheritance and mixin classes
+ Overriding built-in operators like +
+ __getattr__(), __setattr__()
+ Custom iterators
+ Abstract base classes
+ Dataclasses (new in Python 3.7)

Design:
+ Solid Principles:
 - S : Single-responsibility principle
 - O : Open-closed principle
 - L : Liskov substitution principle
 - I : Interface segregation principle
 - D : Dependency inversion principle

"""


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


def main():
    pass


if __name__ == '__main__':
    main()
