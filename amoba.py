# coding=utf-8
import os

clear = lambda: os.system('clear')
j = 'X'
tbl = {'a1': "", 'a2': "", 'a3': "", 'b1': "", 'b2': "", 'b3': "", 'c1': "", 'c2': "", 'c3': ""}
vege = False
nevalt = False
lep = 0


def tabla(mezo, ertek):
    global nevalt
    clear()
    print ('Amőba játék')
    if mezo == 'I':
        ertek = "-"
        for i in tbl.iterkeys():
            tbl[i] = ertek
    elif mezo == 'a1' and tbl['a1'] == "-":
        tbl['a1'] = ertek
    elif mezo == 'a2' and tbl['a2'] == "-":
        tbl['a2'] = ertek
    elif mezo == 'a3' and tbl['a3'] == "-":
        tbl['a3'] = ertek
    elif mezo == 'b1' and tbl['b1'] == "-":
        tbl['b1'] = ertek
    elif mezo == 'b2' and tbl['b2'] == "-":
        tbl['b2'] = ertek
    elif mezo == 'b3' and tbl['b3'] == "-":
        tbl['b3'] = ertek
    elif mezo == 'c1' and tbl['c1'] == "-":
        tbl['c1'] = ertek
    elif mezo == 'c2' and tbl['c2'] == "-":
        tbl['c2'] = ertek
    elif mezo == 'c3' and tbl['c3'] == "-":
        tbl['c3'] = ertek
    else:
        print 'Érvénytelen koordináta! Adj újat!'
        nevalt = True
    print '     1   2   3'
    print 'a   ', tbl['a1'], '|', tbl['a2'], '|', tbl['a3']
    print 'b   ', tbl['b1'], '|', tbl['b2'], '|', tbl['b3']
    print 'c   ', tbl['c1'], '|', tbl['c2'], '|', tbl['c3']
    print '\n'
    return ""


def valtas():
    global j
    global nevalt
    global lep
    if nevalt:
        print j, ' jön'
        nevalt = False
        return ""
    else:
        if j == 'X':
            j = 'O'
            print j, ' jön'
            lep += 1
        else:
            j = 'X'
            print j, ' jön'
            lep += 1
    return ""


def bevitel():
    bev = raw_input("Koordináták (pl.: a2, újra: r ): ")
    return bev


def ertekel():
    global vege
    global lep
    if tbl['a1'] <> '-' and tbl['a1'] == tbl['a2'] == tbl['a3']:
        print 'Nyert', j
        ujra()
    elif tbl['b1'] <> '-' and tbl['b1'] == tbl['b2'] == tbl['b3']:
        print 'Nyert', j
        ujra()
    elif tbl['c1'] <> '-' and tbl['c1'] == tbl['c2'] == tbl['c3']:
        print 'Nyert', j
        ujra()
    elif tbl['a1'] <> '-' and tbl['a1'] == tbl['b1'] == tbl['c1']:
        print 'Nyert', j
        ujra()
    elif tbl['a2'] <> '-' and tbl['a2'] == tbl['b2'] == tbl['c2']:
        print 'Nyert', j
        ujra()
    elif tbl['a3'] <> '-' and tbl['a3'] == tbl['b3'] == tbl['c3']:
        print 'Nyert', j
        ujra()
    elif tbl['a1'] <> '-' and tbl['a1'] == tbl['b2'] == tbl['c3']:
        print 'Nyert', j
        ujra()
    elif tbl['a3'] <> '-' and tbl['a3'] == tbl['b2'] == tbl['c1']:
        print 'Nyert', j
        ujra()
    elif lep == 8:
        print 'Döntetlen'
        ujra()
    else:
        valtas()
        return False


def ujra():
    global vege
    re = raw_input("Új játék?: (i/n)")
    if re == 'i':
        tabla_init()
    else:
        vege = True


def tabla_init():
    global lep
    global vege
    tabla('I', '-')
    lep = 0
    vege = False


tabla_init()
while vege == False:
    tabla(bevitel(), j)
    ertekel()
