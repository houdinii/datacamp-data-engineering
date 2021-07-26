# Add a docstring to count_letter()
import pandas as pd
import numpy as np


def count_letter(content, letter):
  """Count the number of times `letter` appears in `content`.

  # Add a Google style arguments section
  Args:
    content (str): The string to search.
    letter (str): The letter to search for.

  # Add a returns section
  Returns:
    int

  # Add a section detailing what errors might be raised
  Raises:
    ValueError: If `letter` is not a one-character string.
  """
  if (not isinstance(letter, str)) or len(letter) != 1:
    raise ValueError('`letter` must be a single character string.')
  return len([char for char in content if char == letter])


def crafting_a_docstring():
  print(count_letter.__doc__)


def retrieving_docstrings():
  # Get the "count_letter" docstring by using an attribute of the function
  docstring = count_letter.__doc__

  border = '#' * 28
  print('{}\n{}\n{}'.format(border, docstring, border))

  # Using inspect
  import inspect

  # Inspect the count_letter() function to get its docstring
  docstring = inspect.getdoc(count_letter)

  border = '#' * 28
  print('{}\n{}\n{}'.format(border, docstring, border))


def build_tooltip(function):
  import inspect
  """Create a tooltip for any function that shows the
  function's docstring.

  Args:
    function (callable): The function we want a tooltip for.

  Returns:
    str
  """
  # Get the docstring for the "function" argument by using inspect
  docstring = inspect.getdoc(function)
  border = '#' * 28
  return '{}\n{}\n{}'.format(border, docstring, border)


def standardize(column):
  """Standardize the values in a column.

  Args:
    column (pandas Series): The data to standardize.

  Returns:
    pandas Series: the values as z-scores
  """
  # Finish the function so that it returns the z-scores
  z_score = (column - column.mean()) / column.std()
  return z_score


def extract_a_function():
  df = pd.DataFrame(np.array([[2.78587674, 2.05251262, 2.1705437, 0.06556992],
                              [1.14455734, 2.6664982, 0.26709777, 2.88473746],
                              [0.90740581, 0.42363394, 2.61345949, 0.03095006],
                              [2.20525908, 0.5235798, 3.98434531, 0.33928911],
                              [2.87787588, 1.28792243, 3.07758935, 0.90199364],
                              [1.69242584, 2.64625735, 2.29509645, 3.50049814],
                              [3.92305679, 3.3860249, 0.41054104, 1.45430527],
                              [2.73931895, 2.21302938, 2.7993363, 2.15983974],
                              [1.92372761, 3.41780995, 2.64467147, 2.27241286],
                              [1.56847007, 1.53935125, 0.19638852, 0.90185344],
                              [1.37271206, 1.26715159, 3.16919721, 2.28858707],
                              [2.91619883, 1.4170587, 2.07486636, 2.64380718],
                              [1.75428898, 0.68432732, 1.70347078, 1.19298157],
                              [0.23871159, 3.31645054, 3.15274869, 1.67450744],
                              [1.59217702, 1.35468338, 1.64627689, 1.8123557],
                              [2.95198162, 2.2094803, 1.9241051, 3.72940265],
                              [0.72996692, 2.31420587, 0.72651537, 2.34997499],
                              [0.70180702, 2.08613224, 1.2852756, 3.79300949],
                              [2.1262055, 0.01075226, 3.38213199, 2.22413902],
                              [2.12731035, 3.95338168, 0.747615, 2.00224568],
                              [2.53760383, 3.6213663, 1.66916424, 0.01412884],
                              [3.39772718, 0.83054344, 3.95613803, 1.92355618],
                              [2.8978213, 1.16995765, 0.94639925, 3.70981999],
                              [2.44409404, 2.08004061, 3.66732933, 0.79346276],
                              [2.88977353, 3.60764549, 3.67358987, 0.20836454],
                              [1.29183566, 3.93452354, 0.36518537, 1.62711557],
                              [1.44715462, 1.03016826, 1.8546109, 1.48958592],
                              [0.91305292, 2.25743617, 2.00886534, 3.42861223],
                              [1.17485619, 3.22787474, 1.2546758, 0.10644446],
                              [2.5239045, 1.57748022, 0.18935815, 3.68059692],
                              [0.36841976, 2.92429214, 0.96674255, 2.723612],
                              [1.73480469, 0.64427606, 0.38211857, 3.61690398],
                              [1.72345105, 2.40279427, 0.95299962, 2.43011628],
                              [1.97474039, 3.46345783, 3.23116435, 3.24781325],
                              [1.70332116, 3.93408644, 3.57991315, 1.34217549],
                              [1.24904489, 0.31746316, 0.17289157, 1.39826491],
                              [1.70540523, 1.7133891, 1.20778735, 1.55949692],
                              [3.57355665, 0.81817144, 3.92232879, 3.01918833],
                              [3.77664007, 1.80254596, 2.15801929, 1.4771647],
                              [2.0073467, 2.19105429, 2.50523745, 0.96887923],
                              [2.49581181, 0.37330684, 0.02218163, 3.75067343],
                              [0.46247358, 1.1874431, 1.93963777, 3.63204433],
                              [1.26914193, 3.71033696, 3.95331414, 1.39518926],
                              [1.65930485, 2.27601493, 1.50074211, 2.53855228],
                              [3.46523663, 1.82964799, 0.38815263, 1.09536885],
                              [1.00182146, 3.01410396, 1.84763505, 0.82446051],
                              [1.93213706, 2.96744861, 3.85201786, 1.34535812],
                              [3.94223914, 0.19431613, 1.36732245, 1.30839957],
                              [2.07794048, 2.83478958, 3.19569093, 3.5291044],
                              [2.4515781, 3.35697339, 3.19538532, 3.28921526],
                              [0.48251466, 0.66375154, 0.83299319, 2.83849291],
                              [3.3053632, 3.12399175, 1.77347081, 3.8373809],
                              [2.41224051, 1.14614647, 2.8624051, 1.69017341],
                              [2.18027203, 1.22587901, 1.64207914, 0.98013215],
                              [1.37105534, 2.66104586, 0.76402782, 0.46959375],
                              [1.21648316, 0.44556869, 3.86997723, 1.20421343],
                              [1.66808884, 2.6594898, 2.60300147, 0.58105494],
                              [2.72520306, 3.55142717, 3.46183941, 0.36874439],
                              [3.50182737, 2.78524507, 0.10096943, 2.41172879],
                              [2.04168935, 1.76131151, 1.06762326, 1.4567498],
                              [2.67725513, 1.75285754, 2.0082844, 2.25828137],
                              [2.34374621, 3.06038438, 0.26979454, 0.76534288],
                              [2.49961401, 2.262568, 3.97213304, 2.70762344],
                              [2.6987562, 0.33961665, 0.94584958, 0.86202179],
                              [3.36936975, 2.33068435, 1.49716873, 1.11209437],
                              [0.33277995, 3.25937481, 0.85604766, 2.96704169],
                              [3.05473137, 1.34826553, 0.42178346, 2.23895158],
                              [0.9746655, 3.71030632, 0.92991914, 1.33934565],
                              [0.77689184, 3.002868, 1.20244054, 2.17195513],
                              [2.28982783, 2.2962553, 2.53776907, 2.77593881],
                              [0.38285007, 3.00657596, 1.12493913, 3.64852849],
                              [3.54130731, 0.31659584, 1.44910704, 2.32285285],
                              [2.50899589, 3.4375563, 0.02377137, 0.93074552],
                              [2.89366543, 3.28601645, 1.4628765, 2.98679052],
                              [0.06451683, 3.63948664, 2.13554393, 3.11107607],
                              [2.37772752, 0.51452479, 0.64806335, 0.80160526],
                              [2.22714077, 0.32712035, 2.38973243, 3.28229688],
                              [0.63583858, 0.55366229, 1.17260987, 1.85973942],
                              [0.61228206, 1.59751484, 2.52820198, 3.11906665],
                              [2.78211812, 1.69722744, 0.10478642, 0.94991288],
                              [1.27506571, 2.24887351, 3.55037384, 1.33032108],
                              [2.76788118, 0.4889742, 0.06447452, 3.81478848],
                              [2.217533, 0.80559801, 0.50783212, 2.63126029],
                              [1.5558023, 3.24657739, 3.10864985, 3.09151132],
                              [3.70052996, 1.8719503, 0.18358093, 2.75349737],
                              [3.36667999, 3.23175284, 2.84399477, 0.81721647],
                              [1.42959027, 0.02970551, 3.88418456, 1.88275499],
                              [0.17436586, 2.2063709, 3.48673173, 3.23585549],
                              [1.21907229, 3.72772859, 2.84064661, 2.70014051],
                              [1.59274273, 2.32870184, 3.83403897, 0.02411154],
                              [2.81983532, 0.82438291, 1.71925335, 0.34963097],
                              [3.98143393, 2.87103025, 3.49151566, 1.38717888],
                              [1.42365946, 1.5159434, 1.42383067, 3.77746216],
                              [3.05019126, 2.67353579, 3.71905461, 1.96476192],
                              [2.37270767, 0.11727889, 0.59511062, 1.08070507],
                              [2.76680719, 2.54360144, 3.76011606, 1.44169488],
                              [0.60450981, 0.12879174, 3.33086479, 0.84261051],
                              [1.59550517, 2.97912262, 3.38421935, 1.68480023],
                              [0.96342359, 1.89165201, 0.49569204, 0.87214176],
                              [1.37382406, 0.48701742, 2.38594759, 3.38301003]]), columns=['y1_gpa', 'y2_gpa', 'y3_gpa', 'y4_gpa'])
  # Use the standardize() function to calculate the z-scores
  df['y1_z'] = standardize(df['y1_gpa'])
  df['y2_z'] = standardize(df['y2_gpa'])
  df['y3_z'] = standardize(df['y3_gpa'])
  df['y4_z'] = standardize(df['y4_gpa'])
  print(df.head(40))


def mean(values):
  """Get the mean of a sorted list of values

  Args:
    values (iterable of float): A list of numbers

  Returns:
    float
  """
  # Write the mean() function
  mean = sum(values) / len(values)
  return mean


def median(values):
  """Get the median of a sorted list of values

  Args:
    values (iterable of float): A list of numbers

  Returns:
    float
  """
  # Write the median() function
  midpoint = int(len(values) / 2)
  if len(values) % 2 == 0:
    median = (values[midpoint - 1] + values[midpoint]) / 2
  else:
    median = values[midpoint]
  return median


def split_up_a_function():
  values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  print(mean(values))
  print(median(values))


# Use an immutable variable for the default argument
def better_add_column(values, df=None):
  """Add a column of `values` to a DataFrame `df`.
  The column will be named "col_<n>" where "n" is
  the numerical index of the column.

  Args:
    values (iterable): The values of the new column
    df (DataFrame, optional): The DataFrame to update.
      If no DataFrame is passed, one is created by default.

  Returns:
    DataFrame
  """
  # Update the function to create a default DataFrame
  if df is None:
    df = pd.DataFrame()
  df['col_{}'.format(len(df.columns))] = values
  return df


def best_practice_for_default_arguments():
  print(better_add_column([1, 2, 3, 4, 5, 6, 7]))


def main():
  # crafting_a_docstring()
  # retrieving_docstrings()
  # print(build_tooltip(count_letter))
  # print(build_tooltip(range))
  # print(build_tooltip(print))
  # extract_a_function()
  # split_up_a_function()
  best_practice_for_default_arguments()


if __name__ == '__main__':
  main()
