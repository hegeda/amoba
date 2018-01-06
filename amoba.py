# coding=utf-8
import os

clear = lambda: os.system('clear')
j = 'X'
tbl = {'a1': "", 'a2': "", 'a3': "", 'b1': "", 'b2': "", 'b3': "", 'c1': "", 'c2': "", 'c3': ""}
vege=False


def tabla(mezo, ertek):
    clear()
    print ('Amőba játék')
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


def valtas():
    global j
    if j == 'X':
        j = 'O'
        print'O jön'
    else:
        j = 'X'
        print'X jön'
    return ""


def bevitel():
    bev = raw_input("Koordináták (pl.: a2): ")
    return bev


def ertekel():
    global vege
    if tbl['a1'] <> '-' and tbl['a1'] == tbl['a2'] == tbl['a3']:
        print 'nyert'
        vege = True
    elif tbl['b1'] <> '-' and tbl['b1'] == tbl['b2'] == tbl['b3']:
        print 'nyert'
        vege = True
    elif tbl['c1'] <> '-' and tbl['c1'] == tbl['c2'] == tbl['c3']:
        print 'nyert'
        vege = True
    elif tbl['a1'] <> '-' and tbl['a1'] == tbl['b1'] == tbl['c1']:
        print 'nyert'
        vege = True
    elif tbl['a2'] <> '-' and tbl['a2'] == tbl['b2'] == tbl['c2']:
        print 'nyert'
        vege = True
    elif tbl['a3'] <> '-' and tbl['a3'] == tbl['b3'] == tbl['c3']:
        print 'nyert'
        vege = True
    elif tbl['a1'] <> '-' and tbl['a1'] == tbl['b2'] == tbl['c3']:
        print 'nyert'
        vege = True
    elif tbl['a3'] <> '-' and tbl['a3'] == tbl['b2'] == tbl['c1']:
        print 'nyert'
        vege = True
    else:
        valtas()

        return ""



def tabla_init():
    tabla('I', '-')
    vege=False


tabla_init()
while vege==False:
    tabla(bevitel(), j)
    ertekel()


