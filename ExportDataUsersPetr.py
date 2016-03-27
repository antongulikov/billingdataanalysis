# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

name = input()
from openpyxl import load_workbook
xl_files = load_workbook(name)

# <codecell>

sheet = xl_files.get_sheet_by_name('Sheet1')

# <codecell>


# <codecell>

_print = False
for row in sheet.rows:
    if _print:
        print(",".join([str(cell.value) for cell in row]))
    _print = True

# <codecell>


# <codecell>


# <codecell>


# <codecell>


