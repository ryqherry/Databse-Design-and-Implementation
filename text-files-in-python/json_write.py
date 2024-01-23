"""
Shows how to write to a JSON data file using the json module's dumps() function.
"""

import json


def main():
    """
    A simple method to write to a JSON data file using the json module's dumps() function
    """

    # a list of dictionaries, containing our data
    works = [
        {
            "lastName": "Carroll",
            "firstName": "Lewis",
            "title": "Jabberwocky",
            "year": 1871,
        },
        {
            "lastName": "Lear",
            "firstName": "Edward",
            "title": "The Jumblies",
            "year": 1910,
        },
        {
            "lastName": "Bishop",
            "firstName": "Elizabeth",
            "title": "The Man-Moth",
            "year": 1946,
        },
    ]

    # create proper JSON data from this list of dictionaries, indent it nicely
    json_data = json.dumps(works, indent=4)

    # write that JSON data to the file
    f = open("data/nonsense_literature.json", "w")
    f.write(json_data)

    # when done, always close the file
    f.close()


# ------------------------------------------------------------ #
# If this file is being run directly, call the main method ... #
if __name__ == "__main__":
    main()
