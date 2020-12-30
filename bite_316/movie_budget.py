from datetime import date
from typing import Dict, Sequence, NamedTuple
from itertools import groupby


class MovieRented(NamedTuple):
    title: str
    price: int
    date: date


RentingHistory = Sequence[MovieRented]
STREAMING_COST_PER_MONTH = 12
STREAM, RENT = 'stream', 'rent'


def _accumulate(renting_history: RentingHistory):
    movies_grouped = groupby(renting_history, lambda x: (x.date.strftime("%Y-%m")))
    for date_, subiter in movies_grouped:
        yield date_, sum(item.price for item in subiter)

def _rent_or_stream(total_price, streaming_cost):
    if total_price > streaming_cost:
        return 'stream'
    else:
        return 'rent'


def rent_or_stream(
    renting_history: RentingHistory,
    streaming_cost_per_month: int = STREAMING_COST_PER_MONTH
) -> Dict[str, str]:
    """Function that calculates if renting movies one by one is
       cheaper than streaming movies by months.

       Determine this PER MONTH for the movies in renting_history.

       Return a dict of:
       keys = months (YYYY-MM)
       values = 'rent' or 'stream' based on what is cheaper

       Check out the tests for examples.
    """
    movies_grouped = list(_accumulate(renting_history))
    return {group[0]: _rent_or_stream(group[1], STREAMING_COST_PER_MONTH) for group in movies_grouped}



if __name__ == '__main__':
    x = [MovieRented('Spider-Man', 12, date(2020, 12, 28)),
     MovieRented('Sonic', 10, date(2020, 11, 4)),
     MovieRented('Die Hard', 3, date(2020, 11, 3))]
    print(rent_or_stream(x))