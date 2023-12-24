import random

#cubo=["a","b","c","d","e","f","g","h"]

def x(cubo):
    cubo[2],cubo[3],cubo[6],cubo[7]=cubo[7],cubo[2],cubo[3],cubo[6]
    return cubo

def y(cubo):
    cubo[1],cubo[3],cubo[5],cubo[7]=cubo[7],cubo[1],cubo[3],cubo[5]
    return cubo

def z(cubo):
    cubo[4],cubo[5],cubo[6],cubo[7]=cubo[7],cubo[4],cubo[5],cubo[6]
    return cubo

def aleatorio(cubo,lista_comandos):
    ran=random.randint(1,3)
    if ran==1:
        lista_comandos.append("x")
        return x(cubo)
    if ran==2:
        lista_comandos.append("y")
        return y(cubo)
    if ran==3:
        lista_comandos.append("z")
        return z(cubo)

def p():
    cubo=["a","b","c","d","e","f","g","h"]
    lista_comandos=[]
    while cubo!=["b","a","c","d","e","f","g","h"] and len(lista_comandos)<=14:
        cubo=aleatorio(cubo,lista_comandos)
        if cubo==["b","a","c","d","e","f","g","h"]:
            print("********************EUREKA****************", lista_comandos)
            return True
    return False

def p_(): 
    n=3674160
    while True:
        if not p():
            n-=1
            print(n)
        if p():
            return("********************OOOOOOH yeah********************")
            break
    


