from SYM import SYM
from NUM import NUM
from strings import o, oo
from utils import getThe, rand, rnd, setSeed, get_ofile
from csv import csv
from DATA import DATA

def settings_test():
    err = 0
    val = oo(getThe())
    err += 1 if val != '{:dump false :file etc/data/auto93.csv :go all :help false :seed 937162211}' else 0
    return err

def rand_test():
    err = 0
    num1, num2 = NUM(), NUM()

    setSeed(getThe()['seed'])
    for i in range(1, 10**3):
        num1.add(rand(0, 1))
    
    setSeed(getThe()['seed'])
    for i in range(1, 10**3):
        num2.add(rand(0, 1))

    m1, m2 = rnd(num1.mid(), 10), rnd(num2.mid(), 10)

    if m1 != m2:
        err += 1
    if rnd(m1, 1) != 0.5:
        err += 1

    return err

def sym_test():
    err, sym = 0, SYM()
    for c in ["a","a","a","a","b","b","c"]:
        sym.add(c)
    
    if sym.mid() != "a":
        err += 1
    if sym.div() > (1.379 + 0.001) or sym.div() < (1.379 - 0.001):
        err += 1
    return err

def num_test():
    err, num = 0, NUM()
    for i in [1,1,1,1,2,2,3]:
        num.add(i)

    if num.mid() > (1.57142857 + 0.01) or num.mid() < (1.57142857 - 0.01):
        err += 1
    if rnd(num.div()) > (0.787 + 0.01) or rnd(num.div()) < (0.787 - 0.01):
        err += 1
    return err

def csv_test():
    err, n = 0, 0
    t = csv(getThe()['file'])

    for i in range(len(t)):
        for j in range(len(t[i])):
            n += 1
    if n != 8*399:
        err += 1
    return err

def data_test():
    err = 0
    data = DATA(getThe()['file'], None, None)
    err += 1 if len(data.rows) != 398 else 0
    err += 1 if data.cols.ycols[0].w != -1 else 0
    err += 1 if data.cols.xcols[0].col_pos != 0 else 0
    err += 1 if len(data.cols.xcols) != 4 else 0
    return err

def stats_test():
    err = 0
    res = ''
    data = DATA(getThe()['file'], None, None)
    for k, cols in zip(['y', 'x'], [data.cols.ycols, data.cols.xcols]):
        res += k + ' mid ' + o(data.stats('mid', cols, 2)) + '\n'
        res += ' ' + ' div ' + o(data.stats('div', cols, 2))
        if k != 'x': res += '\n'
    print(res)
    get_ofile().write(res + '\n')
    err += 1 if res != 'y mid {:Acc+ 15.57 :Lbs- 2970.42 :Mpg+ 23.84}\n  div {:Acc+ 2.76 :Lbs- 846.84 :Mpg+ 8.34}\nx mid {:Clndrs 5.45 :Model 76.01 :Volume 193.43 :origin 1}\n  div {:Clndrs 1.7 :Model 3.7 :Volume 104.27 :origin 1.3273558482394003}' else 0
    return err
