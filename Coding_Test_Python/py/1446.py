import sys
input = sys.stdin.readline
from collections import defaultdict
tmp = []
N, D = map(int, input().split())  #N은 지름길 개수, D는 고속도로 길이
shortcuts = []
for _ in range(N) :
    a, b, d = map(int, input().split())
    if b > D : continue
    shortcuts.append((a, b, d))

    
dist = [d for d in range(D+1)]


for i in range(D+1) :
    if i > 0 :
        dist[i] = min(dist[i], dist[i-1] + 1)
    for a, b, d in shortcuts :
        if i == a :
            dist[b] = min(dist[b], dist[a] + d)

print(dist[D])
