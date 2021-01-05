from collections import Counter

l = [10, 15, 10, 7]
        
n = 1

occurences = {}
result = []

for i in l:
    if i not in occurences:
        occurences[i] = 1

    else:
        occurences[i] = occurences[i] + 1

for i in occurences.keys():
    if occurences[i] > n:
        result.append(i)
    
target = [x for x in l if x not in result]

print(target)
