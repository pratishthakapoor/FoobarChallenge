def find_access_codes(triplets):
    cnt = 0 
    for i in range(0, len(triplets)):
        if triplets[i][2] % triplets[i][1] == 0 and triplets[i][1] % triplets[i][0] == 0:
            cnt += 1
    return cnt
    
            


def solution(l):
    cnt = 0
    n = 3
    #memo = [0] * len(l)
    #print(memo)
    #for i in range(len(l)-1):
    #    for j in range(i+1, len(l)):
    #        if l[j] % l[i] == 0:
    #            memo[j] += 1
    #            cnt+= memo[i]
    #print(memo)

    #return cnt
    triplets = []

    for i in range(len(l)-1):
        for j in range(i+1, len(l)):
            for k in range(i+2,len(l)):
                if l[k] > l[j]:
                    triplets.append([l[i], l[j], l[k]])
    print(triplets)
    access_code_count = find_access_codes(triplets)
    return access_code_count

print(solution([1, 2, 3, 4, 5, 6]))
print(solution([1,1,1]))
