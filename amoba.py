#!/usr/bin/env python3
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
    global lep
    clear()
    print ('Amőba játék')
    if mezo == 'I':
        ertek = "-"
        for i in tbl.keys():
            tbl[i] = ertek
    elif mezo == 'k':
        quit()
    elif mezo in tbl and tbl[mezo] == "-":
        tbl[mezo] = ertek
        lep += 1
    else:
        print('Érvénytelen koordináta! Adj újat!')
        nevalt = True
    print('     1   2   3')
    print('a   ', tbl['a1'], '|', tbl['a2'], '|', tbl['a3'])
    print('b   ', tbl['b1'], '|', tbl['b2'], '|', tbl['b3'])
    print('c   ', tbl['c1'], '|', tbl['c2'], '|', tbl['c3'])
    print('\n')
    return ""


def valtas():
    global j
    global nevalt
    if nevalt:
        print(j, ' jön')
        nevalt = False
        return ""
    else:
        if j == 'X':
            j = 'O'
            print(j, ' jön')
        else:
            j = 'X'
            print(j, ' jön')
    return ""


def bevitel():
    bev = input("Koordináták (pl.: a2, k: kilép): ")
    return bev


def ertekel():
    global vege
    global lep
    if tbl['a1'] != '-' and tbl['a1'] == tbl['a2'] == tbl['a3']:
        print('Nyert', j)
        ujra()
    elif tbl['b1'] != '-' and tbl['b1'] == tbl['b2'] == tbl['b3']:
        print('Nyert', j)
        ujra()
    elif tbl['c1'] != '-' and tbl['c1'] == tbl['c2'] == tbl['c3']:
        print('Nyert', j)
        ujra()
    elif tbl['a1'] != '-' and tbl['a1'] == tbl['b1'] == tbl['c1']:
        print('Nyert', j)
        ujra()
    elif tbl['a2'] != '-' and tbl['a2'] == tbl['b2'] == tbl['c2']:
        print('Nyert', j)
        ujra()
    elif tbl['a3'] != '-' and tbl['a3'] == tbl['b3'] == tbl['c3']:
        print('Nyert', j)
        ujra()
    elif tbl['a1'] != '-' and tbl['a1'] == tbl['b2'] == tbl['c3']:
        print('Nyert', j)
        ujra()
    elif tbl['a3'] != '-' and tbl['a3'] == tbl['b2'] == tbl['c1']:
        print('Nyert', j)
        ujra()
    elif lep == 9:
        print('Döntetlen')
        ujra()
    else:
        valtas()
        return False


def ujra():
    global vege
    re = input("Új játék?: (i/n)")
    if re == 'i':
        tabla_init()
    else:
        vege = True


def tabla_init():
    global j
    global lep
    global vege
    global nevalt
    tabla('I', '-')
    j = 'X'
    lep = 0
    vege = False
    nevalt = False


tabla_init()
print('X kezd')
while not vege:
    tabla(bevitel(), j)
    ertekel()
