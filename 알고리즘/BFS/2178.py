import sys
from collections import deque

N, M  = map(int, input().split())
grid = []
for _ in range(N) :
    grid.append(list(map(int, input().strip())))
q = deque()
q.append((0,0,1))
d = [[0,1], [0,-1], [1,0], [-1,0]]
visited = [[0]*M for _ in range(N)]
while q :
    y, x, dist = q.popleft()
    if y == N-1 and x == M-1 :
        print(dist)
        sys.exit()
    for dy, dx in d :
        ny, nx = y + dy, x + dx
        if 0<= ny < N and 0 <= nx < M :
            if grid[ny][nx] == 1 :
                if visited[ny][nx] == 0 :
                    visited[ny][nx] = 1
                    q.append((ny, nx, dist + 1))
    
