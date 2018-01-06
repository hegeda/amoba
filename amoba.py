# coding=utf-8
print ('Amőba játék')
j = 'X'
tbl = {'a1': "", 'a2': "", 'a3': "", 'b1': "", 'b2': "", 'b3': "", 'c1': "", 'c2': "", 'c3': ""}
vege=False


def tabla(mezo, ertek):
    if mezo == 'I':
        ertek = "-"
        for i in tbl.iterkeys():
            tbl[i] = ertek
    elif mezo == 'a1':
        tbl['a1'] = ertek
    elif mezo == 'a2':
        tbl['a2'] = ertek
    elif mezo == 'a3':
        tbl['a3'] = ertek
    elif mezo == 'b1':
        tbl['b1'] = ertek
    elif mezo == 'b2':
        tbl['b2'] = ertek
    elif mezo == 'b3':
        tbl['b3'] = ertek
    elif mezo == 'c1':
        tbl['c1'] = ertek
    elif mezo == 'c2':
        tbl['c2'] = ertek
    elif mezo == 'c3':
        tbl['c3'] = ertek
    else:
        print 'Érvénytelen koordináta! Adj újat!'

    print tbl['a1'], '|', tbl['a2'], '|', tbl['a3']
    print tbl['b1'], '|', tbl['b2'], '|', tbl['b3']
    print tbl['c1'], '|', tbl['c2'], '|', tbl['c3']
    return ""


def valtas(valt):
    if j == 'X':
        valt = 'O'
        print'O jön'
    else:
        valt = 'X'
        print'X jön'
    return valt


def bevitel():
    bev = raw_input("Koordináták (pl.: a2): ")
    return bev


def ertekel():
    if tbl['a1'] == tbl['a2'] == tbl['a3']:
        print 'nyert'
        vege=True
    elif tbl['b1'] == tbl['b2'] == tbl['b3']:
        print 'nyert'
        vege = True
    elif tbl['c1'] == tbl['c2'] == tbl['c3']:
        print 'nyert'
        vege = True
    elif tbl['a1'] == tbl['b1'] == tbl['c1']:
        print 'nyert'
        vege = True
    elif tbl['a2'] == tbl['b2'] == tbl['c2']:
        print 'nyert'
        vege = True
    elif tbl['a3'] == tbl['b3'] == tbl['c3']:
        print 'nyert'
        vege = True
    elif tbl['a1'] == tbl['b2'] == tbl['c3']:
        print 'nyert'
        vege = True
    elif tbl['a3'] == tbl['b2'] == tbl['c1']:
        print 'nyert'
        vege = True
    else:
        return ""


def tabla_init():
    print tabla('I', '-')


tabla_init()
while (vege==False):
    tabla(bevitel(), j)
    ertekel()

