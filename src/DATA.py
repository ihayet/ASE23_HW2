from COLS import COLS
from ROW import ROW
from csv import csv
from lists import map, kap

class DATA:
    def __init__(self, src, cols, rows):
        self.rows, self.cols = [], None
        map(csv(src), lambda x: self.add(x)) if src is not None else map(cols+rows, lambda x: self.add(x))            

    def add(self, t):
        if not self.cols is None:
            t = t if isinstance(t, ROW) else ROW(t)
            self.rows.append(t)
            self.cols.add(t)
        else:
            self.cols = COLS(t)
        return t, None

    def clone(self):
        data = DATA(None, [self.cols.names], [row.get_cells() for row in self.rows])
        return data

    def stats(self, what, cols, nPlaces):
        def fun(k, col): return col.rnd(col.mid() if (what == 'mid') else col.div(), nPlaces), col.get_name()
        return kap(self.cols.ycols if (cols is None or len(cols) == 0) else cols, fun)