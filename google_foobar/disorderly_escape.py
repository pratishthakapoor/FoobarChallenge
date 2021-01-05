from collections import Counter

def calculate_gcd(n):
    result = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        for j in range(i,n):
            if i == 0 or j == 0:
                result[i][j] = 1
                result[j][i] = 1
            elif i == j:
                result[i][j]= j+1
            else:
                result[i][j] = result[i][j-i-1]
                result[j][i] = result[i][j-i-1]
    return result


def calculate_fact(n):
    result = [1]
    for i in range(n-1):
        result.append(result[-1]*(i+2))
    return result 

def factorial(x, fact):
    return fact[x-1]

def gcd1(x,y, gcd):
    return gcd[x-1][y-1]

def coefficientFactor(partition, n, fact):
    c = factorial(n, fact)
    for a, b in Counter(partition).items():
        c //=(a**b)*factorial(b, fact)
    return c

def cyclecount(n, fact):
    l = 0
    p =n*[0]
    p[0] = n
    result = []
    a = [0 for i in range(n+1)]
    l = 1
    y = n-1
    while l != 0:
        x = a[l-1] +1
        l -= 1
        while 2 * x <=y:
            a[l] = x
            y -= x
            l += 1
        k = l + 1
        while x <= y:
            a[l] = x
            a[k] = y
            partition = a[:l+2]
            result.append((partition, coefficientFactor(partition, n, fact)))
            x += 1
            y -= 1
        a[l] = x+ y
        y = x + y -1
        partition = a[:l+1]
        result.append((partition, coefficientFactor(partition, n, fact)))
    return result


def solution(w,h,s):
    n = max(w,h)
    gcd = calculate_gcd(n)
    fact = calculate_fact(n)
    grid = 0 
    for i in cyclecount(w, fact):
        for j in cyclecount(h, fact):
            k = i[1]*j[1]
            grid += k*(s**sum([sum([gcd1(x,y, gcd) for x in i[0]]) for y in j[0]]))
    return str(grid//(factorial(w, fact)*factorial(h,fact)))


print(solution(2,2,2))
print(solution(2,3,4))
