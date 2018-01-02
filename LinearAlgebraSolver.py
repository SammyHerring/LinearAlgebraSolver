import sys
###Linear Algebra Solver using MCAD Method

###Origninal Input Value of A (coefficients of x, y, z)
##Assignment Example
AOrg = [[-1, 0, 2],
     [0, 1, -4],
     [5, 3, 1]]

##Alternative Example
##AOrg = [[1, 2, 2],
##     [3, -2, 1],
##     [2, 1, -1]]

###Original Value of B (remaining equation constants)
##Assignment Example
B = [[10],
     [-9],
     [15]]

##Alternative Example
##B = [[5],
##     [-6],
##     [1]]

###Matrices that will be manipulated during runtime
##Manipulated A Matrix Results
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

#Matrix Multiplyed by Interger (1/Determinant) Step
Ai = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]

#Result (x,y,z) Matrix
Z = [[0],
     [0],
     [0]]

def Main():
    print("Linear Algebra Solver")
    print("The solver uses the MCAD method to reach a solution by finding the inverse of the original coefficients. \n")
    
    if (calcDet3x3(AOrg) == 0):
        print("Matrix is not invertable, seek alternate method.")
        end()

    printMatrix(AOrg, "Matrix A (Original)", True, True)
    printMatrix(B, "Matrix B",  True, True)
    printMatrix(Z, "Matrix Z", True, True)

    print("Determinant of A: \n",calcDet3x3(AOrg),"\n")

    matrixOfMinors(AOrg, Am)
    printMatrix(Am, "Matrix Am Result", True, True)
    
    Ac = cofactorsOfMinors(Am)
    printMatrix(Ac, "Matrix Ac Result", True, True)

    transpose3x3(Ac)
    printMatrix(At, "Matrix At Result", True, True)

    multiplyMatrixByInteger(At, (1/calcDet3x3(AOrg)), Ai)
    printMatrix(Ai, "Matrix At Multiplied by Int", True, False)

    multiplyMatrices(Ai, B, Z)
    printMatrix(Z, "Matrix Z Result", True, True)
    
    end()

#Sub Procedures and Functions for System
def multiplyMatrixByInteger(At, INT, Ai):
    for x in range(len(At)):
        for y in range(len(At)):
            Ai[x][y] = (INT)*(At[x][y])

def multiplyMatrices(A, B, Z):
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                Z[i][j] += A[i][k] * B[k][j]

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
            elif (x == 0 and y == 1):
                Am[x][y] = calcDet2x2(AOrg[1][0], AOrg[1][2], AOrg[2][0], AOrg[2][2])
            elif (x == 0 and y == 2):
                Am[x][y] = calcDet2x2(AOrg[1][0], AOrg[1][1], AOrg[2][0], AOrg[2][1])
            elif (x == 1 and y == 0):
                Am[x][y] = calcDet2x2(AOrg[0][1], AOrg[0][2], AOrg[2][1], AOrg[2][2])
            elif (x == 1 and y == 1):
                Am[x][y] = calcDet2x2(AOrg[0][0], AOrg[0][2], AOrg[2][0], AOrg[2][2])
            elif (x == 1 and y == 2):
                Am[x][y] = calcDet2x2(AOrg[0][0], AOrg[0][1], AOrg[2][0], AOrg[2][1])
            elif (x == 2 and y == 0):
                Am[x][y] = calcDet2x2(AOrg[0][1], AOrg[0][2], AOrg[1][1], AOrg[1][2])
            elif (x == 2 and y == 1):
                Am[x][y] = calcDet2x2(AOrg[0][0], AOrg[0][2], AOrg[1][0], AOrg[1][2])
            elif (x == 2 and y == 2):
                Am[x][y] = calcDet2x2(AOrg[0][0], AOrg[0][1], AOrg[1][0], AOrg[1][1])
            else:
                print("Vector Not Found")

def calcDet3x3(M):
    return (M[0][0] * (calcDet2x2(M[1][1], M[2][1], M[1][2], M[2][2]))
           -M[1][0] * (calcDet2x2(M[0][1], M[2][1], M[0][2], M[2][2]))
           +M[2][0] * (calcDet2x2(M[0][1], M[1][1], M[0][2], M[1][2])))

def calcDet2x2(a, b, c, d):
    return (a*d)-(b*c)
    
def printMatrix(matrix, title, newLine, rnd):
    print(title,":")
    #Rounding is to be used for the majority of matrices, except where the decimal mutiplication takes place.
    #Therefore, see the else statement for the m
    if (rnd):
        print('\n'.join([''.join(['{:4}'.format(int(round(item))) for item in row]) for row in matrix]))
    else:
        print("Values Rounded to 2 d.p.")
        print('\n'.join([''.join(['{:6}'.format(round(item,2)) for item in row]) for row in matrix]))
    
    if (newLine): print("")

def end():
    print("\n--Program End--\n")
    sys.exit()

Main()
