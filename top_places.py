__author__ = 'scorpion'


import sys
from sort_by_day import Reader
from collections import defaultdict


def find_top_vertex(reader: Reader):
    count_vertex = defaultdict(int)
    while True:
        line = reader.get_line()
        if line is None:
            break
        v, u = list(map(int, line[0].split(" ")))
        count_vertex[v] += 1
        count_vertex[u] += 1
    top_list = [(key, value) for key, value in count_vertex.items()]
    top_list = sorted(top_list, key=lambda x: -x[1])
    return top_list


def get_points(reader: Reader):
    points = {}
    while True:
        line = reader.get_line()
        if line is None:
            break
        id, time, lan, lot = list(map(float, line[0].split(" ")))
        id , time = list(map(int, [id, time]))
        points[id] = (time, lan, lot)
    return points


def merge_data(list_top, all_points):
    geo_location = defaultdict(int)
    for id in list_top:
        point = id[0]
        value = id[1]
        coordinate = (all_points[point][1], all_points[point][2])
        geo_location[coordinate] += value
    top_points = [(key, value) for key, value in geo_location.items()]
    top_points = sorted(top_points, key=lambda x: -x[1])
    return top_points[:30]



def main():
    desc_file = sys.argv[1]
    graph_file = sys.argv[2]
    out_file = sys.argv[3]
    desc_reader = Reader(desc_file)
    graph_reader = Reader(graph_file)
    list_top = find_top_vertex(graph_reader)
    all_points = get_points(desc_reader)
    list_top = merge_data(list_top, all_points)
    with open(out_file, "w") as file:
        for point in list_top:
            file.write(str(point[0][0]) + " ")
            file.write(str(point[0][1]) + " ")
            file.write(str(point[1]) + "\n")

if __name__ == "__main__":
    main()
