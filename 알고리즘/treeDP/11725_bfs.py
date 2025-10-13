import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
from collections import defaultdict, deque

N = int(input())
parent = [-1]*(N+1)
graph = defaultdict(list)
for _ in range(N-1) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    

visited = [0]*(N+1)

    
q = deque([1])
while q :
    v = q.popleft()
    for u in graph[v] :
        if visited[u] == 0 :
            parent[u] = v
            visited[u] = 1
            q.append(u)

for idx in range(2, N+1) :
    print(parent[idx])
