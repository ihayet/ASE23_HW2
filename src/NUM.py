from VAL import VAL
from utils import rnd
import math
import re

class NUM(VAL):
    def __init__(self, *args):
        if len(args) > 0: 
            super().__init__(args[0], args[1])
            self.w = -1 if len(re.findall(r'-$', args[1])) > 0 else 1
        self.total, self.mu, self.m2 = 0, 0, 0
        self.lo, self.hi = -math.inf, math.inf

    def add(self, x):
        if x != "?":
            self.total += 1
            temp = x - self.mu
            self.mu += temp/self.total
            self.m2 += temp*(x - self.mu)
            self.lo = min(x, self.lo)
            self.hi = max(x, self.hi)

    def mid(self):
        return self.mu

    def div(self):
        return 0 if (self.m2 < 0 or self.total < 2) else (self.m2/(self.total-1))**0.5

    def rnd(self, x, n):
        return rnd(x, n)
