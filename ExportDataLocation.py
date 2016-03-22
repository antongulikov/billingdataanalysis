# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from openpyxl import load_workbook
xl_files = load_workbook('./report.xlsx')

# <codecell>

sheet = xl_files.get_sheet_by_name('SQL Results')

# <codecell>

class Location:
    def __init__(self, lac, lon, lat, address):
        self._lac = lac
        self._lon = lon
        self._lat = lat
        self._address = address.replace(",", "_")
        
    def set_lac(self, lac):
        self._lac = lac
        
    def set_lon(self, lon):
        self._lon = lon
    
    def set_lan(self, lat):
        self._lat = lat
        
    def set_address(self, address):
        self._address = address
        
    def __eq__(self, other):
        return self._lac == other._lac and self._address == self._address
    
    def __hash__(self):
        return self._get_hash()
    
    def __le__(self, other):
        if self._lac != other._lac:
            return self._lac < other._lac
        return self._address < other._address
        
    def __str__(self):
        return ",".join(list(map(str, [self._lac, self._lon, self._lat, self._address])))
    
    def _get_hash(self):
        base = int(1e9 + 7)
        pr = 17
        ret_hash = 0
        for x in self._address:
            add_value = ord(x)
            ret_hash *= pr
            ret_hash += add_value
            ret_hash %= base
        return ret_hash
        
    
    def __repr__(self):
        return str(self)                 

# <codecell>


# <codecell>


# <codecell>

n = len(sheet.columns[0])
locations = set()
for id in range(2, n + 1):
    lac = sheet['B'+str(id)].value
    lon = sheet['C'+str(id)].value
    lat = sheet['D'+str(id)].value
    address = sheet['E'+str(id)].value    
    loc = Location(lac, lon, lat, address)
    try:
        locations.add(loc)
    except:
        pass
print(len(locations))

# <codecell>

with open("locations.csv", "w") as file_csv:
    file_csv.write('lac, lon, lat, adr\n')
    for x in locations:
        file_csv.write(str(x))
        file_csv.write("\n")

# <codecell>


