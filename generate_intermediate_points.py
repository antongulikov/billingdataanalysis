__author__ = 'scorpion'

from requests import get
import sys
from sort_by_day import Reader
from parse_direction_json_request import parse_json_direction_google_points

PATTERN = "https://maps.googleapis.com/maps/api/directions/json?origin={0}&destination={1}&key=AIzaSyAcS-REOnlfW6ulHKR4YybMQyi_O4VgIVc"


def make_lat_lng(x):
    return str(x[0]) + "," + str(x[1])


def main():
    in_file = sys.argv[1]
    ret_file = sys.argv[2]
    reader = Reader(in_file)
    all_points = []
    while True:
        line = reader.get_line()
        if line is None:
            break
        line = list(map(float, line))
        line[0] = int(line[0])
        line[1] = int(line[1])
        all_points.append(line)

    with open(ret_file, "w") as ret_file:
        for x in all_points:
                req_url = PATTERN.format(make_lat_lng((x[2], x[3])), make_lat_lng((x[4], x[5])))
                r = get(req_url)
                with open("tmp.json", "w") as file_json:
                    file_json.write(r.text)
                j_p = parse_json_direction_google_points("tmp.json")
                ret_file.write(" ".join(list(map(str, x))) + "\n")
                ret_file.write(str(len(j_p)) + "\n")
                for p in j_p:
                    ret_file.write(str(p[0]) + " " + str(p[1]) + "\n")


if __name__ == "__main__":
    main()