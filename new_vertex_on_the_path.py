__author__ = 'scorpion'

import sys
from sort_by_day import Reader
from collections import defaultdict


class Position:
    def __init__(self):
        self._map = defaultdict(int)
        self._cnt = 0

    def get_position(self, lan, lng):
        if (lan, lng) not in self._map:
            self._map[(lan, lng)] = self._cnt + 1
            self._cnt += 1
        return self._map[(lan, lng)]


def build_path(lst_vertex):
    ret = []
    for i, x in enumerate(lst_vertex):
        if i + 1 == len(lst_vertex):
            break
        ret.append((x, lst_vertex[i + 1]))
    return ret


def build_pathes_with_new_points(fl_r: Reader, de_r: Reader, in_r: Reader, out_file_name: str,
                                 desc_out_file: str):
    from_de_file = {}
    map_p = Position()
    pathes = defaultdict(list)
    while True:
        line = de_r.get_line()
        if line is None:
            break
        line = line[0].split(" ")
        lan, lng = list(map(float, line[2:4]))
        from_de_file[int(line[0])] = (lan, lng)
    while True:
        line = in_r.get_line()
        if line is None:
            break
        points_ = list(map(float, line[0].split(" ")))
        p1 = map_p.get_position(points_[2], points_[3])
        p2 = map_p.get_position(points_[4], points_[5])
        path = [p1]
        N = in_r.get_line()
        N = int(N[0])
        for j in range(N):
            line = in_r.get_line()
            lan, lng = list(map(float, line[0].split(" ")))
            tmp_p = map_p.get_position(lan, lng)
            path.append(tmp_p)
        path.append(p2)
        path = build_path(path)
        pathes[(p1, p2)] = path
    ret_edges = []
    while True:
        line = fl_r.get_line()
        if line is None:
            break
        p_s, p_f, cost = list(map(int, line[0].split(" ")))
        coord_s = from_de_file[p_s]
        coord_f = from_de_file[p_f]
        p_s1 = map_p.get_position(*coord_s)
        p_f1 = map_p.get_position(*coord_f)
        path = pathes[(p_s1, p_f1)]
        for vert in path:
            ret_edges.append((vert, cost))
    with open(out_file_name, "w") as file:
        for x in ret_edges:
            file.write(" ".join(list(map(str, [x[0][0], x[0][1], x[1]]))) + "\n")
    with open(desc_out_file, "w") as file:
        for key, value in map_p._map.items():
            file.write(" ".join(list(map(str, [value, key[0], key[1]]))))


def main():
    flow_filename = sys.argv[1]
    desc_filename = sys.argv[2]
    inter_filename = sys.argv[3]
    out_file = sys.argv[4]
    desc_out_file = sys.argv[5]
    fl_r = Reader(flow_filename)
    de_r = Reader(desc_filename)
    in_r = Reader(inter_filename)
    build_pathes_with_new_points(fl_r, de_r, in_r, out_file, desc_out_file)

if __name__ == "__main__":
    main()
