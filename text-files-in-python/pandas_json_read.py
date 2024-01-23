"""
Shows how to read data from a JSON file using pandas.
"""

import pandas as pd


def main():
    """
    A simple method to read a JSON data file using pandas' read_json() method.
    """

    df = pd.read_json("data/nonsense_literature.json")

    print(df["title"])  # output all titles

    # that's it!


# ------------------------------------------------------------ #
# If this file is being run directly, call the main method ... #
if __name__ == "__main__":
    main()
