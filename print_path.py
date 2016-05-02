__author__ = 'scorpion'

import sys
from sort_by_day import Reader


class Point:
    def __init__(self, cell_id=0, lac=0, lon=0, lat=0):
        self._cell_id = cell_id
        self._lac = lac
        self._lon = lon
        self._lat = lat

    def get_lat(self):
        return self._lat

    def get_lon(self):
        return self._lon

    def __hash__(self):
        return self._hash()

    def _hash(self):
        return str(self._cell_id) + "#" + str(self._lac)

    def __le__(self, other):
        return hash(self) < hash(other)


class Location:
    def __init__(self, file_name: str):
        self._reader = Reader(file_name)
        self._map_location = {}
        self._build()

    def _build(self):
        current_line = self._reader.get_line()
        while current_line is not None:
            current_line = self._reader.get_line()
            if current_line is None:
                break
            # ['cell_id', 'lac', 'lon', 'lat', 'adr']
            try:
                cell_id = int(current_line[0])
                lac = int(current_line[1])
                lon = float(current_line[2])
                lat = float(current_line[3])
            except Exception as e:
                print(e.with_traceback(), file=sys.stderr)
            self._map_location[(cell_id, lac)] = Point(cell_id, lac, lon, lat)

    def get_point(self, cell_id, lac):
        ret = self._map_location.get((cell_id, lac), None)
        return ret


def main():
    pass

if __name__ == "__main__":
    main()
