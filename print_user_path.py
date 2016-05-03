__author__ = 'scorpion'

from Person import Person, Event
from print_path import Location, Point
from time_oracle import TimeOracle


class PathPrinter:

    def __init__(self, locations: Location):
        self._locations = locations

    def _make_head(self, user_name: str):
        result = """<!DOCTYPE html><html><head>
                    <meta name="viewport" content="initial-scale=1.0, user-scalable=no">
                    <meta charset="utf-8"><title>""" + user_name + """</title>
                    <style> html, body { height: 100%; margin: 0; padding: 0; }
                    #map {  height: 100%; } </style> </head> <body> <div id="map"></div>
                    <script> function initMap() {
                    var myLatLng = {lat: 59.93, lng: 30.31};
                    var map = new google.maps.Map(document.getElementById('map'), {
                    zoom: 10, center: myLatLng }); var flights = """
        return result

    def _make_tail(self):
        result = """];var fpath = new google.maps.Polyline({path: flights,
                    geodesic: true,strokeColor: '#2B0277',strokeOpacity: 1.0, map: map,
                    strokeWeight: 2 });}
                    </script> <script async defer
                    src="https://maps.googleapis.com/maps/api/js?key=AIzaSyD6hN5SpQ9nuAmUIabHRrHetOdz2mgyXLQ&signed_in=true&callback=initMap"></script>
                    </body></html>"""
        return result

    def _gen_coordinate(self, point: Point):
        return "{lat:" + str(point.get_lat()) + "," + "lng:" + str(point.get_lon()) + "}"

    def generate_user_path(self, user: Person):
        result = self._make_head(user._user_id)
        previous = (0, 0)
        for event in user._events:
            current_position = event.get_cell_with_lac()
            if previous[0] == current_position[0] and previous[1] == current_position[1]:
                continue
            # event[0] = cell_id, event[1] = lac
            new_point = self._locations.get_point(*event.get_cell_with_lac())
            symbol = ","
            if previous == (0, 0):
                symbol = "["
            if new_point is None:
                continue
            result += symbol + self._gen_coordinate(new_point)
            previous = current_position
        if previous == (0, 0):
            pass
        result += self._make_tail()
        if previous == (0, 0):
            result = None
        return result


class TimePosition:

    def __init__(self, locations: Location):
        self._location = locations
        self._time_oracle = TimeOracle()

    def generate_user_positions(self, user: Person):
        result = ""
        previous = (0, 0)
        for event in user._events:
            current_position = event.get_cell_with_lac()
            new_point = self._location.get_point(*current_position)
            if new_point is None:
                continue
            result += ",".join(list(map(str, [self._time_oracle.get_full_time(event.get_date()),
                                              new_point.get_lat(), new_point.get_lon()])))
            result += "\n"
            previous = current_position
        if previous == (0, 0):
            result = None
        return result