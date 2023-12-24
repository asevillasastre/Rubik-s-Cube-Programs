import random

solvedcube=["wrb","wb","wbo","wo","wog","wg","wgr","wr","ybr","yr","yrg","yg","ygo","yo","yob","yb"]
initialcube=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

def U(cube):
    cube[0],cube[1],cube[2],cube[3],cube[4],cube[5],cube[6],cube[7]=cube[2],cube[3],cube[4],cube[5],cube[6],cube[7],cube[0],cube[1]
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

def D(cube):
    cube[0+8],cube[1+8],cube[2+8],cube[3+8],cube[4+8],cube[8+5],cube[8+6],cube[8+7]=cube[8+2],cube[8+3],cube[8+4],cube[8+5],cube[8+6],cube[8+7],cube[8+0],cube[8+1]
    return cube

def D2(cube):
    cube=D(cube)
    cube=D(cube)
    
    return cube

def D_(cube):
    cube=D(cube)
    cube=D(cube)
    cube=D(cube)
    return cube

def anti180antiup1(cube):
    cube[0],cube[1],cube[2],cube[3],cube[4],cube[5],cube[6],cube[7],cube[8+0],cube[8+1],cube[8+2],cube[8+3],cube[8+4],cube[8+5],cube[8+6],cube[8+7] =\
    cube[2],cube[3],cube[10],cube[11],cube[4],cube[5],cube[6],cube[7],cube[8],cube[9],cube[12],cube[13],cube[0],cube[1],cube[14],cube[15]
    return cube

def anti180antiup2(cube):
    cube[0],cube[1],cube[2],cube[3],cube[4],cube[5],cube[6],cube[7],cube[8+0],cube[8+1],cube[8+2],cube[8+3],cube[8+4],cube[8+5],cube[8+6],cube[8+7] =\
    cube[10],cube[11],cube[12],cube[13],cube[4],cube[5],cube[6],cube[7],cube[8],cube[9],cube[0],cube[1],cube[2],cube[3],cube[14],cube[15]
    return cube

def anti180antiup3(cube):
    cube[0],cube[1],cube[2],cube[3],cube[4],cube[5],cube[6],cube[7],cube[8+0],cube[8+1],cube[8+2],cube[8+3],cube[8+4],cube[8+5],cube[8+6],cube[8+7] =\
    cube[12],cube[13],cube[0],cube[1],cube[4],cube[5],cube[6],cube[7],cube[8],cube[9],cube[2],cube[3],cube[10],cube[11],cube[14],cube[15]
    return cube

def anti180antidown1(cube):
    cube[0],cube[1],cube[2],cube[3],cube[4],cube[5],cube[6],cube[7],cube[8+0],cube[8+1],cube[8+2],cube[8+3],cube[8+4],cube[8+5],cube[8+6],cube[8+7] =\
    cube[0],cube[1],cube[2],cube[3],cube[8],cube[9],cube[4],cube[5],cube[14],cube[15],cube[10],cube[11],cube[12],cube[13],cube[6],cube[7]
    return cube

def anti180antidown2(cube):
    cube[0],cube[1],cube[2],cube[3],cube[4],cube[5],cube[6],cube[7],cube[8+0],cube[8+1],cube[8+2],cube[8+3],cube[8+4],cube[8+5],cube[8+6],cube[8+7] =\
    cube[0],cube[1],cube[2],cube[3],cube[14],cube[15],cube[8],cube[9],cube[6],cube[7],cube[10],cube[11],cube[12],cube[13],cube[4],cube[5]
    return cube

def anti180antidown3(cube):
    cube[0],cube[1],cube[2],cube[3],cube[4],cube[5],cube[6],cube[7],cube[8+0],cube[8+1],cube[8+2],cube[8+3],cube[8+4],cube[8+5],cube[8+6],cube[8+7] =\
    cube[0],cube[1],cube[2],cube[3],cube[6],cube[7],cube[14],cube[15],cube[4],cube[5],cube[10],cube[11],cube[12],cube[13],cube[8],cube[9]
    return cube

"""
cube1=["yob","wr","wrb","yo","wbo","wo","wog","wb","ygo","yb","yrg","yg","wgr","yr","ybr","wg"]
"""

def buscame(pasosmaximos,busquedas):
    while busquedas>0:
        busquedas-=1
        print(busquedas)
        cube=["yob","wr","wrb","yo","wbo","wo","wog","wb","ygo","yb","yrg","yg","wgr","yr","ybr","wg"]
        pasos=pasosmaximos
        lst=[]
        while pasos>0:
            pasos-=1
            a=random.randint(1,12)
            if a==1:
                cube=U(cube)
                lst.append("U")
            if a==2:
                cube=U2(cube)
                lst.append("U2")
            if a==3:
                cube=U_(cube)
                lst.append("U_")
            if a==4:
                cube=D(cube)
                lst.append("D")
            if a==5:
                cube=D2(cube)
                lst.append("D2")
            if a==6:
                cube=D_(cube)
                lst.append("D_")
            if a==7:
                cube=anti180antiup1(cube)
                lst.append("antiup1")
            if a==8:
                cube=anti180antiup2(cube)
                lst.append("antiup2")
            if a==9:
                cube=anti180antiup3(cube)
                lst.append("antiup3")
            if a==10:
                cube=anti180antidown1(cube)
                lst.append("antidown1")
            if a==11:
                cube=anti180antidown2(cube)
                lst.append("antidown2")
            if a==12:
                cube=anti180antidown3(cube)
                lst.append("antidown3")
            if cube==solvedcube:
                print("**************************SIIII JODEEEEER*******************************")
                print(lst)
                return(lst)

def reduceme(pasosmaximos,busquedas,difs):
        while busquedas>0:
            busquedas-=1
            print(busquedas)
            cube=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
            pasos=pasosmaximos
            lst=[]
            while pasos>0:
                pasos-=1
                a=random.randint(1,12)
                if a==1:
                    cube=U(cube)
                    lst.append("U")
                if a==2:
                    cube=U2(cube)
                    lst.append("U2")
                if a==3:
                    cube=U_(cube)
                    lst.append("U_")
                if a==4:
                    cube=D(cube)
                    lst.append("D")
                if a==5:
                    cube=D2(cube)
                    lst.append("D2")
                if a==6:
                    cube=D_(cube)
                    lst.append("D_")
                if a==7:
                    cube=anti180antiup1(cube)
                    lst.append("antiup1")
                if a==8:
                    cube=anti180antiup2(cube)
                    lst.append("antiup2")
                if a==9:
                    cube=anti180antiup3(cube)
                    lst.append("antiup3")
                if a==10:
                    cube=anti180antidown1(cube)
                    lst.append("antidown1")
                if a==11:
                    cube=anti180antidown2(cube)
                    lst.append("antidown2")
                if a==12:
                    cube=anti180antidown3(cube)
                    lst.append("antidown3")
                if diferentes(cube)<=difs and diferentes(cube)!=0:
                    print("**************************SIIII JODEEEEER*******************************")
                    print("He encontrado un "+str(diferentes(cube))+"-ciclo"+" en "+str(len(lst))+" movimientos.")
                    print(lst)
                    print(cube)
                    return(lst)

def diferentes(lst):
    i=0
    difs=0
    while i<len(lst):
        if lst[i]!=i:
            difs+=1
        i+=1
    return difs

def reducemecon4ciclosymiway(pasosmaximos,busquedas,difs):
        while busquedas>0:
            busquedas-=1
            print(busquedas)
            cube=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
            pasos=pasosmaximos
            lst=[]
            while pasos>0:
                pasos-=1
                a=random.randint(1,19)
                if a==1:
                    cube=U(cube)
                    lst.append("U")
                if a==2:
                    cube=U2(cube)
                    lst.append("U2")
                if a==3:
                    cube=U_(cube)
                    lst.append("U_")
                if a==4:
                    cube=D(cube)
                    lst.append("D")
                if a==5:
                    cube=D2(cube)
                    lst.append("D2")
                if a==6:
                    cube=D_(cube)
                    lst.append("D_")
                if a==7:
                    cube=anti180antiup1(cube)
                    lst.append("antiup1")
                if a==8:
                    cube=anti180antiup2(cube)
                    lst.append("antiup2")
                if a==9:
                    cube=anti180antiup3(cube)
                    lst.append("antiup3")
                if a==10:
                    cube=anti180antidown1(cube)
                    lst.append("antidown1")
                if a==11:
                    cube=anti180antidown2(cube)
                    lst.append("antidown2")
                if a==12:
                    cube=anti180antidown3(cube)
                    lst.append("antidown3")
                if a==13:
                    cube[0],cube[1],cube[2],cube[3]=cube[2],cube[3],cube[0],cube[1]
                    lst.append("0123-2301")
                if a==14:
                    cube[2],cube[3],cube[4],cube[5]=cube[4],cube[5],cube[2],cube[3]
                    lst.append("2345-4523")
                if a==13:
                    cube[4],cube[5],cube[6],cube[7]=cube[6],cube[7],cube[4],cube[5]
                    lst.append("4567-6745")
                if a==14:
                    cube[6],cube[7],cube[0],cube[1]=cube[0],cube[1],cube[6],cube[7]
                    lst.append("6701-0167")
                if a==15:
                    cube[8+0],cube[8+1],cube[8+2],cube[8+3]=cube[8+2],cube[8+3],cube[8+0],cube[8+1]
                    lst.append("0123-2301")
                if a==16:
                    cube[8+2],cube[8+3],cube[8+4],cube[8+5]=cube[8+4],cube[8+5],cube[8+2],cube[8+3]
                    lst.append("2345-4523")
                if a==17:
                    cube[8+4],cube[8+5],cube[8+6],cube[8+7]=cube[8+6],cube[8+7],cube[8+4],cube[8+5]
                    lst.append("4567-6745")
                if a==18:
                    cube[8+6],cube[8+7],cube[8+0],cube[8+1]=cube[8+0],cube[8+1],cube[8+6],cube[8+7]
                    lst.append("6701-0167")
                if a==19:
                    cube[0],cube[1],cube[2],cube[3],cube[4],cube[5],cube[6],cube[7],cube[10],cube[11],cube[12],cube[13]=\
                    cube[12],cube[13],cube[0],cube[1],cube[2],cube[3],cube[10],cube[11],cube[4],cube[5],cube[6],cube[7]
                    lst.append("el súper way brooooo")
                if diferentes(cube)<=difs and diferentes(cube)!=0:
                    print("**************************SIIII JODEEEEER*******************************")
                    print("He encontrado un "+str(diferentes(cube))+"-ciclo"+" en "+str(len(lst))+" movimientos.")
                    print(lst)
                    print(cube)
                    return(lst)

def aristascambiadas(cube):
    i=0
    difs=0
    while i<len(cube):
        if cube[i]!=i and i%2==1:
            difs+=1
        i+=1
    return difs

def esquinascambiadas(cube):
    i=0
    difs=0
    while i<len(cube):
        if cube[i]!=i and i%2==0:
            difs+=1
        i+=1
    return difs

def permutacionesaristas(pasosmaximos,busquedas,difs):
        while busquedas>0:
            busquedas-=1
            print(busquedas)
            cube=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
            pasos=pasosmaximos
            lst=[]
            while pasos>0:
                pasos-=1
                a=random.randint(1,19)
                if a==1:
                    cube=U(cube)
                    lst.append("U")
                if a==2:
                    cube=U2(cube)
                    lst.append("U2")
                if a==3:
                    cube=U_(cube)
                    lst.append("U_")
                if a==4:
                    cube=D(cube)
                    lst.append("D")
                if a==5:
                    cube=D2(cube)
                    lst.append("D2")
                if a==6:
                    cube=D_(cube)
                    lst.append("D_")
                if a==7:
                    cube=anti180antiup1(cube)
                    lst.append("antiup1")
                if a==8:
                    cube=anti180antiup2(cube)
                    lst.append("antiup2")
                if a==9:
                    cube=anti180antiup3(cube)
                    lst.append("antiup3")
                if a==10:
                    cube=anti180antidown1(cube)
                    lst.append("antidown1")
                if a==11:
                    cube=anti180antidown2(cube)
                    lst.append("antidown2")
                if a==12:
                    cube=anti180antidown3(cube)
                    lst.append("antidown3")
                if a==13:
                    cube[0],cube[1],cube[2],cube[3]=cube[2],cube[3],cube[0],cube[1]
                    lst.append("0123-2301")
                if a==14:
                    cube[2],cube[3],cube[4],cube[5]=cube[4],cube[5],cube[2],cube[3]
                    lst.append("2345-4523")
                if a==13:
                    cube[4],cube[5],cube[6],cube[7]=cube[6],cube[7],cube[4],cube[5]
                    lst.append("4567-6745")
                if a==14:
                    cube[6],cube[7],cube[0],cube[1]=cube[0],cube[1],cube[6],cube[7]
                    lst.append("6701-0167")
                if a==15:
                    cube[8+0],cube[8+1],cube[8+2],cube[8+3]=cube[8+2],cube[8+3],cube[8+0],cube[8+1]
                    lst.append("0123-2301")
                if a==16:
                    cube[8+2],cube[8+3],cube[8+4],cube[8+5]=cube[8+4],cube[8+5],cube[8+2],cube[8+3]
                    lst.append("2345-4523")
                if a==17:
                    cube[8+4],cube[8+5],cube[8+6],cube[8+7]=cube[8+6],cube[8+7],cube[8+4],cube[8+5]
                    lst.append("4567-6745")
                if a==18:
                    cube[8+6],cube[8+7],cube[8+0],cube[8+1]=cube[8+0],cube[8+1],cube[8+6],cube[8+7]
                    lst.append("6701-0167")
                if a==19:
                    cube[0],cube[1],cube[2],cube[3],cube[4],cube[5],cube[6],cube[7],cube[10],cube[11],cube[12],cube[13]=\
                    cube[12],cube[13],cube[0],cube[1],cube[2],cube[3],cube[10],cube[11],cube[4],cube[5],cube[6],cube[7]
                    lst.append("el súper way brooooo")
                if aristascambiadas(cube)<=difs and diferentes(cube)!=0 and esquinascambiadas(cube)==0:
                    print("**************************SIIII JODEEEEER*******************************")
                    print("H0STIA PUTA S0Y UN PUT0 GENI0 BR0000000000000000000000000000000000000000")
                    print("He cambiado "+str(aristascambiadas(cube))+" aristas"+" en "+str(len(lst))+" movimientos.")
                    print(lst)
                    print(cube)
                    return(lst)

def permutacionesesquinas(pasosmaximos,busquedas,difs):
        while busquedas>0:
            busquedas-=1
            print(busquedas)
            cube=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
            pasos=pasosmaximos
            lst=[]
            while pasos>0:
                pasos-=1
                a=random.randint(1,19)
                if a==1:
                    cube=U(cube)
                    lst.append("U")
                if a==2:
                    cube=U2(cube)
                    lst.append("U2")
                if a==3:
                    cube=U_(cube)
                    lst.append("U_")
                if a==4:
                    cube=D(cube)
                    lst.append("D")
                if a==5:
                    cube=D2(cube)
                    lst.append("D2")
                if a==6:
                    cube=D_(cube)
                    lst.append("D_")
                if a==7:
                    cube=anti180antiup1(cube)
                    lst.append("antiup1")
                if a==8:
                    cube=anti180antiup2(cube)
                    lst.append("antiup2")
                if a==9:
                    cube=anti180antiup3(cube)
                    lst.append("antiup3")
                if a==10:
                    cube=anti180antidown1(cube)
                    lst.append("antidown1")
                if a==11:
                    cube=anti180antidown2(cube)
                    lst.append("antidown2")
                if a==12:
                    cube=anti180antidown3(cube)
                    lst.append("antidown3")
                if a==13:
                    cube[0],cube[1],cube[2],cube[3]=cube[2],cube[3],cube[0],cube[1]
                    lst.append("0123-2301")
                if a==14:
                    cube[2],cube[3],cube[4],cube[5]=cube[4],cube[5],cube[2],cube[3]
                    lst.append("2345-4523")
                if a==13:
                    cube[4],cube[5],cube[6],cube[7]=cube[6],cube[7],cube[4],cube[5]
                    lst.append("4567-6745")
                if a==14:
                    cube[6],cube[7],cube[0],cube[1]=cube[0],cube[1],cube[6],cube[7]
                    lst.append("6701-0167")
                if a==15:
                    cube[8+0],cube[8+1],cube[8+2],cube[8+3]=cube[8+2],cube[8+3],cube[8+0],cube[8+1]
                    lst.append("0123-2301")
                if a==16:
                    cube[8+2],cube[8+3],cube[8+4],cube[8+5]=cube[8+4],cube[8+5],cube[8+2],cube[8+3]
                    lst.append("2345-4523")
                if a==17:
                    cube[8+4],cube[8+5],cube[8+6],cube[8+7]=cube[8+6],cube[8+7],cube[8+4],cube[8+5]
                    lst.append("4567-6745")
                if a==18:
                    cube[8+6],cube[8+7],cube[8+0],cube[8+1]=cube[8+0],cube[8+1],cube[8+6],cube[8+7]
                    lst.append("6701-0167")
                if a==19:
                    cube[0],cube[1],cube[2],cube[3],cube[4],cube[5],cube[6],cube[7],cube[10],cube[11],cube[12],cube[13]=\
                    cube[12],cube[13],cube[0],cube[1],cube[2],cube[3],cube[10],cube[11],cube[4],cube[5],cube[6],cube[7]
                    lst.append("el súper way brooooo")
                if esquinascambiadas(cube)<=difs and diferentes(cube)!=0 and aristascambiadas(cube)==0:
                    print("**************************SIIII JODEEEEER*******************************")
                    print("He cambiado "+str(esquinascambiadas(cube))+" esquinas"+" en "+str(len(lst))+" movimientos.")
                    print(lst)
                    print(cube)
                    return(lst)




