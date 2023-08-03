from statistics import mean, median


class IntList(list):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def mean(self):
        return mean(self)

    @property
    def median(self):
        return median(self)

    def _check_int(self, num):
        try:
            return [int(i) for i in num] if isinstance(num, list) else int(num)
        except (ValueError, TypeError) as e:
            raise TypeError from e

    def append(self, num):
        num = self._check_int(num)
        super().append(num)

    def __add__(self, num):
        num = self._check_int(num)
        return super().__add__(num)

    def __iadd__(self, num):
        num = self._check_int(num)
        return super().__iadd__(num)
