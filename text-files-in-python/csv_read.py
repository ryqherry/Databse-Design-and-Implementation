"""
Shows how to read a CSV data file using the csv module.
"""

import csv


def main():
    """
    A simple method to read a CSV data file using the csv module's DictReader.
    """
    # open the file in read mode
    f = open("data/nonsense_literature.csv", "r")

    csv_reader = csv.DictReader(f)
    for line in csv_reader:
        print(line["Title"])


# ------------------------------------------------------------ #
# If this file is being run directly, call the main method ... #
if __name__ == "__main__":
    main()
