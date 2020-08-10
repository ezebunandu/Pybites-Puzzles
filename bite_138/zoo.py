import itertools


class Animal:
    _seq = itertools.count(10001)
    _zoo = []

    def __init__(self, name):
        self.id = next(self._seq)
        self.name = name.title()
        self._zoo.append(self)

    def __str__(self):
        return f"{self.id}. {self.name}"

    @classmethod
    def zoo(cls):
        return "\n".join([str(animal) for animal in cls._zoo])
