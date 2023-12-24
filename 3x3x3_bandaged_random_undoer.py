import random

solvedcube = [["y","y","y","y","y","y","y","y","y","r","r","r","b","b","b","p","p","p","g","g","g", \
"r","r","r","b","b","b","p","p","p","g","g","g","r","r","r","b","b","b","p","p","p","g","g","g", \
"w","w","w","w","w","w","w","w","w"],
[[0, 1],
 [2, 5],
 [3, 4],
 [6, 7],
 [9, 10],
 [12, 13],
 [16, 17],
 [21, 33],
 [22, 34],
 [24, 25],
 [26, 33],
 [27, 39],
 [28, 40],
 [29, 41],
 [30, 42],
 [31, 43],
 [32, 44],
 [49, 52],
 [50, 53]]]

def ispossibleU(cube):
    for ligadura in [[9, 21],[10, 22],[11, 23],[12, 24],[13, 25],[14, 26],[15, 27],[16, 28],[17, 31],[18, 30],[19, 31]]:
        if ligadura in cube[1]:
            return False
    return True

def U(cube):
    if not ispossibleU(cube):
        print("U IS BLOCKED")
        return None
    #print(cube[0])
    #print(cube[1])
    #print("-------------------------------------------")
    cube[0][0],cube[0][1],cube[0][2],cube[0][3],cube[0][5],cube[0][6],cube[0][7],cube[0][8],\
    cube[0][9], cube[0][10],cube[0][11],cube[0][12],cube[0][13],cube[0][14],cube[0][15],cube[0][16],cube[0][17],cube[0][18],cube[0][19],cube[0][20]= \
    cube[0][6],cube[0][3],cube[0][0],cube[0][7],cube[0][1],cube[0][8],cube[0][5],cube[0][2],\
    cube[0][18],cube[0][19],cube[0][20],cube[0][9],cube[0][10],cube[0][11],cube[0][12],cube[0][13],cube[0][14],cube[0][15],cube[0][16],cube[0][17]
    i=0
    while i<=3:
        to_change=True
        if cube[1][i]==[0,1] and to_change:
            cube[1][i]=[2,5]
            to_change=False
        if cube[1][i]==[0,3] and to_change:
            cube[1][i]=[1,2]
            to_change=False
        if cube[1][i]==[1,2] and to_change:
            cube[1][i]=[5,8]
            to_change=False
        if cube[1][i]==[1,4] and to_change:
            cube[1][i]=[4,5]
            to_change=False
        if cube[1][i]==[2,5] and to_change:
            cube[1][i]=[7,8]
            to_change=False
        if cube[1][i]==[3,4] and to_change:
            cube[1][i]=[1,4]
            to_change=False
        if cube[1][i]==[3,6] and to_change:
            cube[1][i]=[0,1]
            to_change=False
        if cube[1][i]==[4,5] and to_change:
            cube[1][i]=[4,7]
            to_change=False
        if cube[1][i]==[4,7] and to_change:
            cube[1][i]=[3,6]
            to_change=False
        if cube[1][i]==[5,8] and to_change:
            cube[1][i]=[6,7]
            to_change=False
        if cube[1][i]==[6,7] and to_change:
            cube[1][i]=[0,3]
            to_change=False
        if cube[1][i]==[7,8] and to_change:
            cube[1][i]=[3,6]
        i+=1
    #print(cube[0])
    #print(cube[1])
    #print("--------------------------------------------")
    return cube

def U2(cube):
    cube=U(cube)
    cube=U(cube)
    return cube

def U_(cube):
    cube=U(cube)
    cube=U(cube)
    cube=U(cube)
    return cube

def ispossibleB(cube):
    for ligadura in [[2, 5],
 [1, 4],
 [0, 3],
 [19, 20],
 [31, 32],
 [43, 44],
 [45, 48],
 [46, 49],
 [47, 50],
 [36, 37],
 [24, 25],
 [12, 13]]:
        if ligadura in cube[1]:
            return False
    return True

def B(cube):
    if not ispossibleU(cube):
        print("B IS BLOCKED")
        return None
    #print(cube[0])
    #print(cube[1])
    #print("-------------------------------------------")
    cube[0][11],cube[0][10],cube[0][9],cube[0][23],cube[0][21],cube[0][35],cube[0][34],cube[0][33],\
    cube[0][2], cube[0][1],cube[0][0],cube[0][20],cube[0][32],cube[0][44],cube[0][45],cube[0][46],cube[0][47],cube[0][36],cube[0][24],cube[0][12]= \
    cube[0][9],cube[0][21],cube[0][33],cube[0][10],cube[0][34],cube[0][11],cube[0][23],cube[0][35],\
    cube[0][36],cube[0][24],cube[0][12],cube[0][2],cube[0][1],cube[0][0],cube[0][20],cube[0][32],cube[0][44],cube[0][45],cube[0][46],cube[0][47]
    i=0
    while i<=3:
        to_change=True
        if cube[1][i]==[11,10] and to_change:
            cube[1][i]=[9,21]
            to_change=False
        if cube[1][i]==[11,23] and to_change:
            cube[1][i]=[9,10]
            to_change=False
        if cube[1][i]==[10,9] and to_change:
            cube[1][i]=[21,33]
            to_change=False
        if cube[1][i]==[10,22] and to_change:
            cube[1][i]=[21,22]
            to_change=False
        if cube[1][i]==[9,21] and to_change:
            cube[1][i]=[33,34]
            to_change=False
        if cube[1][i]==[22,23] and to_change:
            cube[1][i]=[10,22]
            to_change=False
        if cube[1][i]==[23,35] and to_change:
            cube[1][i]=[10,11]
            to_change=False
        if cube[1][i]==[21,22] and to_change:
            cube[1][i]=[22,34]
            to_change=False
        if cube[1][i]==[22,34] and to_change:
            cube[1][i]=[22,23]
            to_change=False
        if cube[1][i]==[21,33] and to_change:
            cube[1][i]=[34,35]
            to_change=False
        if cube[1][i]==[34,35] and to_change:
            cube[1][i]=[11,23]
            to_change=False
        if cube[1][i]==[33,34] and to_change:
            cube[1][i]=[23,35]
        i+=1
    #print(cube[0])
    #print(cube[1])
    #print("--------------------------------------------")
    return cube

def B2(cube):
    cube=B(cube)
    cube=B(cube)
    return cube

def B_(cube):
    cube=B(cube)
    cube=B(cube)
    cube=B(cube)
    return cube

def ispossibleF(cube):
    for ligadura in [[3,6],[4,7],[5,8],[13,14],[25,26],[37,38],[50,53],[49,52],[48,51],[42,43],[30,31],[18,19]]:
        if ligadura in cube[1]:
            return False
    return True

def F(cube):
    if not ispossibleF(cube):
        print("F IS BLOCKED")
        return None
    #print(cube[0])
    #print(cube[1])
    #print("-------------------------------------------")
    cube[0][17],cube[0][16],cube[0][15],cube[0][29],cube[0][27],cube[0][41],cube[0][40],cube[0][39],\
    cube[0][6], cube[0][7],cube[0][8],cube[0][14],cube[0][26],cube[0][38],cube[0][53],cube[0][52],cube[0][51],cube[0][42],cube[0][30],cube[0][18]= \
    cube[0][41],cube[0][29],cube[0][17],cube[0][40],cube[0][16],cube[0][39],cube[0][27],cube[0][15],\
    cube[0][42],cube[0][30],cube[0][18],cube[0][6],cube[0][7],cube[0][8],cube[0][14],cube[0][26],cube[0][38],cube[0][53],cube[0][52],cube[0][51]
    i=0
    while i<=3:
        to_change=True
        if cube[1][i]==[16,17] and to_change:
            cube[1][i]=[15,27]
            to_change=False
        if cube[1][i]==[17,29] and to_change:
            cube[1][i]=[15,16]
            to_change=False
        if cube[1][i]==[15,16] and to_change:
            cube[1][i]=[27,39]
            to_change=False
        if cube[1][i]==[16,28] and to_change:
            cube[1][i]=[27,28]
            to_change=False
        if cube[1][i]==[15,27] and to_change:
            cube[1][i]=[39,40]
            to_change=False
        if cube[1][i]==[28,29] and to_change:
            cube[1][i]=[16,28]
            to_change=False
        if cube[1][i]==[29,41] and to_change:
            cube[1][i]=[16,17]
            to_change=False
        if cube[1][i]==[27,28] and to_change:
            cube[1][i]=[28,40]
            to_change=False
        if cube[1][i]==[28,40] and to_change:
            cube[1][i]=[29,41]
            to_change=False
        if cube[1][i]==[27,39] and to_change:
            cube[1][i]=[40,41]
            to_change=False
        if cube[1][i]==[40,41] and to_change:
            cube[1][i]=[17,29]
            to_change=False
        if cube[1][i]==[39,40] and to_change:
            cube[1][i]=[29,41]
        i+=1
    #print(cube[0])
    #print(cube[1])
    #print("--------------------------------------------")
    return cube

def F2(cube):
    cube=F(cube)
    cube=F(cube)
    return cube

def F_(cube):
    cube=F(cube)
    cube=F(cube)
    cube=F(cube)
    return cube

def ispossibleR(cube):
    for ligadura in [[7,8],[4,5],[1,2],[10,11],[22,23],[33,34],[46,47],[49,50],[52,53],[39,40],[27,28],[15,16]]:
        if ligadura in cube[1]:
            return False
    return True

def R(cube):
    if not ispossibleR(cube):
        print("R IS BLOCKED")
        return None
    #print(cube[0])
    #print(cube[1])
    #print("-------------------------------------------")
    cube[0][14],cube[0][13],cube[0][12],cube[0][26],cube[0][24],cube[0][38],cube[0][37],cube[0][36],\
    cube[0][8], cube[0][5],cube[0][2],cube[0][11],cube[0][23],cube[0][35],cube[0][47],cube[0][50],cube[0][53],cube[0][39],cube[0][27],cube[0][15]= \
    cube[0][41],cube[0][29],cube[0][17],cube[0][40],cube[0][16],cube[0][39],cube[0][27],cube[0][15],\
    cube[0][39],cube[0][27],cube[0][15],cube[0][8],cube[0][5],cube[0][2],cube[0][11],cube[0][23],cube[0][35],cube[0][47],cube[0][50],cube[0][53]
    i=0
    while i<=3:
        to_change=True
        if cube[1][i]==[13,14] and to_change:
            cube[1][i]=[12,24]
            to_change=False
        if cube[1][i]==[14,26] and to_change:
            cube[1][i]=[12,13]
            to_change=False
        if cube[1][i]==[12,13] and to_change:
            cube[1][i]=[24,36]
            to_change=False
        if cube[1][i]==[13,25] and to_change:
            cube[1][i]=[24,25]
            to_change=False
        if cube[1][i]==[24,25] and to_change:
            cube[1][i]=[25,37]
            to_change=False
        if cube[1][i]==[24,36] and to_change:
            cube[1][i]=[37,38]
            to_change=False
        if cube[1][i]==[36,37] and to_change:
            cube[1][i]=[26,38]
            to_change=False
        if cube[1][i]==[37,38] and to_change:
            cube[1][i]=[14,26]
            to_change=False
        if cube[1][i]==[26,38] and to_change:
            cube[1][i]=[13,14]
            to_change=False
        if cube[1][i]==[25,37] and to_change:
            cube[1][i]=[25,26]
            to_change=False
        if cube[1][i]==[25,26] and to_change:
            cube[1][i]=[13,25]
            to_change=False
        if cube[1][i]==[12,24] and to_change:
            cube[1][i]=[36,37]
        i+=1
    #print(cube[0])
    #print(cube[1])
    #print("--------------------------------------------")
    return cube

def R2(cube):
    cube=R(cube)
    cube=R(cube)
    return cube

def R_(cube):
    cube=R(cube)
    cube=R(cube)
    cube=R(cube)
    return cube

def ispossibleL(cube):
    for ligadura in [[0,1],[3,4],[6,7],[16,17],[28,29],[40,41],[51,52],[48,49],[45,46],[33,39],[21,22],[9,10]]:
        if ligadura in cube[1]:
            return False
    return True

def L(cube):
    if not ispossibleL(cube):
        print("L IS BLOCKED")
        return None
    #print(cube[0])
    #print(cube[1])
    #print("-------------------------------------------")
    cube[0][20],cube[0][19],cube[0][18],cube[0][32],cube[0][30],cube[0][44],cube[0][43],cube[0][42],\
    cube[0][0], cube[0][3],cube[0][6],cube[0][17],cube[0][29],cube[0][41],cube[0][51],cube[0][48],cube[0][45],cube[0][33],cube[0][21],cube[0][9]= \
    cube[0][44],cube[0][32],cube[0][20],cube[0][43],cube[0][19],cube[0][42],cube[0][30],cube[0][18],\
    cube[0][33],cube[0][21],cube[0][9],cube[0][0], cube[0][3],cube[0][6],cube[0][17],cube[0][29],cube[0][41],cube[0][51],cube[0][48],cube[0][45]
    i=0
    while i<=3:
        to_change=True
        if cube[1][i]==[19,20] and to_change:
            cube[1][i]=[18,30]
            to_change=False
        if cube[1][i]==[18,19] and to_change:
            cube[1][i]=[30,42]
            to_change=False
        if cube[1][i]==[18,30] and to_change:
            cube[1][i]=[42,43]
            to_change=False
        if cube[1][i]==[30,42] and to_change:
            cube[1][i]=[43,44]
            to_change=False
        if cube[1][i]==[43,44] and to_change:
            cube[1][i]=[20,32]
            to_change=False
        if cube[1][i]==[32,44] and to_change:
            cube[1][i]=[19,20]
            to_change=False
        if cube[1][i]==[20,32] and to_change:
            cube[1][i]=[18,19]
            to_change=False
        if cube[1][i]==[19,31] and to_change:
            cube[1][i]=[30,31]
            to_change=False
        if cube[1][i]==[30,31] and to_change:
            cube[1][i]=[31,43]
            to_change=False
        if cube[1][i]==[31,43] and to_change:
            cube[1][i]=[31,32]
            to_change=False
        if cube[1][i]==[31,32] and to_change:
            cube[1][i]=[19,31]
            to_change=False
        if cube[1][i]==[42,43] and to_change:
            cube[1][i]=[32,44]
        i+=1
    #print(cube[0])
    #print(cube[1])
    #print("--------------------------------------------")
    return cube

def L2(cube):
    cube=R(cube)
    cube=R(cube)
    return cube

def L_(cube):
    cube=R(cube)
    cube=R(cube)
    cube=R(cube)
    return cube

def ispossibleD(cube):
    for ligadura in [[23,35],[22,34],[21,33],[32,44],[31,43],[30,42],[29,41],[28,40],[27,39],[26,38],[25,37],[24,36]]:
        if ligadura in cube[1]:
            return False
    return True

def D(cube):
    if not ispossibleD(cube):
        print("D IS BLOCKED")
        return None
    #print(cube[0])
    #print(cube[1])
    #print("-------------------------------------------")
    cube[0][47],cube[0][46],cube[0][45],cube[0][50],cube[0][48],cube[0][53],cube[0][52],cube[0][51],\
    cube[0][35], cube[0][34],cube[0][33],cube[0][44],cube[0][43],cube[0][42],cube[0][41],cube[0][40],cube[0][39],cube[0][38],cube[0][37],cube[0][36]= \
    cube[0][53],cube[0][50],cube[0][47],cube[0][52],cube[0][46],cube[0][51],cube[0][48],cube[0][45],\
    cube[0][38],cube[0][37],cube[0][36],cube[0][35], cube[0][34],cube[0][33],cube[0][44],cube[0][43],cube[0][42],cube[0][41],cube[0][40],cube[0][39]
    i=0
    while i<=3:
        to_change=True
        if cube[1][i]==[46,47] and to_change:
            cube[1][i]=[45,48]
            to_change=False
        if cube[1][i]==[45,46] and to_change:
            cube[1][i]=[48,51]
            to_change=False
        if cube[1][i]==[45,48] and to_change:
            cube[1][i]=[51,52]
            to_change=False
        if cube[1][i]==[48,51] and to_change:
            cube[1][i]=[52,53]
            to_change=False
        if cube[1][i]==[51,52] and to_change:
            cube[1][i]=[50,53]
            to_change=False
        if cube[1][i]==[52,53] and to_change:
            cube[1][i]=[47,50]
            to_change=False
        if cube[1][i]==[50,53] and to_change:
            cube[1][i]=[46,47]
            to_change=False
        if cube[1][i]==[46,49] and to_change:
            cube[1][i]=[48,49]
            to_change=False
        if cube[1][i]==[48,49] and to_change:
            cube[1][i]=[49,52]
            to_change=False
        if cube[1][i]==[49,52] and to_change:
            cube[1][i]=[49,50]
            to_change=False
        if cube[1][i]==[49,50] and to_change:
            cube[1][i]=[46,49]
            to_change=False
        if cube[1][i]==[47,50] and to_change:
            cube[1][i]=[45,46]
        i+=1
    #print(cube[0])
    #print(cube[1])
    #print("--------------------------------------------")
    return cube

def D2(cube):
    cube=R(cube)
    cube=R(cube)
    return cube

def D_(cube):
    cube=R(cube)
    cube=R(cube)
    cube=R(cube)
    return cube

def posibles(cube):
    result=[]
    if ispossibleU(cube):
        result.append((U(cube),"U"))
        #result.append(U2(cube))
        result.append((U_(cube),"U_"))
    if ispossibleD(cube):
        result.append((D(cube),"D"))
        #result.append(D2(cube))
        result.append((D_(cube),"D_"))
    if ispossibleF(cube):
        result.append((F(cube),"F"))
        #result.append(F2(cube))
        result.append((F_(cube),"F_"))
    if ispossibleB(cube):
        result.append((B(cube),"B"))
        #result.append(B2(cube))
        result.append((B_(cube),"B_"))
    if ispossibleR(cube):
        result.append((R(cube),"R"))
        #result.append(R2(cube))
        result.append((R_(cube),"R_"))
    if ispossibleL(cube):
        result.append((L(cube),"L"))
        #result.append(L2(cube))
        result.append((L_(cube),"L_"))
    return result
    

def deshazmelo(movimientos,cube):
    lst=[]
    for i in range(movimientos):
        a=random.randint(0,len(posibles(cube))-1)
        cube=posibles(cube)[a][0]
        lst.append(posibles(cube)[a][1])
    print(lst)
    return cube
        












