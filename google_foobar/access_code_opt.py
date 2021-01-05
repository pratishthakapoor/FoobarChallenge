def find_access_codes(l):
    #print(len(l))
    cnt = [0] * len(l)
    triplets = 0 
    #print(cnt)

    for i in range(0, len(l)):
        for j in range(0,i):
            print((i,j))
            #if l[i]%l[j] == 0:
            #    cnt[i] += 1
            #    triplets += cnt[j]
    #print(triplets)
    #print(cnt)

    return triplets
    

def solution(l):

    cnt = 0 
    temp = []

    if len(l) < 3:
        return 0 

    return find_access_codes(l)



print(solution([1,2,3,4,5,6]))
#print(solution([1,1,1]))

