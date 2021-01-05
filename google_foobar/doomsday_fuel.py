from fractions import Fraction

def absorbingStatesFilter(mat):

    abStates = []
    otherStates = []

    for index, val in enumerate(mat):
        if all([x == 0 for x in val]):
            abStates.append(index)
        else:
            otherStates.append(index)
    return abStates, otherStates
def createLimitingMatrix(m, absorbingStates, otherStates):

    limitingMatrix = []
    n = 0

    if len(absorbingStates) == 1:
        return [1, 1]

    for i in absorbingStates:
        limitingMatrix.append(m[i])
        limitingMatrix[n][n] = 1
        n += 1
    for i in otherStates:
        temp, temp1 = [], []
        for n in (absorbingStates + otherStates):
            temp.append(m[i][n])
        for index, val in enumerate(temp):
            temp1.append(Fraction(val, sum(temp)))
        limitingMatrix.append(temp1)

    return limitingMatrix
    
def matrixMinor(mat, i, j):
    return [row[:j] + row[j+1:] for row in (mat[:i] + mat[i+1:])]


def matrixDeterminant(mat):
    if len(mat) == 2:
        return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
    determinant = 0

    for i in range(len(mat)):
        determinant += (
            (-1)**i) * mat[0][i] * matrixDeterminant(matrixMinor(mat, 0, i))
    return determinant


def matrixTranspose(mat):
    temp = []
    for i in range(len(mat)):
        row = []
        for j in range(len(mat[i])):
            if j == i:
                row.append(mat[i][j])
            else:
                row.append(mat[j][i])
        temp.append(row)
    return temp


def inverseMat(mat):
    determinant = matrixDeterminant(mat)

    if len(mat) == 2:
        return [mat[1][1] / determinant ,- 1 * mat[0][1] / determinant], [
            -1 * mat[1][0] / determinant, mat[0][0] / determinant
        ]

    cofactor = []

    for i in range(len(mat)):
        coRow = []
        for j in range(len(mat)):
            minor = matrixMinor(mat, i, j)
            coRow.append(((-1)**(i + j)) * matrixDeterminant(minor))
        cofactor.append(coRow)
    cofactor = matrixTranspose(cofactor)
    for i in range(len(cofactor)):
        for j in range(len(cofactor)):
            cofactor[i][j] = cofactor[i][j] / determinant
    return cofactor

def createFundamentalMatrix(limMat, abStates):
    I , R, Q = [], [], []
    IQ = []

    for i in range(len(abStates), len(limMat)):
        R.append(limMat[i][:len(abStates)])
        Q.append(limMat[i][len(abStates):])

    for i in range(0, len(Q)):
        temp = [0] * len(Q)
        temp[i] = 1
        I.append(temp)

    for i in range(0, len(I)):
        temp = []
        for j in range(0, len(I[0])):
            temp.append(I[i][j] - Q[i][j])
        IQ.append(temp)
    #Inverse the matrix recieved from the difference of Identiity martix and Q matrix

    F = inverseMat(IQ)
    #print(F)
    return R, F

def multiplyMatrix(F, R):
    zip_b = zip(*R)
    return [[
        sum(ele_a * ele_b for ele_a, ele_b in zip(row_a, col_b))
        for col_b in zip_b
    ] for row_a in F]

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def lcm_val(l):
    return reduce((lambda x, y: lcm(x, y)), l)

def solution(m):
    # Your code here
    abStates, otherStates = absorbingStatesFilter(m)
    limMatrix = createLimitingMatrix(m, abStates, otherStates)
    R, F = createFundamentalMatrix(limMatrix, abStates)
    # calculate the FR value
    FR = multiplyMatrix(F, R)
     # convert fraction to values
    l = []
    for i in FR[0]:
        l.append([i.numerator, i.denominator])
    lcm = lcm_val([i[1] for i in l])

    end = [ (lcm / i[1]) * i[0] for i in l ]

    #print(F)
    #print(R)
    #print(FR)
    #print(end)
    #print(lcm)  
    return end + [lcm]

    
m = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]

print(solution(m)) 
print(solution([
        [1, 2, 3, 0, 0, 0],
        [4, 5, 6, 0, 0, 0],
        [7, 8, 9, 1, 0, 0],
        [0, 0, 0, 0, 1, 2],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]))
print(solution([
        [0, 86, 61, 189, 0, 18, 12, 33, 66, 39],
        [0, 0, 2, 0, 0, 1, 0, 0, 0, 0],
        [15, 187, 0, 0, 18, 23, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]))
