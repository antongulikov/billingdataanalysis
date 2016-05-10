__author__ = 'scorpion'


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

    def __iter__(self):
        return self

    def __next__(self):
        line = self.get_line()
        if line is None:
            raise StopIteration
        return line

    def __del__(self):
        self._in.close()


def main():
    in_file = "YOUR FILE"
    rd = Reader(in_file)
    header = rd.get_line()
    pattern = "new_anna{}.csv"
    cnt = 3
    pos = 0
    file = open(pattern.format(pos), "w")
    file.write(header + "\n")
    for line in rd:
        if cnt == 0:
            file.close()
            pos += 1
            file = open(pattern.format(pos), "w")
            file.write(header + "\n")
        else:
            file.write(",".join(list(map(str, line))) + "\n")
            cnt -= 1


if __name__ == "__main__":
    main()
