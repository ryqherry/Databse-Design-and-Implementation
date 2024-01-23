"""
Shows how to read data from a CSV file using pandas.
"""

import pandas as pd


def main():
    """
    A simple method to read a CSV data file using pandas' read_csv() method.
    """
    df = pd.read_csv("data/nonsense_literature.csv")

    print(df["Title"])  # output all titles

    # that's it!


# ------------------------------------------------------------ #
# If this file is being run directly, call the main method ... #
if __name__ == "__main__":
    main()
