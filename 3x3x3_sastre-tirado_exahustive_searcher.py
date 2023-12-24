"""
Tma de Sastre-Tirado
"""

import random

def rotate(l, n):
    return l[-n:] + l[:-n]

cube=[["r","a","z"],["r","v","b"],["r","v","a"],["r","z","b"],["n","a","z"],["n","v","b"],["n","v","a"],["n","z","b"]]

def ran(ite):
    for i in range(ite):
        print(12*10**6 - i)
        quedan=[["r","a","z"],["r","v","b"],["r","v","a"],["r","z","b"],["n","a","z"],["n","v","b"],["n","v","a"],["n","z","b"]]
        new=[[],[],[],[],[],[],[],[]]
        n=7
        for j in range(8):
            a=random.randint(0,n)
            b=random.randint(0,2)
            new[j]=rotate(quedan[a],b)
            quedan.pop(a)
            n-=1
        new.insert(0,0)
        caras=[[],[],[],[],[],[]]
        caras[0]=[new[1][2],new[2][2],new[3][2],new[4][2]]
        caras[1]=[new[1][0],new[2][1],new[5][0],new[6][1]]
        caras[2]=[new[2][0],new[3][1],new[6][0],new[7][1]]
        caras[3]=[new[3][0],new[4][1],new[7][0],new[8][1]]
        caras[4]=[new[4][0],new[1][1],new[8][0],new[5][1]]
        caras[5]=[new[5][2],new[6][2],new[7][2],new[8][2]]
        wena=True
        for k in range(5):
            if caras[k]!=list(set(caras[k])):
                wena=False
                break
        if wena:
            print("*****************************************   EUREKA   **************************************")
            print(new)
            print(caras)
            return(new, caras)

ran(12*10**6)




