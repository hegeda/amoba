# coding=utf-8
print ('Amőba játék')
j='X'

def tabla_init(a1, a2, a3, b1, b2, b3, c1, c2, c3):
    tbl = {'a1': a1, 'a2': a2, 'a3': a3, 'b1': b1, 'b2': b2, 'b3': b3, 'c1': c1, 'c2': c2, 'c3': c3}
    print tbl['a1'], '|', tbl['a2'], '|', tbl['a3']
    print tbl['b1'], '|', tbl['b2'], '|', tbl['b3']
    print tbl['c1'], '|', tbl['c2'], '|', tbl['c3']


def tabla(a1, a2, a3, b1, b2, b3, c1, c2, c3):
    pass

def valtas(j):
    if j == 'X':
        valt='O'
        print'O jön'
    else:
        valt='X'
        print'X jön'
    return valt

def bevitel():
    bev = input("Koordináták (pl.: a2): ")
    return bev

def ertekel():

    valtas()



print tabla_init('-', '-', '-', '-', '-', '-', '-', '-', '-')
