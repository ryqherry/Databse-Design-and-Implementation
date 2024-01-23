"""
Shows how to use the file object's read() method.
"""


def main():
    """
    A simple method to open a file and print out the entire contents therein.
    """
    f = open("./data/nonsense_literature.csv", "r")  # open the file in read mode

    print("\nGetting all text at once as a String using f.read()...\n")
    full_text = f.read()  # read the entire file as a single String
    print(full_text)  # prints out the entire contents of the file, plus a line break

    # if you wanted to go line-by-line through the file, consider a different method
    print("\nGetting text line-by-line by splitting lines and looping...\n")
    lines = full_text.split("\n")  # split into a list
    for line in lines:
        print(line.strip())  # remove the line break from the lines


# ------------------------------------------------------------ #
# If this file is being run directly, call the main method ... #
if __name__ == "__main__":
    main()
