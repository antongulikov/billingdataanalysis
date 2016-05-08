__author__ = 'scorpion'

import json
import sys
from bs4 import BeautifulSoup
from requests import request, get


def parse_json_direction_google_points(json_req):
    with open(json_req, encoding="utf-8") as file:
        json_dict = json.load(file)
    inter_points = json_dict['routes'][0]['legs'][0]['steps']
    points = []
    for x in inter_points:
        pos = x['start_location']
        lat = float(pos['lat'])
        lng = float(pos['lng'])
        points.append((lat, lng))
    return points


def main():
    ret = sys.argv[1]
    pt = parse_json_direction_google_points(ret)
    for x in pt:
        print(x)


if __name__ == "__main__":
    main()



