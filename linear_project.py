B = [[1,2,3,5],
     [2,3,3,5],
     [1,2,5,1]]


def shape(M):
    return len(M),len(M[0])


def matxRound(M, decPts=4):
    for row in M:
        for i in range(len(row)):
            row[i] = round(row[i], decPts)


def transpose(M):
    row, col = shape(M)
    N = [[0]*row for i in range(col)]
    for i in range(col):
        for j in range(row):
            N[i][j] = M[j][i]

    return N


def matxMultiply(A, B):
    row_A, col_A = shape(A)
    row_B, col_B = shape(B)
    if col_A != row_B:
        return None
    A_mul_B = [[0]*col_B for i in range(row_A)]
    for i in range(row_A):
        for j in range(col_B):
            for k in range(col_A):
                A_mul_B[i][j] += A[i][k]*B[k][j]

    return A_mul_B


def augmentMatrix(A, b):
    import copy
    Ab = copy.deepcopy(A)
    row = len(Ab)
    for i in range(row):
        Ab[i].append(b[i][0])

    return Ab


def swapRows(M, r1, r2):
    tem = M[r1]
    M[r1] = M[r2]
    M[r2] = tem

    return None

#print (B)
#swapRows(B, 0, 2)
#print ('After: B=', B)


def scaleRow(M, r, scale):
    try:
        if not scale:
            raise ValueError
        for i in range(len(M[0])):
            M[r][i] *= scale

        return None
    except ValueError:
        raise ValueError('scale cannot be 0')


def addScaledRow(M, r1, r2, scale):
    for i in range(len(M[0])):
        M[r1][i] += M[r2][i] * scale

    return None
'''
def gj_Solve(A, b, decPts=4, epsilon = 1.0e-16):
    if len(A) != len(b):
        return None
    row = len(A[0])
    Ab = augmentMatrix(A,b)
    for i in range(row):
        for j in range(i:row):



    return None
'''

print (B)
C=transpose(B)
print ('After: B=', B)
print (C)
