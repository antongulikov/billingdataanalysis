__author__ = 'scorpion'

from sort_by_day import Reader
import sys
from random import randint
import math


def dist(ver1, ver2):
    x1, y1 = ver1[2], ver1[3]
    x2, y2 = ver2[2], ver2[3]
    return (x1 - x2) ** 2 + (y1 - y2) ** 2


def gen_shell(reader: Reader, file_name: str, num: int):
    vextex_list = []
    while True:
        line = reader.get_line()
        if line is None:
            break
        v, time, lan, lot = list(map(float, line[0].split(" ")))
        v = int(v)
        vextex_list.append((v, time, lan, lot))
    n = len(vextex_list)
    succ = 0

    eps = 1e-4

    out_file_shell = open(file_name, "w")

    best_in = 18 * 60 // num
    best_out = 23 * 60 // num
    time_eps = 2 * 60 // num

    shell_line = "../.././flow ../../g{0}/g{0} ../../g{0} {1} {2} \n echo \"{1} {2}\"\n echo \"iter={3}\" \n"

    while succ < 1000:
        p1 = randint(1, n) - 1
        p2 = randint(1, n) - 1
        if vextex_list[p1][1] > vextex_list[p2][1]:
            continue
        if dist(vextex_list[p1], vextex_list[p2]) < eps:
            continue
        if math.fabs(vextex_list[p1][1] - best_in) > time_eps:
            continue
        if math.fabs(vextex_list[p2][1] - best_out) > time_eps:
            continue
        succ += 1
        out_file_shell.write(shell_line.format(num, vextex_list[p1][0], vextex_list[p2][0], succ))

    out_file_shell.close()


def main():
    in_file = sys.argv[1]
    out_file = sys.argv[2]
    num_file = int(sys.argv[3])
    in_r = Reader(in_file)
    gen_shell(in_r, out_file, num_file)


if __name__ == "__main__":
    main()
