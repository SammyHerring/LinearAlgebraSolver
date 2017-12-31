import sys
import numpy as np
#Linear Algebra Solver using MCAD Method

A = [[-1, 0, 2],
     [0, 1, -4],
     [5, 3, 1]]

B = [[10],
     [-9],
     [15]]

Z = [[0],
     [0],
     [0]]

def Main():
    printMatrix(A, True)
    printMatrix(B, True)
    printMatrix(Z, True)

    #global DetA = (A[0][0])() - (A[0][1])() + (A[0][2])()
    #global AbsDetA = abs(DetA)
    print(dete(A))
    
    end()

#Sub Procedures and Functions for UI elements
##def dete(a):
##    return (a[0][0] * (a[1][1] * a[2][2] - a[2][1] * a[1][2])
##           -a[1][0] * (a[0][1] * a[2][2] - a[2][1] * a[0][2])
##           +a[2][0] * (a[0][1] * a[1][2] - a[1][1] * a[0][2]))

def dete(M):
    return (M[0][0] * (calcDet(create2x2(M[1][1], M[2][1], M[1][2], M[2][2])))
           -M[1][0] * (calcDet(create2x2(M[0][1], M[2][1], M[0][2], M[2][2])))
           +M[2][0] * (calcDet(create2x2(M[0][1], M[1][1], M[0][2], M[1][2]))))

def calcDet(R):
    a = R[0][0]
    b = R[0][1]
    c = R[1][0]
    d = R[1][1]
    #NEEDS TO BE AD-BC, SO FIX MATRIX ALIGNMENT OF 00 01 10 11
    #det = (M[0][0])(M[0][1])-(M[1][0])(M[1][1])
    #det = ad-bc
    return (R[0][0])(R[0][1])-(R[1][0])(R[1][1])

def create2x2(a, b, c, d):
    matrix = [[a, b],
              [c, d]]
    printMatrix(matrix, True)
    return matrix
    
def printMatrix(matrix, newLine):
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in matrix]))
    if (newLine): print("")

def end():
    print("\n--Program End--\n")
    sys.exit()

Main()
