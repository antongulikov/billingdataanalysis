# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import numpy as np
import pandas as pd
import sys

# <codecell>

fans = set()
data = pd.read_table("./hp3", sep=",", low_memory=False)
print(len(data))

# <codecell>

def get_user(data):
    stadium_lacs = ["200966002", "52895"]
    n = len(data)
    ret = set()
    for i in range(n):        
        try:
            if data['cell'][i] in stadium_lacs:                
                ret.add(data['code'][i])
        except:
            pass
    return ret

# <codecell>


# <codecell>


# <codecell>

fans = get_user(data)
print("got_fans", file=sys.stderr)

# <codecell>

print(len(fans))

# <codecell>

How_Many = 5
list_fans = [x for x in fans]
#rnd.shuffle(list_fans)
top_100 = list_fans[:How_Many]

# <codecell>


def get_persons_inf(data, wanted):
    n = len(data)    
    ret = []
    da = data.values
    for i in range(n):
        try:
            if int(data['code'][i]) in wanted:                
                ret.append(da[i])
        except:
            pass
    return ret

# <codecell>

interesting_events = get_persons_inf(data, top_100)

# <codecell>

#data.head(1)
man = 38920
tmp = []
for x in interesting_events:
    if x[4] == man:
        tmp.append(x)
interesting_events = tmp

# <codecell>

coordinates = pd.read_table("./locations2.csv", sep=",")

# <codecell>

coord = {}
n_cor = len(coordinates)
for i in range(n_cor):
        try:
            coord[int(coordinates['id'][i])] = (coordinates[' lon'][i], coordinates[' lat'][i])
        except:
            pass

# <codecell>


# <codecell>


# <codecell>

good = set()

for x in tmp:
    try:        
        if coord.get(int(x[2])) is not None:
            good.add(x[2])
    except:
        pass
good

# <codecell>

cnt_ = 0
dif_location = []
for val in good:
    key = int(val)
    dif_location.append([coord[key][0], coord[key][1], key])
temp1 = "var myLatLng{0}"
tmp2 = "lng: {}, lat: {}"
tempM = """var marker{} = new google.maps.Marker("""
to = """{
    map: map,"""
st2 = """
    position: myLatLng{0},
    title: '{1}'"""  
cnt_ = 0
with open("geo3.html", "w") as file:
    for lng, lat, dist in dif_location:
        cnt_ += 1
        s1 = temp1.format(cnt_) + " = { " + tmp2.format(lng, lat) + "};\n\n"
        s2 = tempM.format(cnt_) + to + st2.format(cnt_, dist) + "\n});\n\n"
        file.write(s1 + s2)

# <codecell>

def getColor(x):    
    pos = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    x = int(x.__hash__())     
    col = int(x) % (256 * 256 * 256)
    p1 = col % 256
    col //= 256
    p2 = col % 256
    col //= 256
    return pos[p1 % 16] + pos[p1 // 16] + pos[p2 % 16] + pos[p2 // 16] + pos[col % 16] + pos[col // 16]

# <codecell>

from collections import defaultdict

# <codecell>

people = defaultdict(list)

# <codecell>

interesting_events[0]

# <codecell>

for x in interesting_events:
    people[x[-1]].append(x[2])

# <codecell>

interesting_events = sorted(interesting_events, key= lambda x: x[0])

# <codecell>

def pathes(file):
    firline = """<!DOCTYPE html>
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
  var myLatLng = {lat: 59.93, lng: 30.31};

  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 4,
    center: myLatLng
  });\n
"""
    file.write(firline)
    cntt = 0
    kol = 0
    for key, value in people.items():
        cntt += 1
        ret = "var flightPlanCoordinates{} = [\n".format(cntt)   
        prev = None
        for x in value:
            try:
                y = int(x)
                xx, yy = coord[y]
                xx, yy = yy, xx
                if y != prev:
                    ret += "{lat:" + str(xx) + ", lng:" + str(yy) + "},\n"
                prev = y
            except:
                pass
        ret = ret[:len(ret) - 2]
        ret += "\n];"
        color = getColor(key)    
        if (len(ret) > 40):
            ret += "var flightPath{}".format(cntt) + " = new google.maps.Polyline({"+"path: flightPlanCoordinates{}".format(cntt)+ """,
    geodesic: true,"""
            ret += "strokeColor: '#" + color + "'," + """strokeOpacity: 1.0,
            map: map,
        strokeWeight: 2
      });
    """            
            kol += 1
            ret += "\n"
            file.write(ret)
    lastLine = """   
}
    </script>
    <script async defer
        src="https://maps.googleapis.com/maps/api/js?key=AIzaSyD6hN5SpQ9nuAmUIabHRrHetOdz2mgyXLQ&signed_in=true&callback=initMap"></script>
  </body>
</html>"""
    file.write(lastLine)

# <rawcell>

#   var flightPlanCoordinates = [
#     {lat: 37.772, lng: -122.214},
#     {lat: 21.291, lng: -157.821},
#     {lat: -18.142, lng: 178.431},
#     {lat: -27.467, lng: 153.027}
#   ];
#   var flightPath = new google.maps.Polyline({
#     path: flightPlanCoordinates,
#     geodesic: true,
#     strokeColor: '#FF0000',
#     strokeOpacity: 1.0,
#     strokeWeight: 2
#   });
# 
#   flightPath.setMap(map);

# <codecell>

with open("patheh.html", "w") as file:
    pathes(file)

# <codecell>


# <codecell>


