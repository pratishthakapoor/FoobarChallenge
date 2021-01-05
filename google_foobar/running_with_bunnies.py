from itertools import permutations 

def getNode(node):
    for i, row in enumerate(node):
        for j, w in enumerate(row):
            yield(i, j, w)

def bellmanFord(node, start_point):
    distance = [float('inf') for i in node]
    #print(type(distance))
    #print(type(node))
    #print(type(start_point))
    distance[start_point] = node[start_point][start_point]
    for i in range(len(node)):
        for j,k,w in getNode(node):
            if distance[j] + w < distance[k]:
                distance[k] = distance[j] + w
    return distance


def getDistanceTravelled(times):
    distances = []
    for i in range( len(times) ):
        #print(times, i)
        distance = bellmanFord(times, i)
        distances.append(distance)
    return distances

def checkNegativeCycle(distance):
    dist = distance[0]
    for i,j, w in getNode(distance):
        if dist[i] + w < dist[j]:
            return True 
    return False

def getCost(bunnyList, distance):
    cost = 0
    for i in range(0, len(bunnyList) -1):
        start = bunnyList[i]
        end = bunnyList[i+1]
        cost += distance[start][end]
    start = 0
    end = len(distance) -1
    cost += distance[start][bunnyList[0]]
    cost += distance[bunnyList[-1]][end]
    return cost 


def solution(times, time_limit):
    bunniesCount = len(times) - 2
    #print(bunniesCount)
    bunnyIndex = [bunny + 1 for bunny in range(bunniesCount)]
    #print(bunnyIndex)
    distance = getDistanceTravelled(times)
    #print(distance)
    if checkNegativeCycle(distance):
        return range(bunniesCount)

    for i in range(bunniesCount, 0, -1):
        for bunnyList in permutations(bunnyIndex, i):
            travelCost = getCost(bunnyList, distance)
            if travelCost <= time_limit:
                return [cnt - 1 for cnt in sorted(bunnyList)]
    return []




print(solution([[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]], 1))
