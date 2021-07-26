import pandas as pd
import numpy as np
from numpy import mean, std, minimum, maximum, random


def building_a_command_line_app():
  def load_data():
    return np.array([[72.1, 198.],
                     [69.8, 204.],
                     [63.2, 164.],
                     [64.7, 238.]])

  def get_user_input(prompt='Type a command: '):
    command = random.choice(['mean', 'std'])
    print(prompt)
    print('> {}'.format(command))
    return command

  # Add the missing function references to the function map
  function_map = {
    'mean': mean,
    'std': std,
    'minimum': minimum,
    'maximum': maximum
  }

  data = load_data()
  print(data)

  func_name = get_user_input()

  # Call the chosen function and
  print(function_map[func_name](data))


def load_and_plot_data(filename):
  """Load a data frame and plot each column.

  Args:
        filename (str): Path to a CSV file of data.

  Returns:
        pandas.DataFrame
  """
  df = pd.load_csv(filename, index_col=0)
  df.hist()
  return df


def has_docstring(func):
  """Check to see if the function `func` has a docstring.

  Args:
      func (callable): A function.

  Returns:
      bool
  """
  return func.__doc__ is not None


def as_2D(arr):
  """Reshape an array to 2 dimensions"""
  return np.array(arr).reshape(1, -1)


def log_product(arr):
  return np.exp(np.sum(np.log(arr)))


def reviewing_your_coworkers_code():
  # Call has_docstring() on the load_and_plot_data() function
  ok = has_docstring(load_and_plot_data)

  if not ok:
    print("load_and_plot_data() doesn't have a docstring!")
  else:
    print("load_and_plot_data() looks ok")

  # Call has_docstring() on the as_2D() function
  ok = has_docstring(as_2D)

  if not ok:
    print("as_2D() doesn't have a docstring!")
  else:
    print("as_2D() looks ok")

  # Call has_docstring() on the log_product() function
  ok = has_docstring(log_product)

  if not ok:
    print("log_product() doesn't have a docstring!")
  else:
    print("log_product() looks ok")


def create_math_function(func_name):
  if func_name == 'add':
    def add(a, b):
      return a + b
    return add
  elif func_name == 'subtract':
    # Define the subtract() function
    def subtract(x, y):
      return x - y
    return subtract
  else:
    print("I don't know that one")


def returning_functions_for_a_math_game():
  add = create_math_function('add')
  print('5 + 2 = {}'.format(add(5, 2)))

  subtract = create_math_function('subtract')
  print('5 - 2 = {}'.format(subtract(5, 2)))


"""
The nonlocal keyword: The same thing as global for normal functions, allows you to update a variable from a nested function located
in the parent function.

def foo():
  x = 10
  def bar():
    x = 200
    print(x)
  bar()
  print(x)
foo()
>>> 200
>>> 10

def foo():
  x = 10
  def bar():
    nonlocal x      # The different line
    x = 200
    print(x)
  bar()
  print(x)
foo()
>>> 200
>>> 200
"""

"""
Understanding scope: What four values does the below print?

x = 50

def one():
  x = 10
  
def two():
  global x
  x = 30
  
def three():
  x = 100
  print(x)
  
for func in [one, two, three]:
  func()
  print(x)
  
>>> 50, 30, 100, 30

Good job! 
- one() doesn't change the global x, so the first print() statement prints 50.
- two() does change the global x so the second print() statement prints 30.
- The print() statement inside the function three() is referencing the x value that is local to three(), so it prints 100.
- But three() does not change the global x value so the last print() statement prints 30 again.
"""

call_count = 0


def my_function():
  # Use a keyword that lets us update call_count
  global call_count
  call_count
  call_count += 1

  print(f"You've called my_function() {call_count} times!")


def modifying_variables_outside_local_scope():
  for _ in range(20):
    my_function()


def read_files():
  file_contents = None

  def save_contents(filename):
    # Add a keyword that lets us modify file_contents
    nonlocal file_contents
    if file_contents is None:
      file_contents = []
    with open(filename) as fin:
      file_contents.append(fin.read())

  for filename in ['1984.txt', 'MobyDick.txt', 'CatsEye.txt']:
    save_contents(filename)

  return file_contents


def modifying_variables_outside_local_scope_2():
  print('\n'.join(read_files()))


done = False


def wait_until_done():
  def check_is_done():
    # Add a keyword so that wait_until_done()
    # doesn't run forever
    global done
    if random.random() < 0.1:
      done = True

  while not done:
    check_is_done()


def modifying_variables_outside_local_scope_3():
  wait_until_done()
  print(f"Work done? {done}")
  """
  Stellar scoping! By adding global done in check_is_done(), you ensure that the done being referenced is the one that was set to 
  False before wait_until_done() was called. Without this keyword, wait_until_done() would loop forever because the done = True in 
  check_is_done() would only be changing a variable that is local to check_is_done(). Understanding what scope your variables are in
  will help you debug tricky situations like this one.
  """


def checking_for_closure():
  def return_a_func(arg1, arg2):
    def new_func():
      print('arg1 was {}'.format(arg1))
      print('arg2 was {}'.format(arg2))

    return new_func

  my_func = return_a_func(2, 17)

  # Show that my_func()'s closure is not None
  print(my_func.__closure__ is not None)

  # Show that there are two variables in the closure
  print(len(my_func.__closure__) == 2)

  # Get the values of the variables in the closure
  closure_values = [
    my_func.__closure__[i].cell_contents for i in range(2)
  ]
  print(closure_values == [2, 17])

  """
  Case closed! Your niece is relieved to see that the values she passed to return_a_func() are still accessible to the new 
  function she returned, even after the program has left the scope of return_a_func().

  Values get added to a function's closure in the order they are defined in the enclosing function (in this case, arg1 and then arg2),
  but only if they are used in the nested function. That is, if return_a_func() took a third argument (e.g., arg3) that wasn't used by 
  new_func(), then it would not be captured in new_func()'s closure.
  """


def closures_keep_your_values_safe():
  def my_special_function():
    print('You are running my_special_function()')

  def get_new_func(func):
    def call_func():
      func()

    return call_func

  new_func = get_new_func(my_special_function)

  # Redefine my_special_function() to just print "hello"
  def my_special_function():
    print("hello")

  # Delete my_special_function
  del my_special_function

  new_func()


def closures_keep_your_values_safe_2():
  def my_special_function():
    print('You are running my_special_function()')

  def get_new_func(func):
    def call_func():
      func()

    return call_func

  # Overwrite `my_special_function` with the new function
  my_special_function = get_new_func(my_special_function)

  my_special_function()


"""
Well done! Your niece feels like she understands closures now. She has seen that you can modify, delete, or overwrite the values 
needed by the nested function, but the nested function can still access those values because they are stored safely in the function's 
closure. She even realized that you could run into memory issues if you wound up adding a very large array or object to the closure, 
and has resolved to keep her eye out for that sort of problem.
"""


def main():
  # building_a_command_line_app()
  # reviewing_your_coworkers_code()
  # returning_functions_for_a_math_game()
  # modifying_variables_outside_local_scope()
  # modifying_variables_outside_local_scope_2()
  # modifying_variables_outside_local_scope_3()
  # checking_for_closure()
  closures_keep_your_values_safe_2()


if __name__ == '__main__':
  main()
