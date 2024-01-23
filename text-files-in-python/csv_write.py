"""
Shows how to write to a CSV data file using the csv module.
"""

import csv


def main():
    """
    A simple method to write to a CSV data file using the csv module's DictReader.
    """
    # open the file in read mode
    f = open("data/nonsense_literature.csv", "w")

    columns = ["Last name", "First name", "Title", "Year"]  # list of column names

    # a list of dictionaries, containing our data
    works = [
        {
            "Last name": "Carroll",
            "First name": "Lewis",
            "Title": "Jabberwocky",
            "Year": 1871,
        },
        {
            "Last name": "Lear",
            "First name": "Edward",
            "Title": "The Jumblies",
            "Year": 1910,
        },
        {
            "Last name": "Bishop",
            "First name": "Elizabeth",
            "Title": "The Man-Moth",
            "Year": 1946,
        },
    ]

    # use csv module's DictWriter to write each work in the list
    dict_writer = csv.DictWriter(f, fieldnames=columns)
    dict_writer.writeheader()  # write the column headers
    # iterate through each work and write it
    for work in works:
        dict_writer.writerow(work)

    # when done, close the file
    f.close()


# ------------------------------------------------------------ #
# If this file is being run directly, call the main method ... #
if __name__ == "__main__":
    main()
