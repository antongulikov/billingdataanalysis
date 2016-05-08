__author__ = 'scorpion'

import math


class GenColor:
    def __init__(self, values):
        self._ma = max(values)
        self._mi = min(values)

    def _color(self, y):
        values = [str(x) for x in range(10)]
        for x in "ABCDEF":
            values.append(x)
        return values[y // 16] + values[y % 16]

    def get_color(self, x):
        x = (x - self._mi) / (self._ma - self._mi)
        x *= 255
        x = int(x)
        if x < 0:
            x = 0
        if x > 255:
            x = 255
        return self._color(x) * 2 + "00"


def main():
    pass

if __name__ == "__main__":
    main()
