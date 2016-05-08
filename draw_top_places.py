__author__ = 'scorpion'

from gen_color import GenColor
from sort_by_day import Reader
import sys

HEAD = """<!DOCTYPE html>
<html>
  <head>
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no">
    <meta charset="utf-8">
    <title>Coordinates</title>
    <style>
      html, body {
        height: 100%;
        margin: 0;
        padding: 0;
      }
      #map {
        height: 100%;
      }
    </style>
  </head>
  <body>
    <div id="map"></div>
    <script>


function initMap() {
  var myLatLng = {lat: 60, lng: 30};

  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 10,
    center: myLatLng
  });"""


TAIL = """                                              }
    </script>
    <script async defer
        src="https://maps.googleapis.com/maps/api/js?key=AIzaSyD6hN5SpQ9nuAmUIabHRrHetOdz2mgyXLQ&signed_in=true&callback=initMap"></script>
  </body>
</html>"""


def add_marker(num, coordinate, color):
    im = """var im{0} = new google.maps.MarkerImage("http://www.googlemapsmarkers.com/v1/{1}/");""".format(num, color)
    lanlng = "var c{}".format(num) + " = { lng:" + str(coordinate[1]) + ", lat: " +str(coordinate[0]) +"};"
    marker = """var marker""" +str(num) + """= new google.maps.Marker({icon: im""" + str(num) + """,
                                                map: map, position: c""" + str(num) + """,title:'""" + color + """'});"""
    return "\n".join([im, lanlng, marker])


def generate_html(v_r: Reader, d_r: Reader, out_f: str):
    all = []
    values = []
    ret = HEAD
    while True:
        line = v_r.get_line()
        if line is None:
            break
        v, c = list(map(int, line[0].split()))
        values.append(c)
        all.append((v, c))
    print(values)
    gc = GenColor(values)
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
    for i, x in enumerate(all):
        ret += add_marker(i, pos[x[0]], gc.get_color(x[1]))
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
