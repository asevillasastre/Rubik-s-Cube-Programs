import random

def white_matrix():
    return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def white_lasquehay():
    lasquehay=[(1,1,1,1),(1,0,1,1),(0,1,1,1),(0,0,1,1),(1,1,1,0),(1,0,1,0),(0,1,1,0),(0,0,1,0),(1,1,0,1),(1,0,0,1),(0,1,0,1),(0,0,0,1),(1,1,0,0),(1,0,0,0),(0,1,0,0),(0,0,0,0)]
    return lasquehay

def random_matrix():
    matrix=white_matrix()
    lasquehay=white_lasquehay()
    for i in range(len(matrix)):
        ran=random.randint(0,len(lasquehay)-1)
        matrix[i]=lasquehay[ran]
        lasquehay.pop(ran)
    return matrix

def real_matrix(matrix):
    result=[[],[],[],[]]
    for p in range(len(matrix)):
        resto=p%4
        result[resto].append(matrix[p])
    return result

def matrix_gen():
    return real_matrix(random_matrix())

def comprobation_hendiduras(matrix):
    for e in range(4):
        veracity=matrix[e][0]==0 and matrix[e][3]==1
        if not veracity:
            return False
        for k in range(3):
            veracity=matrix[e][k][1]+matrix[e][k+1][0]
            if not veracity:
                return False
    return True

def comprobation_marron(matrix):
    for e in range(4):
        veracity=matrix[0][e]==0 and matrix[3][e]==1
        if not veracity:
            return False
    for k in range(3):
        veracity=matrix[k][e][1]+matrix[k+1][e][0]
        if not veracity:
            return False
    return True

def p():
    a=matrix_gen()
    count=0
    while ((comprobation_hendiduras(a),comprobation_marron(a))!=(True,True)):
        a=matrix_gen()
        count+=1
        print(20922789888000-count)
    print("*********************************************EUREKA*****************************************")
    return a

            