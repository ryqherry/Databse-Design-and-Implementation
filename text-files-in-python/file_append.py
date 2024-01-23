"""
Shows how to append to a file using the file object's write() method.
"""


def main():
    """
    A simple method to open a file and append a few lines to it.
    """
    f = open("./data/jabberwocky.txt", "a")  # open the file in append mode

    print("\Appending new lines to the file...\n")

    f.write('"Beware the Jabberwock, my son!\n')
    f.write("The jaws that bite, the claws that catch!\n")
    f.write("Beware the Jubjub bird, and shun\n")
    f.write('The frumious Bandersnatch!"\n')
    f.write(
        "\nRead the entire poem: https://www.poetryfoundation.org/poems/42916/jabberwocky\n"
    )

    # when done, always close the file
    f.close()


# ------------------------------------------------------------ #
# If this file is being run directly, call the main method ... #
if __name__ == "__main__":
    main()
