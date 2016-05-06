__author__ = 'scorpion'

import sys
import os
from sort_by_day import Reader
from collections import defaultdict


def main():
    dir_name = sys.argv[1]
    file_name = "./new_data/graph_near_petr/g{}/flow_data/flow_result/".format(dir_name)
    file_list = os.listdir(file_name)
    flow_result = defaultdict(int)
    capacity_result = defaultdict(int)
    for f_name in file_list:
        reader = Reader(file_name + f_name)
        line = reader.get_line()
        if line == "0":
            continue
        while True:
            line = reader.get_line()
            if line is None:
                break
            elements = line[0].split(" ")
            v, u, f, c = list(map(int, elements[:4]))
            flow_result[(v, u)] += f
            capacity_result[(v, u)] += c
    ret = sorted([(key, value) for key, value in flow_result.items()], key=lambda x: -x[1])
    with open("./new_data/graph_near_petr/g{}/flow_data/top_edges.data".format(dir_name), "w") as file:
        for key, value in ret[:100]:
            file.write(str(key[0]) + " " + str(key[1]) + " " + str(value) + "\n")


if __name__ == "__main__":
    main()