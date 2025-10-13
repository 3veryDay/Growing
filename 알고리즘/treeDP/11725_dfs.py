import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
from collections import defaultdict

N = int(input())
parent = [-1]*(N+1)
graph = defaultdict(list)
for _ in range(N-1) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    

visited = [0]*(N+1)
def dfs(u) :
    visited[u] = 1
    for v in graph[u] :
        if visited[v] == 0 :
            visited[v] = 1
            parent[v] = u
            dfs(v)
dfs(1)     

for idx in range(2, N+1) :
    print(parent[idx])
