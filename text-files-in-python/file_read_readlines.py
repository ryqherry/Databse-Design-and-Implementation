"""
Shows how to use the file object's readlines() method.
"""


def main():
    """
    A simple method to open a file and print out the entire contents therein.
    """
    f = open("./data/nonsense_literature.csv", "r")  # open the file in read mode

    print("\nGetting all text at once as a list using f.readlines()...\n")
    lines = f.readlines()  # returns text as a list

    # iterate through each line in the list
    for line in lines:
        print(line.strip())


# ------------------------------------------------------------ #
# If this file is being run directly, call the main method ... #
if __name__ == "__main__":
    main()
