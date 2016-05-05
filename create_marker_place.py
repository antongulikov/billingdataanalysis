__author__ = 'scorpion'


from sort_by_day import Reader
import sys


def counter():
    value = 0
    while True:
        value += 1
        yield value

g = counter()


def new_maker(point, num):
    position = next(g)
    ret = "\nvar myLatLng{}".format(position) + " = { lng:"
    ret = ret + str(point[1]) + ", lat: " + str(point[0]) +"};\n"
    ret = ret + "var marker{}".format(position) + """= new google.maps.Marker({
                                                map: map, position: myLatLng""" +str(position)+""",title:'""" + str(int(num)) + """'});\n
                                                """
    return ret


def build_html(reader: Reader):
    result = """<!DOCTYPE html>
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
    zoom: 4,
    center: myLatLng
  });"""
    while True:
        line = reader.get_line()
        if line is None:
            break
        lat, lon, num = list(map(float, line[0].split(" ")))
        result += new_maker((lat, lon), num)
    result += """}
    </script>
    <script async defer
        src="https://maps.googleapis.com/maps/api/js?key=AIzaSyD6hN5SpQ9nuAmUIabHRrHetOdz2mgyXLQ&signed_in=true&callback=initMap"></script>
  </body>
</html>"""
    return result


def main():
    in_file_name = sys.argv[1]
    in_reader = Reader(in_file_name)
    ret = build_html(in_reader)
    out_file = in_file_name.split("/")
    out_file[-1] = "markers.html"
    out_file = "/".join(out_file)
    with open(out_file, "w") as file:
        file.write(ret)


if __name__ == "__main__":
    main()
