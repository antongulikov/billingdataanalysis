__author__ = 'scorpion'


class TimeOracle:

    def __init__(self):
        self._h, self._m, self._s = 0, 0, 0

    def get_full_time(self, cur: str):
        self._h, self._m, self._s = list(map(int, cur.split(".")))
        return self._h * 60 * 60 + self._m * 60 + self._m


