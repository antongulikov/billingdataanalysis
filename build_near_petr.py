__author__ = 'scorpion'

import sys
import math
from sort_by_day import Reader

HEADER = "./new_data/positions/"
files = ["03.10.2015.csv", "21.11.2015.csv", "24.11.2015.csv",
         "20.10.2015.csv", "24.10.2015.csv", "31.10.2015.csv"]


class GraphBuilderNear:

    petr_coordinates = (59.95271, 30.28725)
    treshold = 1e-3

    def __init__(self, graph_name: str, frequency=1):
        self._file = open(graph_name + ".graph", "w")
        self._desc = open(graph_name + ".desc", "w")
        self._frequency = frequency
        self._vertex = {}
        self._nv = 0
        self._flag = frequency != 24 * 60 * 60

    def _is_near(self, coordinate):
        dist = (coordinate[0] - GraphBuilderNear.petr_coordinates[0]) ** 2 + \
               (coordinate[1] - GraphBuilderNear.petr_coordinates[1]) ** 2
        return dist < GraphBuilderNear.treshold

    def _build_graph(self):
        for file in files:
            file_name = HEADER + file
            reader = Reader(file_name)
            self._add_edges(reader)

    def _get_vertex_number(self, time, lat, lon):
        key = (time, lat, lon)
        if self._vertex.get(key, None) is None:
            self._nv += 1
            self._vertex[key] = self._nv
            self._desc.write(" ".join(list(map(str, [self._nv, time, lat, lon]))) + "\n")
        return self._vertex[key]

    def _add_edges(self, reader: Reader):
        reader.seek_line()
        previous = None
        while True:
            line = reader.get_line()
            if line is None:
                break
            time, lat, lon = list(map(float, line))
            time = int(time)
            time //= self._frequency
            current = (time, lat, lon)
            if not self._is_near((lat, lon)):
                continue
            current_number = self._get_vertex_number(time, lat, lon)
            if previous is None:
                previous = (time, lat, lon)
                continue
            if time <= previous[0] and self._flag:
                previous = (time, lat, lon)
                continue
            if previous == current:
                continue
            previous_number = self._get_vertex_number(*previous)
            previous = current #!!!!! fuck the police
            self._file.write(str(previous_number) + " " + str(current_number) + "\n")

    def __del__(self):
        self._file.close()
        self._desc.close()


def main():
    file_name = sys.argv[1]
    frequency = int(sys.argv[2]) * 60
    print(file_name, frequency)
    gb = GraphBuilderNear(file_name, frequency)
    gb._build_graph()

if __name__ == "__main__":
    main()
