def replication_cycle(M, F):
    #startM = 1
    #startF = 1

    m, f = int(M), int(F)
    cnt = 0
    #print(m ,f)

    while m!=1 and f!=1:
        if m ==0 or f == 0:
            return "impossible"
        else:
            if m > f:
                cnt += int(m/f)
                m = m -(f*int(m/f)) 
            elif f > m:
                cnt += int(f/m)
                f = f - (m* int(f/m))
        
    return str(cnt+max(m,f)-1) 



def solution(M, F):
    if F == M:
        return 0
    return replication_cycle(M, F)

print(solution('2', '1'))

print(solution('31', '4'))
print(solution('4', '7'))
