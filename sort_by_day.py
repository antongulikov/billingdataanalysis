import pandas as pd
import numpy as np
import os
import sys


class Reader:
    bad_values = ["", "None"]

    def __init__(self, in_file):
        self._in = open(in_file)

    def seek_line(self):
        self._in.readline()

    def get_line(self):
        ok = True
        result = None
        while ok:
            try:
                ok = False
                line = self._in.readline().rstrip()
                ret = line.split(",")
                if line == "":
                    break
                for x in ret:
                    if x in Reader.bad_values:
                        ok = True
                if not ok:
                    result = ret
            except Exception as e:
                print(e.with_traceback(), file=sys.stderr)
                ok = False
        return result

    def __del__(self):
        self._in.close()


# <codecell>

def main():
    reader = Reader("./new_data/user_activities.csv")

    print(reader.get_line())

    open_files = []
    desc_files = {}

    ret = reader.get_line()
    cnt = 0
    while ret is not None:
        cnt += 1
        if cnt % 100000 == 0:
            print(cnt, ret)
        date = ret[0].split()[0]
        ret[0] = ret[0].split()[1]
        if not date in open_files:
            open_files.append(date)
            os.open("./new_data/days/" + date + ".csv", os.O_CREAT | os.O_RDWR)
            file_ = open("./new_data/days/" + date + ".csv", "w")
            desc_files[date] = file_
            file_.write("date,type,cell_id,lac,user_id\n")
        fi = desc_files[date]
        fi.write(",".join(ret) + "\n")
        ret = reader.get_line()

    for fi in desc_files.values():
        fi.close()


if __name__ == "__main__":
    main()
