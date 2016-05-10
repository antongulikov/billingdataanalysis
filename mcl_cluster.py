__author__ = 'scorpion'

from graph import Graph
from sort_by_day import Reader
import sys


class Mcl:
    def __init__(self, g: Graph):
        self._edges = self._do_clustering(g._adjacency)
        self._n = len(g._adjacency)
        self._edge_list = self._build_edge_list(self._edges, self._n)
        self._redge_list = self._rlist(self._edges)
        self._used = [False for j in range(self._n)]
        self._order = []
        self._tmp_set = set()
        self._clusters = self._finish_clusters()

    def _rlist(self, edges):
        ret = []
        for (u, v) in edges:
            ret.append((v, u))
        return self._build_edge_list(ret, self._n)

    def _normalize(self, matrix):
        ret_matrix = [[x for x in y] for y in matrix]
        sum = [0. for y in matrix]
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                sum[j] += matrix[i][j]
        for i in range(n):
            for j in range(n):
                ret_matrix[i][j] = ret_matrix[i][j] / sum[j]
        return ret_matrix

    def _mult(self, a, b):
        n = len(a)
        ret = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    ret[i][j] += a[i][k] * b[k][j]
        return ret

    def _inflate(self, a, p):
        n = len(a)
        ret = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(n):
                ret[i][j] = (a[i][j] ** p)
        return ret

    def _do_clustering(self, matrix):
        n = len(matrix)
        for j in range(n):
            matrix[j][j] = 1
        matrix = self._normalize(matrix)
        for _iterate in range(10):
            print(_iterate)
            matrix = self._mult(matrix, matrix)
            matrix = self._inflate(matrix, 2)
            matrix = self._normalize(matrix)
            for x in matrix:
                print(x)
            print("---------")
        edges_ret = []
        for i in range(n):
            for j in range(n):
                if matrix[i][j] > 0.7:
                    edges_ret.append((i, j))
        print(len(edges_ret))
        return edges_ret

    def _build_edge_list(self, edges, n):
        ret = [[] for j in range(n)]
        for (u, v) in edges:
            ret[u].append(v)
        return ret

    def _dfs(self, v):
        self._used[v] = True
        for u in self._edge_list[v]:
            if not self._used[u]:
                self._dfs(u)
        self._order.append(v)

    def _dfs_reverse(self, v):
        self._used[v] = True
        self._tmp_set.add(v)
        for u in self._redge_list[v]:
            if not self._used[u]:
                self._dfs_reverse(u)

    def _finish_clusters(self):
        for i in range(self._n):
            if not self._used[i]:
                self._dfs(i)
        for j in range(self._n):
            self._used[j] = False

        clusters = []

        for x in reversed(self._order):
            if not self._used[x]:
                self._tmp_set = set()
                self._dfs_reverse(x)
                new_set = set()
                for x in self._tmp_set:
                    for u in self._edge_list[x]:
                        self._used[u] = True
                        print("from {} to {}".format(x, u))
                        new_set.add(u)
                    new_set.add(x)
                clusters.append([x for x in new_set])

        return clusters


def main():
    in_r = sys.argv[1]
    in_d = sys.argv[2]
    gr = Graph(Reader(in_r), Reader(in_d))
    clusters = Mcl(gr)
    print(len(clusters._clusters))

if __name__ == "__main__":
    main()
