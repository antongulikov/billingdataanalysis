__author__ = 'scorpion'

import sys

from Person import Person, Event
from print_path import Location, Point
from sort_by_day import Reader
from print_user_path import PathPrinter, TimePosition

class Person_oracle:

    def __init__(self, person_file):
        self._reader = Reader(person_file)
        self._reader.seek_line()
        self._persons = []
        self._np = 0
        self._cp = 0
        self._read()

    def _read(self):
        line = self._reader.get_line()
        while line is not None:
            if not self._persons:
                new_name = line[-1]
                self._persons.append(Person(new_name))
                self._np += 1
            if not self._persons[-1].add_event(",".join(line)):
                new_name = line[-1]
                self._persons.append(Person(new_name))
                self._np += 1
                self._persons[-1].add_event(",".join(line))
            line = self._reader.get_line()

    def __iter__(self):
        self._cp = 0
        return self

    def __next__(self):
        if self._cp == self._np:
            raise StopIteration
        self._cp += 1
        return self._persons[self._cp - 1]


def test(oracle: Person_oracle, path_printer: PathPrinter):
    for person in oracle:
        way = path_printer.generate_user_path(person)
        if way is not None:
            with open("./new_data/user_pathes/" + person._user_id + ".html", "w") as file:
                file.write(way)


# name = ./foo/bar/tmp/*.*.*.csv
def get_file_name(name: str):
    tmp = name.split("/")
    tmp = tmp[-1]
    return tmp


def test2(oracle: Person_oracle, positions_printer: TimePosition):
    file_name = get_file_name(sys.argv[1])
    with open("./new_data/positions/" + file_name, "w") as file:
        file.write("time,lat,lon\n")
        for person in oracle:
            way = positions_printer.generate_user_positions(person)
            if way is not None:
                file.write(way)


def main():
    person_file = sys.argv[1]
    location_file = sys.argv[2]
    oracle = Person_oracle(person_file)
    location = Location(location_file)
    path_printer = PathPrinter(location)
    position_printer = TimePosition(location)
    #test(oracle, path_printer)
    test2(oracle, position_printer)

if __name__ == "__main__":
    main()
