N, M, V = map(int, input().split())
graph = {}
for m in range(M) :
    node1, node2 = map(int, input().split())
    
    if node1 not in graph.keys() :
        graph[node1] = [node2]
    else :
        graph[node1].append(node2)
    if node2 not in graph.keys() :
        graph[node2] = [node1]
    else :
        graph[node2].append(node1)
for key in graph :
    graph[key].sort()
    
#dfs
def dfs(graph, start, visited) :
    visited.append(start)
    if start in graph.keys() :
        for node in graph[start] :
            if node not in visited :
                dfs(graph, node, visited)
                    
    return visited
print(' '.join(map(str,dfs(graph, V, []))))
from collections import deque


def bfs(graph, V) :
    q, visited = deque(), []
    q.append(V)
    
    while q :
        node = q.popleft()
        
        if node not in visited :
            visited.append(node)
            if node in graph.keys() :
                for n in graph[node] :
                    if n not in visited :
                        q.append(n)
    return visited

print(' '.join(map(str,bfs(graph, V))))
