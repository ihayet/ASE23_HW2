from COLS import COLS
from ROW import ROW
from lists import map, kap

class DATA:
    def __init__(self, src):
        self.rows, self.cols = [], None
        if type(src) == 'string':
            pass
        else:
            map([] if (src is None) else src, lambda x: self.add(x))

    def add(self, t):
        if self.cols is not None:
            t = t if isinstance(t, ROW) else ROW(t)
            self.rows.append(t)
            self.cols.add(t)
        else:
            self.cols = COLS(t)
        return t, None

    def clone(self, init):
        data = DATA(self.cols.all)
        map(init if init is not None else [], lambda x: data.add(x))
        return data

    def stats(self, what, cols, nPlaces):
        def fun(k, col):
            return col.rnd(col.mid() if (what == 'mid') else col.div(), nPlaces), col.get_name()
        return kap(self.cols.ycols if (cols is None or len(cols) == 0) else cols, fun)

c = COLS(['Num', 'IgX', 'sym'])
d = DATA(c.all)
d.add(['Num', 'IgX', 'sym'])
d.add(ROW([5, 1 , 'a']))
d.add(ROW([15, 2 , 'b']))
d.add(ROW([15, 3 , 'a']))

print(d.stats('mid', (d.cols.xcols + d.cols.ycols), 2))
print(d.clone(None))