import numpy as np
import pandas as pd


"""
Intro To pandas DataFrame Iteration:
 + Best practice for iterating over a pandas DataFrame

Baseball stats:
"""
baseball = pd.read_csv('baseball_stats.csv')


def baseball_stats():
    print(baseball.head())


def calc_win_perc(wins, games_played):
    win_perc = wins / games_played
    return np.round(win_perc, 2)


def adding_win_percentage_to_dataframe_with_iloc():
    # Inefficient
    baseball_df = baseball.copy()
    win_perc_list = []
    for i in range(len(baseball_df)):
        row = baseball_df.iloc[i]
        wins = row['W']
        games_played = row['G']
        win_perc = calc_win_perc(wins, games_played)
        win_perc_list.append(win_perc)
    baseball_df['WP'] = win_perc_list
    print(baseball_df.head(10))


def adding_win_percentage_to_dataframe_with_iterrows():
    baseball_df = baseball.copy()
    win_perc_list = []
    for i, row in baseball_df.iterrows():
        wins = row['W']
        games_played = row['G']
        win_perc = calc_win_perc(wins, games_played)
        win_perc_list.append(win_perc)
    baseball_df['WP'] = win_perc_list
    print(baseball_df.head(10))


"""
Another Iterator Method: .itertuples():

new = old[['A', 'B', 'C']].copy()
Team wins data
"""
team_wins_df = baseball[['Team', 'Year', 'W']]


def another_iterator_method_itertuples():
    # Inefficient with iterrows
    for row_tuple in team_wins_df.iterrows():
        # print(row_tuple)
        # print(type(row_tuple[1]))
        print(f"Index: {row_tuple[0]} Team: {row_tuple[1]['Team']} Year: {row_tuple[1]['Year']} Wins: {row_tuple[1]['W']}")

    # Instead with itertuples (WAY WAY FASTER)
    for row_namedtuple in team_wins_df.itertuples():
        # print(row_namedtuple)
        print(f"Index: {row_namedtuple.Index} Team: {row_namedtuple.Team} Year: {row_namedtuple.Year} Wins: {row_namedtuple.W}")


def calc_run_diff(runs_scored, runs_allowed):
    rs = int(runs_scored)
    ra = int(runs_allowed)
    diff = rs - ra
    return diff


def run_differentials_with_a_loop():
    baseball_df = baseball.copy()
    run_diffs_iterrows = []
    for i, row in baseball_df.iterrows():
        run_diff = calc_run_diff(row['RS'], row['RA'])
        run_diffs_iterrows.append(run_diff)
    baseball_df['RD'] = run_diffs_iterrows
    print(baseball_df)


"""
pandas .apply() method
 + Takes a function and applies it to a DataFrame
    + Must specify an axis to apply (0 for columns; 1 for rows)
 + Can be used with anonymous lambda functions
 + Examples:
    baseball_df.apply(lambda row: calc_run_diff(row['RS'], row['RA']), axis=1)
"""


def run_differentials_with_apply():
    baseball_df = baseball.copy()
    run_diffs_apply = baseball_df.apply(lambda row: calc_run_diff(row['RS'], row['RA']), axis=1)
    baseball_df['RD'] = run_diffs_apply
    print(baseball_df)


"""
Optimal pandas Iterating:

Since pandas is built on NumPy, eliminating loops applies to pandas too.

Power of vectorization:
  + Broadcasting (vectorizing) is extremely efficient!
  + baseball_df['RS'].values - baseball_df['RA'].values
"""


def optimal_pandas_iterating():
    baseball_df = baseball.copy()
    print(baseball_df)
    wins_np = baseball_df['W'].values
    print(type(wins_np))
    print(wins_np)
    run_diffs_np = baseball_df['RS'].values - baseball_df['RA'].values
    baseball_df['RD'] = run_diffs_np
    print(baseball_df)


def main():
    # baseball_stats()
    # adding_win_percentage_to_dataframe_with_iloc()
    # adding_win_percentage_to_dataframe_with_iterrows()
    # another_iterator_method_itertuples()
    # run_differentials_with_a_loop()
    # run_differentials_with_apply()
    optimal_pandas_iterating()


if __name__ == '__main__':
    main()
