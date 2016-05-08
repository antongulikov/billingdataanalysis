__author__ = 'scorpion'


from draw_top_places import HEAD, TAIL
from gen_color import GenColor
from sort_by_day import Reader
from gen_top_html import new_path
import sys


def generate_html(edge_r: Reader, d_r: Reader, out_f:str):
    pos = {}
    while True:
        line = d_r.get_line()
        if line is None:
            break
        line = line[0].split()
        p = int(line[0])
        lan = float(line[1])
        lng = float(line[2])
        pos[p] = (lan, lng)
    values = []
    all = []
    while True:
        line = edge_r.get_line()
        if line is None:
            break
        u, v, c = list(map(int, line[0].split(" ")))
        values.append(c)
        all.append((u, v, c))
    gc = GenColor(values)
    ret = HEAD
    for i, x in enumerate(all):
        ret += new_path(i, pos[x[0]], pos[x[1]], gc.get_color(x[2]))
    ret += TAIL
    with open(out_f, "w") as file:
        file.write(ret)


def main():
    ver_in = sys.argv[1]
    desc_in = sys.argv[2]
    out_f = sys.argv[3]
    ver_reader = Reader(ver_in)
    desc_r = Reader(desc_in)
    generate_html(ver_reader, desc_r, out_f)

if __name__ == "__main__":
    main()
