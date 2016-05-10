__author__ = 'scorpion'

from sort_by_day import Reader
import math
import sys


class Graph:
    def __init__(self, edge_reader: Reader, desc_reader: Reader):
        self._edge_list = self._read_edges(edge_reader)
        self._position = self._read_position(desc_reader)
        self._N = self._count_n()
        self._adjacency = self._badj()
        self._distance = self._buildd()

    def _read_edges(self, edge_reader: Reader):
        edges = []
        for line in edge_reader:
            u, _ = list(map(int, line[0].split(" ")))
            edges.append((u, u))
        return edges

    def _read_position(self, desc_reader: Reader):
        positions = {}
        for line in desc_reader:
            p, lan, lng = list(map(float, line[0].split(" ")))
            positions[int(p)] = (lan, lng)
        return positions

    def _count_n(self):
        N = 0
        for (u, v) in self._edge_list:
            N = max(N, u, v)
        return N

    def _badj(self):
        matrix = [[0 for _1 in range(self._N + 1)] for _2 in range(self._N + 1)]
        for (u, v) in self._edge_list:
            matrix[u][v] = 1
            matrix[v][u] = 1
        return matrix

    def _distance(self, c1, c2):
        return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

    def _buildd(self):
        matrix = [[0 for _1 in range(self._N + 1)] for _2 in range(self._N + 1)]
        for (u, v) in self._edge_list:
            for (u1, v1) in self._edge_list:
                matrix[u][u1] = self._distance(self._position[u], self._position[u1])
                matrix[u1][u] = matrix[u][u1]
                if matrix[u][u1] < 0.007:
                    self._adjacency[u][u1] = 1
                    self._adjacency[u1][u] = 1
        return matrix


def main():
    ed_f = sys.argv[1]
    de_f = sys.argv[2]
    ed_r, de_r = Reader(ed_f), Reader(de_f)
    graph = Graph(ed_r, de_r)
    for x in graph._distance:
        print(sum(x))

if __name__ == "__main__":
    main()



