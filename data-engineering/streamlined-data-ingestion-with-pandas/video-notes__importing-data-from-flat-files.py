"""
Introduction To Flat Files:

DataFrame - pandas specific structure for two-dimensional data in columns and rows (index by default)

Flat Files:
+ Simple and easy to produce format
+ Data is stored as plain text with no formating
+ One row per line
+ Values for different fields are separated by a delimiter
+ Most common flat file type: comma-separated values
+ One pandas function to load them all: read_csv()

Loading other flat files:
+ Specify a different delimiter with sep (tax_data = pd.read_csv("us_taxes.tsv", sep="\t")

Customer loading tax data into a dataframe:
"""

import pandas as pd

tax_data = pd.read_csv("data/vt_tax_data_2016.csv")
print(tax_data.head(4))
print(tax_data.describe())

"""
Modifying Flat File Imports:
We'll look at ways to limit the amount of data imported and how to make that data easier to work with by naming columns.

Limiting columns:
+ Choose columns to load with the usecols keyword argument.
+ Accepts a list of column numbers or names, or a function to filter column names.

Customer:
"""

col_names = ['STATEFIPS', 'STATE', 'zipcode', 'agi_stub', 'N1']
col_nums = [0, 1, 2, 3, 4]

# Choose columns to load by name
tax_data_v1 = pd.read_csv("data/vt_tax_data_2016.csv", usecols=col_names)

# Choose columns to load by number
tax_data_v2 = pd.read_csv("data/vt_tax_data_2016.csv", usecols=col_nums)

print(tax_data_v1.equals(tax_data_v2))

"""
Another option is to limit the number of rows loaded with the nrows keyword argument
"""
tax_data_first_1000 = pd.read_csv("data/vt_tax_data_2016.csv", nrows=1000)
print(tax_data_first_1000.shape)

"""
+ Use nrows and skiprows together to process a file in chunks
+ skiprows accepts a list of row numbers, a number of rows, or a function to filter rows
+ Set header=None so pandas knows there are no column names
"""
tax_data_next_500 = pd.read_csv('data/vt_tax_data_2016.csv',
                                nrows=500,
                                skiprows=1000,
                                header=None)
print(tax_data_next_500.head(1))

"""
Assigning Column Names:
+ Supply columns names by passing a list to the names argument
+ The list MUST have a name for every column in your data
+ If you only need to rename a few columns, do it after import!
"""
col_names = list(tax_data_first_1000)
tax_data_next_500 = pd.read_csv('data/vt_tax_data_2016.csv',
                                nrows=500,
                                skiprows=1000,
                                header=None,
                                names=col_names)
print(tax_data_next_500.head(1))

"""
Handling Errors And Missing Data:

Common Flat File Import Issues:
+ Column data types are wrong
+ Values are missing
+ Records that cannot be read by pandas

Specifying Data Types:
"""
print(tax_data.dtypes)

"""
Pandas automatically inferrs column data types.
Use the dtype keyword argument to specify column data types.
dtype takes a dictionary of column names and data types.
"""
tax_data = pd.read_csv("data/vt_tax_data_2016.csv", dtype={"zipcode": str})
print(tax_data.dtypes)

"""
Customizing Missing Data Values:
Pandas automatically interprets some values as missing or NA (Zipcode column has 0 for no zip entered)

To customize:
+ Use the na_values keyword argument to set custom missing values
+ Can pass a single value, list, or dictionary of columns and values
"""
tax_data = pd.read_csv("data/vt_tax_data_2016.csv", na_values={"zipcode": 0})
print(tax_data.head(10))
print(tax_data[tax_data.zipcode.isna()])

"""
Lines with Errors:
If you try to import a corrupted csv, it could come back with errors. You could however:
+ Set error_bad_lines=False to skip unparseable records
+ Set warn_bad_lines=True to see messages when records are skipped
"""
tax_data = pd.read_csv("data/vt_tax_data_2016.csv",
                       error_bad_lines=False,
                       warn_bad_lines=True)
