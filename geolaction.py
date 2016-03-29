# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import pandas as pd
import numpy as np
import sys

# <codecell>

data = pd.read_table('./locations.csv', sep=",")
tmp = data.values

# <codecell>

def get_different_location(data):
    data_array = data.values
    already_have = set()
    result = []
    for x in data_array:
        lon, lat, name = x[1:]
        if (lon, lat) in already_have:
            continue
        already_have.add((lon, lat))
        result.append(x[1:])
    return result

# <codecell>

dif_location = get_different_location(data)

# <codecell>

dif_location= sorted(dif_location, key=lambda x : (x[0], x[1]))

# <codecell>

temp1 = "var myLatLng{0}"
tmp2 = "lng: {}, lat: {}"
tempM = """var marker{} = new google.maps.Marker("""
to = """{
    map: map,"""
st2 = """
    position: myLatLng{0},
    title: '{1}'"""  
cnt_ = 0
with open("geo.html", "w") as file:
    for lng, lat, dist in dif_location:
        cnt_ += 1
        s1 = temp1.format(cnt_) + " = { " + tmp2.format(lng, lat) + "};\n\n"
        s2 = tempM.format(cnt_) + to + st2.format(cnt_, dist) + "\n});\n\n"
        file.write(s1 + s2)

# <codecell>


