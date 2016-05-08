__author__ = 'scorpion'

import sys

from sort_by_day import Reader
from random import randint


def generate_random_color():
    values = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    ret = ""
    for i in range(6):
        ret += values[randint(0, 15)]
    return ret


def gen_number():
    cnt = 0
    while True:
        cnt += 1
        yield cnt



HEADER = """<!DOCTYPE html><html><head>
                    <meta name="viewport" content="initial-scale=1.0, user-scalable=no">
                    <meta charset="utf-8"><title>Top_edges</title>
                    <style> html, body { height: 100%; margin: 0; padding: 0; }
                    #map {  height: 100%; } </style> </head> <body> <div id="map"></div>
                    <script> function initMap() {
                    var myLatLng = {lat: 59.93, lng: 30.31};
                    var map = new google.maps.Map(document.getElementById('map'), {
                    zoom: 10, center: myLatLng });"""


def new_path(num, cor_from, cor_to, color):
    ret = "var flights{}=".format(num)
    ret += "[" + "{lat:" + str(cor_from[0]) + ",lng:" + str(cor_from[1])+"},"+\
           "{lat:" + str(cor_to[0]) + ",lng:" + str(cor_to[1]) + "}];\n"
    ret += "var fpath{}".format(num) + \
           " = new google.maps.Polyline({path: flights" + str(num) +\
           ",geodesic: true,strokeColor: '#" +\
           str(color) + """',strokeOpacity: 1.0, map: map,strokeWeight: 2 });""" + "\n"
    return ret


def add_new(cor_from, cor_to, file):
    all = next(gen_number())
    ret = new_path(all, cor_from, cor_to, generate_random_color())
    file.write(ret)


def build_html(descr: Reader, top: Reader, file):
    coordinates = {}
    file.write(HEADER + "\n")
    while True:
        line = descr.get_line()
        if line is None:
            break
        line = line[0].split(" ")
        pos, time, lat, lon = list(map(float, line))
        pos = int(pos)
        coordinates[pos] = (lat, lon)
    while True:
        line = top.get_line()
        if line is None:
            break
        line = line[0].split(" ")
        from_v, to_v, cnt = list(map(int, line))
        cor_from = coordinates[from_v]
        cor_to = coordinates[to_v]
        add_new(cor_from, cor_to, file)
    file.write("""}
                    </script> <script async defer
                    src="https://maps.googleapis.com/maps/api/js?key=AIzaSyD6hN5SpQ9nuAmUIabHRrHetOdz2mgyXLQ&signed_in=true&callback=initMap"></script>
                    </body></html>""")


def get_out_name(name: str):
    name = name[:-4]
    return name + "html"


def main():
    descr_file = sys.argv[1]
    ret_file = sys.argv[2]
    descr_reader = Reader(descr_file)
    file_reader = Reader(ret_file)
    out_file_name = get_out_name(ret_file)
    out_file = open(out_file_name, "w")
    build_html(descr_reader, file_reader, out_file)
    out_file.close()

if __name__ == "__main__":
    main()
