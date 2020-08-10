from datetime import datetime, timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    for i in range(1, 1_000_000):
        yield from (PYBITES_BORN + timedelta(days=100 * i))
        yield from (PYBITES_BORN + timedelta(days=365 * i))
