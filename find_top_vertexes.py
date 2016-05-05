__author__ = 'scorpion'

import sys
from sort_by_day import Reader
from collections import defaultdict


def get_out_file(file_name: str):
    ret = file_name
    ret = ret.split("/")
    ret[-1] = "vertex.data"
    return "/".join(ret)


def print_top_vertex(d_reader: Reader, c_reader:Reader, out_file):
    cordinate_list = defaultdict(list)
    posis = {}
    while True:
        line = d_reader.get_line()
        if line is None:
            break
        id, tim, lat, lon = list(map(float, line[0].split(" " )))
        id = int(id)
        posis[id] = (lat, lon)
        cordinate_list[(lat, lon)].append((id, tim))
    result = []
    c_reader.get_line()
    c_reader.get_line()
    while True:
        line = c_reader.get_line()
        if line is None:
            break
        lat, lon, _ = list(map(float, line[0].split(" ")))
        result.extend(cordinate_list.get((lat, lon), []))
    ret = ""
    for value in result:
        ret += " ".join(list(map(str, [value[0], value[1], posis[value[0]][0], posis[value[0]][1]]))) + "\n"
    with open(out_file, "w") as file:
        file.write(ret)


def main():
    coordinate_file = sys.argv[1]
    desc_file = sys.argv[2]
    out_file = get_out_file(coordinate_file)
    desc_reader = Reader(desc_file)
    coord_reader = Reader(coordinate_file)
    print_top_vertex(desc_reader, coord_reader, out_file)


if __name__ == "__main__":
    main()
