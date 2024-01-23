"""
Shows how to read data from an HTML file using Beautiful Soup (a.k.a. bs4).
"""

from bs4 import BeautifulSoup


def main():
    """
    A simple method to scrape data from an HTML file using the Beautiful Soup module.
    """

    f = open("data/nonsense_literature.html", "r")  # open the file in read mode

    contents = f.read()  # returns the entire contents of the file as a string

    soup = BeautifulSoup(contents, "lxml")  # use Beautiful Soup to parse the html

    # find all h1 tags and iterate through them
    for tag in soup.find_all("h2"):
        # print out the contents of each h2 tag in the HTML documenbt
        print(tag.text)


# ------------------------------------------------------------ #
# If this file is being run directly, call the main method ... #
if __name__ == "__main__":
    main()
