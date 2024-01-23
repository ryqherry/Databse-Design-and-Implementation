"""
Shows how to write to a file using the file object's write() method.
"""


def main():
    """
    A simple method to open a file and write a few lines to it.
    """
    f = open("./data/jabberwocky.txt", "w")  # open the file in write mode

    print("\nWriting new lines to the file...\n")

    f.write("Jabberwocky, by Lewis Carroll\n\n")
    f.write("'Twas brillig, and the slithy toves\n")
    f.write("Did gyre and gimble in the wabe:\n")
    f.write("All mimsy were the borogoves,\n")
    f.write("And the mome raths outgrabe.\n")

    # when done, always close the file
    f.close()


# ------------------------------------------------------------ #
# If this file is being run directly, call the main method ... #
if __name__ == "__main__":
    main()
