import random
caras=[[17,9,0,18,10,1,19,11,2],[0,1,2,3,4,5,6,7,8],[17,9,0,20,12,3,23,14,6],[23,14,6,24,15,7,25,16,8],[25,16,8,22,13,5,19,11,2],[17,18,19,20,21,22,23,24,25]]
prop=False

cuboprueba1=[0, 0, 0, 0, 0, 100000000, 0, 0, 0, 100000000, 0, 10000000, 0, 0, 10000000, 0, 10000000, 0, 0, 0, 0, 0, 100000000, 0, 0, 0]
cuboprueba2=[0, 0, 0, 0, 0, 0, 0, 0, 0, 10000000, 0, 0, 0, 0, 100000000, 0, 10000000, 0, 100000000, 0, 0, 0, 10000000, 0, 100000000, 0]
cuboprueba3=[0, 100000000, 0, 100000000, 0, 0, 0, 100000000, 0, 10000000, 0, 0, 0, 0, 0, 0, 10000000, 0, 0, 0, 0, 0, 10000000, 0, 0, 0]
cuboprueba4=[0, 100000000, 0, 0, 0, 100000000, 0, 0, 0, 10000000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100000000, 0, 10000000, 0, 10000000, 0]

def gen_base():
    cubo=[]
    for q in range(26):
        cubo.append(0)
    return cubo

def gen_aristas(cubo):
    aristas=[9,11,14,16,1,3,5,7,20,18,22,24]
    for j in range(3):
        for i in range(7,9):
            ran=random.randint(0,len(aristas)-1)
            cubo[aristas[ran]]=10**i
            aristas.pop(ran)

def gen_centros_y_verdes(cubo):
    cubo[0],cubo[25]=1,1
    cubo[4],cubo[10],cubo[12],cubo[13],cubo[15],cubo[21]=10,100,1000,10000,100000,1000000

def gen_final_aristas_y_vertices(cubo):
    vertices=[17,19,23,6,8,2]
    aristas=[]
    for k in range(1,7):
        ran=random.randint(0,len(vertices)-1)
        cubo[vertices[ran]]=10**k               
        vertices.pop(ran)
    for u in range(len(cubo)):
        if cubo[u]==0:
            aristas.append(u)
    for k in range(1,7):
        ran=random.randint(0,len(aristas)-1)
        cubo[aristas[ran]]=10**k
        aristas.pop(ran)

def cubu_gen(cubo,cara):
    cubu=0
    for h in range(9):
        cubu+=cubo[cara[h]]
    return cubu

def aristas_comprobation(cubo):
    cara=0
    while cara<6:
        #print(cubu_gen(cubo,caras[cara]))
        if cubu_gen(cubo,caras[cara])!=110000000:
            return False
        else:
            cara+=1
            #print(cubo)
        return True

def comprobation(cubo):
    cara=0
    while cara<4:
        #print(cubu_gen(cubo,caras[cara]))
        if cubu_gen(cubo,caras[cara])!=111111111:        
            return False
        else:
            cara+=1
            """
            if cara==2:
                for z in range(1000):
                    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
            if cara==3:
                for z in range(100000):
                    print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
                    print(cubo)
            print("##########################")
            """
    return True

def p():
    n=1
    prop=False
    while not prop:
        cube=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        gen_aristas(cube)
        if aristas_comprobation(cube):
            gen_centros_y_verdes(cube)
            gen_final_aristas_y_vertices(cube)
            #print(cube)
            if comprobation(cube):
                return cube
        
        n+=1
        if n%1000000==0:
            print(n)

def dame(cuantos):
    n=1
    prop=False
    listote=[]
    while not prop and len(listote)<cuantos*2:
        cube=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        gen_aristas(cube)
        if aristas_comprobation(cube):
            gen_centros_y_verdes(cube)
            gen_final_aristas_y_vertices(cube)
            #print(cube)
            if comprobation(cube):
                listote.append(cube)
        n+=1
        print(n,len(listote)//2)
    print(listote)
    for cubamen in listote:
        print(gg(cubamen))

def gg(cubo):
        cara=0
        while cara<6:
            #print(cubu_gen(cubo,caras[cara]))
            if cubu_gen(cubo,caras[cara])!=111111111:        
                return False
            else:
                cara+=1
        return True

"""
si joderrr
[1, 10000000, 1000, 100000, 10, 100, 10000, 100000000, 1000000, 1000000, 100, 100000000, 1000, 10000, 10000000, 100000, 10, 10, 10000, 100000, 100000000, 1000000, 10000000, 100, 1000, 1]
[1, 10000000, 10000, 100000, 10, 100000000, 100, 1000000, 1000, 100000000, 100, 1000, 1000, 10000, 10000, 100000, 10000000, 1000000, 10, 100000, 10000000, 1000000, 100, 10, 100000000, 1]
[1, 100000000, 1000, 100000, 10, 100, 1000000, 10000000, 10000, 10000, 100, 1000000, 1000, 10000, 100000000, 100000, 1000, 10, 10000000, 100000, 10000000, 1000000, 100000000, 100, 10, 1]
[1, 1000000, 1000, 100000000, 10, 100000, 10000, 10000000, 100, 10000000, 100, 100000000, 1000, 10000, 10, 100000, 100000000, 100000, 10000, 10, 100, 1000000, 10000000, 1000000, 1000, 1]
[1, 10000000, 100000, 100000000, 10, 100, 10000, 1000, 1000000, 1000000, 100, 10000, 1000, 10000, 10000000, 100000, 100000000, 10, 100000000, 1000, 100000, 1000000, 10000000, 100, 10, 1]
[1, 1000000, 1000, 100000, 10, 10000000, 100, 100000000, 10000, 10000, 100, 100000000, 1000, 10000, 10000000, 100000, 10, 10, 10000000, 100000, 100000000, 1000000, 100, 1000000, 1000, 1]
[1, 100000000, 1000, 100000, 10, 10000000, 10000, 1000000, 100, 10000000, 100, 10000, 1000, 10000, 100000000, 100000, 10000000, 1000000, 10, 100000, 100, 1000000, 100000000, 10, 1000, 1]

"""

"""        
def p_():
    n=1
    prop=False
    while not prop:
        #cuboprueba1=[0, 0, 0, 0, 0, 100000000, 0, 0, 0, 100000000, 0, 10000000, 0, 0, 10000000, 0, 10000000, 0, 0, 0, 0, 0, 100000000, 0, 0, 0]
        cuboprueba2=[0, 0, 0, 0, 0, 0, 0, 0, 0, 10000000, 0, 0, 0, 0, 100000000, 0, 10000000, 0, 100000000, 0, 0, 0, 10000000, 0, 100000000, 0]
        #cuboprueba3=[0, 100000000, 0, 100000000, 0, 0, 0, 100000000, 0, 10000000, 0, 0, 0, 0, 0, 0, 10000000, 0, 0, 0, 0, 0, 10000000, 0, 0, 0]
        #cuboprueba4=[0, 100000000, 0, 0, 0, 100000000, 0, 0, 0, 10000000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100000000, 0, 10000000, 0, 10000000, 0]
        cube=cuboprueba2
        gen_centros_y_verdes(cube)
        gen_final_aristas_y_vertices(cube)
        if comprobation(cube):
            print("wwwwwwwwwwwwwwwwwwwwwwwwwwwiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
            return cube
        n+=1
        print(n)
        
        
        print(n)
        print("***************************")
        print("**********",sum(cube)==333333332,"***********")
        print("***************************")
"""


def traductor(lista):
    """
    cubo[4],cubo[10],cubo[12],cubo[13],cubo[15],cubo[21]=10,100,1000,10000,100000,1000000
    """
    color=[]
    num=0
    for i in lista:
        num+=1
        if i==1:
            color.append((num,"verde"))
        if i==10:
            color.append((num,"azul_claro"))
        if i==100:
            color.append((num,"blanco"))
        if i==1000:
            color.append((num,"amarillo"))
        if i==10000:
            color.append((num,"naranja"))
        if i==100000:
            color.append((num,"negro"))
        if i==1000000:
            color.append((num,"azul_oscuro"))
        if i==10000000:
            color.append((num,"rosa"))
        if i==100000000:
            color.append((num,"rojo"))
    return color
            





