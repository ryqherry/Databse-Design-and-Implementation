"""
Shows how to use the file object's readline() method.
"""


def main():
    """
    A simple method to open a file and retrieve one line at a time.
    """
    f = open("./data/nonsense_literature.csv", "r")  # open the file in read mode

    print("\nGetting each line as a String using f.readline()...\n")
    line = f.readline().strip()  # read the next available line, including line break
    print(line)  # prints out the contents of one line of the file, plus a line break

    line = f.readline().strip()  # read the next available line, including line break
    print(line)  # prints out the contents of one line of the file, plus a line break

    line = f.readline().strip()  # read the next available line, including line break
    print(line)  # prints out the contents of one line of the file, plus a line break

    line = f.readline().strip()  # read the next available line, including line break
    print(line)  # prints out the contents of one line of the file, plus a line break

    line = f.readline().strip()  # read the next available line, including line break
    print(line)  # prints out the contents of one line of the file, plus a line break


# ------------------------------------------------------------ #
# If this file is being run directly, call the main method ... #
if __name__ == "__main__":
    main()
