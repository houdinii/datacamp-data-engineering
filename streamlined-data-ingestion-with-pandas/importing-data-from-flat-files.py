import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def get_data_from_csvs():
    """
    Get data from CSVs
    In this exercise, you'll create a data frame from a CSV file. The United States makes available CSV files containing tax data by
    ZIP or postal code, allowing us to analyze income information in different parts of the country. We'll focus on a subset of the
    data, vt_tax_data_2016.csv, which has select tax statistics by ZIP code in Vermont in 2016.

    To load the data, you'll need to import the pandas library, then read vt_tax_data_2016.csv and assign the resulting data frame to
    a variable. Then we'll have a look at the data.

    Instructions:
    + Import the pandas library as pd.
    + Use read_csv() to load vt_tax_data_2016.csv and assign it to the variable data.
    + View the first few lines of the data frame with the head() method. This code has been written for you.
    """

    # Read the CSV and assign it to the variable data
    data = pd.read_csv("data/vt_tax_data_2016.csv")

    # View the first few lines of data
    print(data.head())


def get_data_from_other_flat_files():
    # Load TSV using the sep keyword argument to set delimiter
    data = pd.read_csv("data/vt_tax_data_2016.csv", sep=',')

    # Plot the total number of tax returns by income group
    counts = data.groupby("agi_stub").N1.sum()
    counts.plot.bar()
    plt.show()


def main():
    sns.set()
    get_data_from_csvs()
    get_data_from_other_flat_files()


if __name__ == '__main__':
    main()
