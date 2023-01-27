import re
from NUM import NUM
from SYM import SYM

class COLS:
    names = []
    all, xcols, ycols, skipcols = [], [], [], []
    klass = ''

    def __init__(self, t):
        for n, s in enumerate(t):
            col = NUM(n,s) if (len(re.findall(r'^[A-Z]+', s)) > 0) else SYM(n, s)
            self.all.append(col)
            self.names.append(s)

            self.skipcols.append(col) if (len(re.findall(r'X$', s)) > 0) else self.assign_klass(col) if (len(re.findall(r'!$', s)) > 0) else 1
            self.ycols.append(col) if len(re.findall(r'[!+-]$', s)) > 0 else self.xcols.append(col)

    def add(self, row):
        for col in self.xcols:
            col.add(row.get_cells()[col.get_pos()]) # for col in self.xcols

        [col.add(row.get_cells()[col.get_pos()]) for col in self.ycols]

    def assign_klass(self, col):
        self.klass = col