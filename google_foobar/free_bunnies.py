from itertools import combinations

# combination of the keys for num_buns - num_required + 1

def solution(num_buns, num_required):
    numBunnies = num_buns - num_required + 1
    keys = [[] for num in range(num_buns)]

    #print(numBunnies)
    #print(keys)
    for i, j in enumerate(combinations(range(num_buns), numBunnies)):
        for k in j:
            keys[k].append(i)
    return keys




print(solution (2,1))
print(solution(4,4))
print(solution(5,3))
