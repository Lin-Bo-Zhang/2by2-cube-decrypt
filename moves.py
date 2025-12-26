'''
程式.二階魔術方塊破解器.moves 的 Docstring
本程式用於存放重複類似的魔術方塊轉動函式，以便 main.py 調用。
'''
# 轉動代號和函式對照 
# R=R0 R'=R1 L=L0 L'=L1 U=U0 U'=U1 D=D0 D'=D1 F=F0 F'=F1 B=B0 B'=B1
import numpy as np
l = np.array([0,1,2,3,4,5,6,7])
o = np.array([0,0,0,0,0,0,0,0])


def R0(l,o):  #R
    a=[3,0,4,7]
    l[[0,4,7,3]]=l[a]
    o[[0,4,7,3]]=o[a]
    for idx in a:
        if o[[idx]] == 0:
            o[[idx]]=o[[idx]]+1
        elif o[[idx]] == 1:
            o[[idx]]=o[[idx]]-1
    return l,o

def R1(l,o):  #R'
    a=[4,7,3,0]
    l[[0,4,7,3]]=l[a]
    o[[0,4,7,3]]=o[a]
    for idx in a:
        if o[[idx]] == 0:
            o[[idx]]=o[[idx]]+1
        elif o[[idx]] == 1:
            o[[idx]]=o[[idx]]-1
    return l,o


def L0(l,o): #L
    a=[5,6,2,1]
    l[[1,5,6,2]]=l[a]
    o[[1,5,6,2]]=o[a]
    for idx in a:
        if o[[idx]] == 0:
            o[[idx]]=o[[idx]]+1
        elif o[[idx]] == 1:
            o[[idx]]=o[[idx]]-1
    return l,o

def L1(l,o): #L'
    a=[2,1,5,6]
    l[[1,5,6,2]]=l[a]
    o[[1,5,6,2]]=o[a]
    for idx in a:
        if o[[idx]] == 0:
            o[[idx]]=o[[idx]]+1
        elif o[[idx]] == 1:
            o[[idx]]=o[[idx]]-1
    return l,o

def U0(l,o): #U
    a=[7,4,5,6]
    l[[4,5,6,7]]=l[a]
    o[[4,5,6,7]]=o[a]
    for idx in a:
        if o[[idx]] == 1:
            o[[idx]]=o[[idx]]+1
        elif o[[idx]] == 2:
            o[[idx]]=o[[idx]]-1
    return l,o

def U1(l,o): #U'
    a=[5,6,7,4]
    l[[4,5,6,7]]=l[a]
    o[[4,5,6,7]]=o[a]
    for idx in a:
        if o[[idx]] == 1:
            o[[idx]]=o[[idx]]+1
        elif o[[idx]] == 2:
            o[[idx]]=o[[idx]]-1
    return l,o

def D0(l,o):#D
    a=[1,2,3,0]
    l[[0,1,2,3]]=l[a]
    o[[0,1,2,3]]=o[a]
    for idx in a:
        if o[[idx]] == 1:
            o[[idx]]=o[[idx]]+1
        elif o[[idx]] == 2:
            o[[idx]]=o[[idx]]-1
    return l,o

def D1(l,o):#D'
    a=[3,0,1,2]
    l[[0,1,2,3]]=l[a]
    o[[0,1,2,3]]=o[a]
    for idx in a:
        if o[[idx]] == 1:
            o[[idx]]=o[[idx]]+1
        elif o[[idx]] == 2:
            o[[idx]]=o[[idx]]-1
    return l,o

def F0(l,o):#F
    a=[4,0,1,5]
    l[[0,1,5,4]]=l[a]
    o[[0,1,5,4]]=o[a]
    for idx in a:
        if o[[idx]] == 0:
            o[[idx]]=o[[idx]]+2
        elif o[[idx]] == 2:
            o[[idx]]=o[[idx]]-2
    return l,o

def F1(l,o):#F'
    a=[1,5,4,0]
    l[[0,1,5,4]]=l[a]
    o[[0,1,5,4]]=o[a]
    for idx in a:
        if o[[idx]] == 0:
            o[[idx]]=o[[idx]]+2
        elif o[[idx]] == 2:
            o[[idx]]=o[[idx]]-2
    return l,o

def B0(l,o):#B
    a=[6,2,3,7]
    l[[2,3,7,6]]=l[a]
    o[[2,3,7,6]]=o[a]
    for idx in a:
        if o[[idx]] == 0:
            o[[idx]]=o[[idx]]+2
        elif o[[idx]] == 2:
            o[[idx]]=o[[idx]]-2
    return l,o

def B1(l,o):#B'
    a=[3,7,6,2]
    l[[2,3,7,6]]=l[a]
    o[[2,3,7,6]]=o[a]
    for idx in a:
        if o[[idx]] == 0:
            o[[idx]]=o[[idx]]+2
        elif o[[idx]] == 2:
            o[[idx]]=o[[idx]]-2
    return l,o

def N(l,o):#不動作(佔位用)
    return l,o

def R2(l,o):#R2
    R0(l,o)
    R0(l,o)
    return l,o
def U2(l,o):#U2
    U0(l,o)
    U0(l,o)
    return l,o
def F2(l,o):#F2
    F0(l,o)
    F0(l,o)
    return l,o
def L2(l,o):#L2
    L0(l,o)
    L0(l,o)
    return l,o
def D2(l,o):#D2
    D0(l,o)
    D0(l,o)
    return l,o
def B2(l,o):#B2
    B0(l,o)
    B0(l,o)
    return l,o
def f(l,o,a):#執行列表動作
    for i in a:
        i(l,o)
    return l,o
if __name__=="__main__":
    print('What are you doing?')
