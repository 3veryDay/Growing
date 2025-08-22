import sys
from collections import defaultdict

input = sys.stdin.readline

N, M = map(int, input().split()) 
# 도시 개수 N, 버스 노선 개수 M

edges = []

for _ in range(M) :
    a, b, c = map(int, input().split())
    edges.append((a, b, c))


INF = sys.maxsize

def bellman_ford(start, n) :
    dist = [INF] * (n+1)
    dist[start] = 0

    for i in range(n-1) :
        for a, b, c in edges :
            if dist[a] != INF and dist[b] > dist[a] + c :
                dist[b] = dist[a] + c
    for a, b, c in edges :
        if dist[a] != INF and dist[b] > dist[a] + c :
            print(-1)
            sys.exit()
    return dist


dist = bellman_ford(1, N)
for i in range(2, N + 1 ) :
    if dist[i] != INF :
        print(dist[i])
    else :
        print(-1)
