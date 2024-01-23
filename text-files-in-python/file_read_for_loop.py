"""
Shows how to use a for loop to iterate directly through a file object.
"""


def main():
    """
    A simple method to open a file and iterate through its lines.
    """
    f = open("./data/nonsense_literature.csv", "r")  # open the file in read mode

    print("\nIterating through the file object using a for loop...\n")
    for line in f:
        print(line.strip())


# ------------------------------------------------------------ #
# If this file is being run directly, call the main method ... #
if __name__ == "__main__":
    main()
