from pathlib import Path
from urllib.request import urlretrieve

from bs4 import BeautifulSoup

url = ("https://bites-data.s3.us-east-2.amazonaws.com/"
       "best-programming-books.html")
tmp = Path("/tmp")
html_file = tmp / "books.html"

if not html_file.exists():
    urlretrieve(url, html_file)


class Book:
    """Book class should instatiate the following variables:

    title - as it appears on the page
    author - should be entered as lastname, firstname
    year - four digit integer year that the book was published
    rank - integer rank to be updated once the books have been sorted
    rating - float as indicated on the page
    """
    def __init__(self, title: str, author:str, year:int, rank:int, rating:float) -> None:
        self.title = title
        self.author = author
        self.year = year
        self.rank = rank
        self.rating = float(rating)

    def __str__(self):
        return f"[{self.rank:03}] {self.title} ({self.year})\n      {self.author} {self.rating}"
        
    def __repr__(self):
        return f"{self.__class__.__name__} {self.__dict__}"


def _get_soup(file):
    return BeautifulSoup(file.read_text(), "html.parser")


def display_books(books, limit=10, year=None):
    """Prints the specified books to the console

    :param books: list of all the books
    :param limit: integer that indicates how many books to return
    :param year: integer indicating the oldest year to include
    :return: None
    """

    if year:
        required_books = [book for book in books if book.year >= year]
    else:
        required_books = books

    for book in required_books[:limit]:
        print(book)


def load_data():
    """Loads the data from the html file

    Creates the soup object and processes it to extract the information
    required to create the Book class objects and returns a sorted list
    of Book objects.

    Books should be sorted by rating, year, title, and then by author's
    last name. After the books have been sorted, the rank of each book
    should be updated to indicate this new sorting order.The Book object
    with the highest rating should be first and go down from there.
    """
    all_books = []
    soup = _get_soup(html_file)
    books = soup.find_all(class_="book accepted normal")
    python_books = [book for book in books if 'python' in book.find('h2').get_text().lower()]
    
    for book in python_books:
        title = book.find('h2').get_text()
        author_name = book.find(class_="subtitle").h3.a.get_text()

        if len(author_name.split()) == 3:
            first_name, initial, last_name = author_name.split()
            author = f"{last_name}, {first_name} {initial}"
        elif len(author_name.split()) == 2:
            first_name, last_name = author_name.split()
            author = f"{last_name}, {first_name}"
        year = book.find("span", {'class': 'date'}).get_text()[-4:] if book.find("span", {'class': 'date'}) else None
        rating = book.find(class_="subtitle").find(class_="our-rating").text
        
        if all((title, author, year, rating)):
            all_books.append(Book(title=title, author=author, year=int(year), rank=None, rating=float(rating)))
            
         
    all_books = sorted(all_books, key=lambda book: (book.year, book.title.lower(), book.author.split(' ')[0].strip(',').lower()))
    all_books = sorted(all_books, key=lambda book: book.rating, reverse=True)
    
    for i, book in enumerate(all_books, start=1):
        book.rank=i
        
    return all_books


def main():
    books = load_data()
    display_books(books, limit=5, year=2017)
    """If done correctly, the previous function call should display the
    output below.
    """


if __name__ == "__main__":
    main()