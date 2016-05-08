__author__ = 'scorpion'


from sort_by_day import Reader
import sys
from collections import defaultdict

files_id = [10, 20, 30, 40, 60, 80, 100, 120, 1440]
FLOW_PATTERN = "./new_data/graph_near_petr/g{}/flow_data/top_edges.data"
DESC_PATTERN = "./new_data/graph_near_petr/g{0}/g{0}.desc"
OUT_FILE = "./new_data/graph_near_petr/interesting_path.data"
DESC_FILE = "./new_data/graph_near_petr/desc_path.data"


def main():
    with open(OUT_FILE, "w") as o_file:
        used_c = defaultdict(int)
        for file_id in files_id:
            desc_reader = Reader(DESC_PATTERN.format(file_id))
            flow_reader = Reader(FLOW_PATTERN.format(file_id))
            coord = {}
            while True:
                line = desc_reader.get_line()
                if line is None:
                    break
                line = line[0].split(" ")
                p = int(line[0])
                lat, lng = list(map(float, [line[2], line[3]]))
                if (lat, lng) not in used_c:
                    used_c[(lat, lng)] = len(used_c) + 1
                coord[p] = (lat, lng)
            while True:
                line = flow_reader.get_line()
                if line is None:
                    break
                line = line[0].split(" ")
                v, u, c = list(map(int, line))
                from_ = coord[v]
                to_ = coord[u]
                p_v = used_c[from_]
                p_u = used_c[to_]
                o_file.write(",".join(list(map(str, [p_v, p_u, from_[0], from_[1], to_[0], to_[1]]))) + "\n")
    with open(DESC_FILE, "w") as d_file:
        for key, value in used_c.items():
            d_file.write(",".join(list(map(str, [value, key[0], key[1]]))) + "\n")

if __name__ == "__main__":
    main()
