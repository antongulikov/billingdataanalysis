__author__ = 'scorpion'

from sort_by_day import Reader
import sys
from collections import defaultdict


def main():
    in_file_name = sys.argv[1]
    out_file = sys.argv[2]
    reader = Reader(in_file_name)
    points = defaultdict(int)
    while True:
        line = reader.get_line()
        if line is None:
            break
        _, __, x, y = list(map(float, line[0].split(" ")))
        if (x, y) in points:
            continue
        points[(x, y)] = len(points) + 1
    point_s = sorted([(key, value) for key, value in points.items()], key=lambda x: x[1])
    with open(out_file, "w") as file:
        for key, value in point_s:
            file.write(" ".join(list(map(str,[key[0], key[1], value]))) + "\n")

if __name__ == "__main__":
    main()
