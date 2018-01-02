import sys
###Linear Algebra Solver using MCAD Method
##Built and tested to run in the Python 3.6.2 Shell

###Origninal Potential Input Value of A (coefficients of x, y, z)
##Assignment Example
q1A = [[-1, 0, 2],
     [0, 1, -4],
     [5, 3, 1]]

##Alternative Example
q2A = [[1, 2, 2],
     [3, -2, 1],
     [2, 1, -1]]

###Original Potential of B (remaining equation constants)
##Assignment Example
q1B = [[10],
     [-9],
     [15]]

##Alternative Example
q2B = [[5],
     [-6],
     [-1]]

###Matrices that will be manipulated during runtime
##Original Matrix A
AOrg = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]
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

##Original Matrix B
B = [[0],
     [0],
     [0]]

##Result (x,y,z) Matrix
Z = [[0],
     [0],
     [0]]

def Main():
    print("Linear Algebra Solver")
    print("The solver uses the MCAD method to reach a solution by finding the inverse\n of the original coefficients. \n")

    if userConfirm("Select question to solve.\nEnter 1 for Example Posed or 2 for Alternative Example: ") == 1:
        AOrg = q1A
        B = q1B
    else:
        AOrg = q2A
        B = q2B
        
    if (calcDet3x3(AOrg) == 0):
        print("The matrix is singular. Therefore, the matrix not invertable, seek alternate method.")
        end()
    else:
        print("\n--Program Start--\n")

    printMatrix(AOrg, "Matrix A (Original)", True, True)
    printMatrix(B, "Matrix B",  True, True)
    printMatrix(Z, "Matrix Z", True, True)

    print("Determinant of A: \n",calcDet3x3(AOrg),"\n")

    print("Calculation of the Matrix of Minors")
    matrixOfMinors(AOrg, Am)
    printMatrix(Am, "Matrix Am Result", True, True)

    print("Calculation of the Cofactors Matrix")
    Ac = cofactorsOfMinors(Am)
    printMatrix(Ac, "Matrix Ac Result", True, True)

    print("Transposition of Cofactors Matrix")
    transpose3x3(Ac)
    printMatrix(At, "Matrix At Result", True, True)

    print("Multiplication of 1 / Determinant of A by Matrix At ")
    multiplyMatrixByInteger(At, (float(round(1/calcDet3x3(AOrg),10))), Ai)
    printMatrix(Ai, "Matrix At Multiplied by 1 / Det A", True, False)

    print("Multiplication of the Inverse of A by B to give Z")
    multiplyMatrices(Ai, B, Z)
    printMatrix(Z, "Matrix Z Result", False, True)
    
    end()

#Sub Procedures and Functions for System
#Multiplication of a Matrix by a given single integer
def multiplyMatrixByInteger(At, INT, Ai):
    for x in range(len(At)):
        for y in range(len(At)):
            Ai[x][y] = (INT)*(At[x][y])

#Matrix Multiplication Function that returns the result to a predefined matrix
def multiplyMatrices(A, B, Z):
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                Z[i][j] += A[i][k] * B[k][j]

#Transpose a 3x3 Matrix
def transpose3x3(Ac):
    for x in range(len(Ac)):
        for y in range(len(Ac[0])):
            At[y][x] = Ac[x][y]

#Invert the sign of select values in a matrix 
def cofactorsOfMinors(Am):
    return [[Am[0][0], -(Am[0][1]), Am[0][2]],
            [-(Am[1][0]), Am[1][1], -(Am[1][2])],
            [Am[2][0], -(Am[2][1]), Am[2][2]]]

#Calculation of the matrix of minors from the original matrix         
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

#Calculation of the determinant for a 3x3 matrix.=
def calcDet3x3(M):
    return (M[0][0] * (calcDet2x2(M[1][1], M[2][1], M[1][2], M[2][2]))
           -M[1][0] * (calcDet2x2(M[0][1], M[2][1], M[0][2], M[2][2]))
           +M[2][0] * (calcDet2x2(M[0][1], M[1][1], M[0][2], M[1][2])))

#Calculation of the determinant based on the a,b,c,d values (or a 2x2 matrix).
#Where the matrix structured as follows:
# [[a, b],
#  [c, d]]
def calcDet2x2(a, b, c, d):
    return (a*d)-(b*c)

#Print a matrix using the appropriate formatting.
#Where matrix is the matrix being passed;
#title is the name printed above the matrix
#newLine is a boolean value used to determine if a space is left after the matrix
#rnd is a boolean value used to determine what type of formatting is applied to the matrix values
def printMatrix(matrix, title, newLine, rnd):
    print(title,":")
    #Integer is to be used for the majority of matrices, except where the mutiplication by a decimal value takes place.
    #Therefore, see the else statement where non-standard rounding takes place - passed through as a boolean value (rnd).
    if (rnd):
        print('\n'.join([''.join(['{:4}'.format(int(round(item))) for item in row]) for row in matrix]))
    else:
        print("Values Rounded to 2 d.p.")
        print('\n'.join([''.join(['{:6}'.format(float(round(item,2))) for item in row]) for row in matrix]))
    if (newLine): print("")

#Checks which question the user would like the system to solve and prevents an invalid entry
def userConfirm(question): #Require the user to select a question to solve
    reply = str(input(question+' : ')).lower().strip()
    if reply[0] == '1':
        return int(reply[0])
    if reply[0] == '2':
        return int(reply[0])
    else:
        return userConfirm("Please confirm using 1 or 2.")

#Cleanly closes the process and restarts the python shell
def end():
    print("\n--Program End--\n")
    sys.exit()

Main()
