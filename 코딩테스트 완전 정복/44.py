import heapq


def solution(n, road , k ) :
    distances = [float('inf')] * (n + 1)
    node_before = [0]* (n + 1)
    
    distances[1] = 0
    node_before[1] = 1
    adjacent_node = {}
    #road를 dict 형태로 개조
    for r in road :
        city1, city2, cost = r[0], r[1], r[2]
        adjacent_node[city1].append([city2, cost])
        adjacent_node[city2].append([city1, cost])
        
    queue = []
    heapq.heappush(queue, [distances[1], 1])
    
    while queue :
        distance, node = heapq.heappop()
        
        if distance >= distances[node] :
            continue
        
        for adjacent_node, cost in adjacent_node[node].items() :
            renew_distance = distance + cost
            if renew_distance < distance :
                distances[adjacent_node] = renew_distance
                node_before[adjacent_node] = node
                
                heapq.heappush(queue, [renew_distance, adjacent_node])
        print(queue, distances)
        
print(solution(	6,[[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]],4))