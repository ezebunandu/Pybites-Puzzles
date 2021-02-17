from collections import namedtuple
from datetime import datetime

Transaction = namedtuple("Transaction", "giver points date")
# https://twitter.com/raymondh/status/953173419486359552
Transaction.__new__.__defaults__ = (datetime.now(),)


class User:
    def __init__(self, name):
        self.name = name
        self._transactions = []

    def __add__(self, transaction: Transaction):
        self._transactions.append(transaction)

    @property
    def karma(self):
        return sum(transaction.points for transaction in self._transactions)

    @property
    def fans(self):
        return len({transaction.giver for transaction in self._transactions})

    @property
    def points(self):
        return [transaction.points for transaction in self._transactions]

    def __str__(self):
        end = "fans" if self.fans > 1 else "fan"
        return f"{self.name} has a karma of {self.karma} and {self.fans} " + end
