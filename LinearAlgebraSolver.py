import sys
import numpy as np
#Linear Algebra Solver using MCAD Method

#Origninal Input Value of A
##Assignment Example
AOrg = [[-1, 0, 2],
     [0, 1, -4],
     [5, 3, 1]]

##Alternative Example
##AOrg = [[1, 2, 2],
##     [3, -2, 1],
##     [2, 1, -1]]

#Manipulated A Matrix Result
#Matrix of Minors Step
Am = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]

#Cofactors Matrix Step
Ac = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]

#Matrix Transposition Step
At = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]

#Original Result Value of B
##Assignment Example
B = [[10],
     [-9],
     [15]]

##Alternative Example
##B = [[5],
##     [-6],
##     [1]]

#Result (x,y,z) Matrix
Z = [[0],
     [0],
     [0]]

def Main():
    print("Linear Algebra Solver, see proof for translation between steps and procedures.\n")
    printMatrix(AOrg, "Matrix A (Original)", True)
    printMatrix(B, "Matrix B",  True)
    printMatrix(Z, "Matrix Z", True)

    print("Determinant of A:",calcDet3x3(AOrg))

    #PUSH INPUT THEN OUTPUT
    matrixOfMinors(AOrg, Am)
    printMatrix(Am, "Matrix Am Result", True)
    
    Ac = cofactorsOfMinors(Am)
    printMatrix(Ac, "Matrix Ac Result", True)

    transpose3x3(Ac)
    printMatrix(At, "Matrix At Result", True)
    
    end()

#Sub Procedures and Functions for System

def multiplyMatrixByInteger():
    return

def mutliplyMatrices():
    # iterate through rows of X
    for i in range(len(X)):
        # iterate through columns of Y
        for j in range(len(Y[0])):
            # iterate through rows of Y
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]

def transpose3x3(Ac):
    for x in range(len(Ac)):
        for y in range(len(Ac[0])):
            At[y][x] = Ac[x][y]

def cofactorsOfMinors(Am):
    return [[Am[0][0], -(Am[0][1]), Am[0][2]],
            [-(Am[1][0]), Am[1][1], -(Am[1][2])],
            [Am[2][0], -(Am[2][1]), Am[2][2]]]
            
def matrixOfMinors(AOrg, Am):
    for x in range(len(AOrg)):
        for y in range(len(AOrg)):
            if (x == 0 and y == 0):
                Am[x][y] = calcDet2x2(AOrg[1][1], AOrg[1][2], AOrg[2][1], AOrg[2][2])
                print(x,y,Am[x][y])
            elif (x == 0 and y == 1):
                Am[x][y] = calcDet2x2(AOrg[1][0], AOrg[1][2], AOrg[2][0], AOrg[2][2])
                print(x,y,Am[x][y])
            elif (x == 0 and y == 2):
                Am[x][y] = calcDet2x2(AOrg[1][0], AOrg[1][1], AOrg[2][0], AOrg[2][1])
                print(x,y,Am[x][y])
            elif (x == 1 and y == 0):
                Am[x][y] = calcDet2x2(AOrg[0][1], AOrg[0][2], AOrg[2][1], AOrg[2][2])
                print(x,y,Am[x][y])
            elif (x == 1 and y == 1):
                Am[x][y] = calcDet2x2(AOrg[0][0], AOrg[0][2], AOrg[2][0], AOrg[2][2])
                print(x,y,Am[x][y])
            elif (x == 1 and y == 2):
                Am[x][y] = calcDet2x2(AOrg[0][0], AOrg[0][1], AOrg[2][0], AOrg[2][1])
                print(x,y,Am[x][y])
            elif (x == 2 and y == 0):
                Am[x][y] = calcDet2x2(AOrg[0][1], AOrg[0][2], AOrg[1][1], AOrg[1][2])
                print(x,y,Am[x][y])
            elif (x == 2 and y == 1):
                Am[x][y] = calcDet2x2(AOrg[0][0], AOrg[0][2], AOrg[1][0], AOrg[1][2])
                print(x,y,Am[x][y])
            elif (x == 2 and y == 2):
                Am[x][y] = calcDet2x2(AOrg[0][0], AOrg[0][1], AOrg[1][0], AOrg[1][1])
                print(x,y,Am[x][y])
            else:
                print("Vector Not Found")

def calcDet3x3(M):
    return (M[0][0] * (calcDet2x2(M[1][1], M[2][1], M[1][2], M[2][2]))
           -M[1][0] * (calcDet2x2(M[0][1], M[2][1], M[0][2], M[2][2]))
           +M[2][0] * (calcDet2x2(M[0][1], M[1][1], M[0][2], M[1][2])))

def calcDet2x2(a, b, c, d):
    return (a*d)-(b*c)
    
def printMatrix(matrix, title, newLine):
    print(title,":")
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in matrix]))
    if (newLine): print("")

def end():
    print("\n--Program End--\n")
    sys.exit()

Main()
