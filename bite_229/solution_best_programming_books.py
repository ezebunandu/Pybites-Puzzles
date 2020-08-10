from dataclasses import dataclass
from functools import total_ordering
from operator import attrgetter
from pathlib import Path
from typing import Any, List, Optional
from urllib.request import urlretrieve

from bs4 import BeautifulSoup  # type: ignore

url: str = ("https://bites-data.s3.us-east-2.amazonaws.com/"
            "best-programming-books.html")
tmp: Path = Path("/tmp")
html_file: Path = tmp / "books.html"

if not html_file.exists():
    urlretrieve(url, html_file)


@total_ordering
@dataclass
class Book:
    title: str
    author: str
    year: int
    rank: int
    rating: float

    def __lt__(self, other) -> bool:
        last = self.author.split(", ")[0]
        other_last = other.author.split(", ")[0]
        title = self.title.title()
        other_title = other.title.title()
        if self.rating < other.rating:
            return True
        elif self.rating == other.rating and self.year < other.year:
            return True
        elif (
            self.rating == other.rating
            and self.year == other.year
            and title < other_title
        ):
            return True
        elif (
            self.rating == other.rating
            and self.year == other.year
            and title == other_title
            and last < other_last
        ):
            return True
        else:
            return False

    def __gt__(self, other) -> bool:
        last = self.author.split(", ")[0]
        other_last = other.author.split(", ")[0]
        title = self.title.title()
        other_title = other.title.title()
        if self.rating > other.rating:
            return True
        elif self.rating == other.rating and self.year > other.year:
            return True
        elif (
            self.rating == other.rating
            and self.year == other.year
            and title > other_title
        ):
            return True
        elif (
            self.rating == other.rating
            and self.year == other.year
            and title == other_title
            and last > other_last
        ):
            return True
        else:
            return False

    def __str__(self) -> str:
        desc = f"[{str(self.rank).zfill(3)}] {self.title} ({self.year})\n"
        desc += f"      {self.author} {float(self.rating)}"
        return desc


def _clean_data(soup: Any, replace: str = "", as_type: Any = str) -> Any:
    return as_type(soup.replace(replace, ""))


def _format_authors(authors: Any) -> str:
    names = []
    if "," in authors:
        authors = authors.split(", ")
        for name in authors:
            first, last = name.rsplit(maxsplit=1)
            names.append(f"{last}, {first}")
    else:
        first, last = authors.rsplit(maxsplit=1)
        names.append(f"{last}, {first}")
    return ", ".join(names)


def _get_soup(file: Path) -> Any:
    return BeautifulSoup(file.read_text(), "html.parser")


def _process_soup(soup: Any) -> Optional[Book]:
    try:
        title_soup = soup.find("h2", {"class": "main"}).text
        author_soup = soup.find("h3", {"class": "authors"}).text
        year_soup = soup.find("span", {"class", "date"}).text
        rank_soup = soup.find("div", {"class": "rank"}).text
        rating_soup = soup.find("span", {"class", "our-rating"}).text

        title: str = _clean_data(title_soup)
        authors: str = _clean_data(author_soup, " (You?)")
        author: str = _format_authors(authors)
        year: int = _clean_data(year_soup, " | ", int)
        rank: int = _clean_data(rank_soup, as_type=int)
        rating: float = _clean_data(rating_soup, as_type=float)

        return Book(title, author, year, rank, rating)
    except AttributeError:
        return None


def _sort_books(python_books: Any) -> List[Book]:
    books = [book for book in python_books if book is not None]
    sorted_books = sorted(books)
    rated = sorted(sorted_books, key=attrgetter("rating"), reverse=True)

    for i, book in enumerate(rated, 1):
        book.rank = i

    return rated


def display_books(books: List[Book], limit: int = 10,
                  year: Optional[int] = None):
    if year:
        books = [book for book in books if book.year >= year]
    for book in books[:limit]:
        print(book)


def load_data() -> List[Book]:
    soup = _get_soup(html_file)
    all_books = soup.find_all("div", {"class": "book accepted normal"})
    selected_books = [
        book
        for book in all_books
        if "python" in book["data-title"].split(": ")[0].lower()
    ]
    python_books = [_process_soup(book) for book in selected_books]

    return _sort_books(python_books)


def main():
    books = load_data()
    display_books(books, limit=5, year=2017)
    """If done correctly, the previous function call should display the
    output below.
    """


if __name__ == "__main__":
    main()

"""
[001] Python Tricks (2017)
      Bader, Dan 4.74
[002] Mastering Deep Learning Fundamentals with Python (2019)
      Wilson, Richard 4.7
[006] Python Programming (2019)
      Fedden, Antony Mc 4.68
[007] Python Programming (2019)
      Mining, Joseph 4.68
[009] A Smarter Way to Learn Python (2017)
      Myers, Mark 4.66
"""