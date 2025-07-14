import heapq


def solution(graph, start) :
    #거리 기록용 distances
    distances = {node : float('inf') for node in graph}
    
    #자신으로부터 시작하기에 start의 최소 경로는 0으로 고정
    distances[start] = 0
    #heapq로 관리할 것이기에, 가장 작은 값을 가진 node를 꺼냄
    queue = []
    heapq.heappush(queue, [distances[start], start])
    paths = {}
    
    
    #모든 노드가 방문하고, 기록될 때까지 반복
    while queue :
        current_distance, current_node = heapq.heappop(queue)
        
        if distances[current_node] < current_distance :
            continue
        
        for adjacent_node, weight in graph[current_node] :
            distance = distances[current_node] + current_distance
        
            if distance < distances[adjacent_node] :
            #리뉴리뉴리뉴리뉴
                paths[adjacent_node] = paths[current_node] + adjacent_node
                distances[adjacent_node] = distance
                    
                    
                    
                    
    return ([distances, paths])