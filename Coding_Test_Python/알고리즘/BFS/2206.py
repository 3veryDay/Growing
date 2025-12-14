import sys

input  = sys.stdin.readline

from collections import deque

N, M = map(int, input().split())
d = [[0,1], [-1, 0], [0, -1], [1, 0]]

grid = []
for _ in range(N) :
    grid.append(list(map(int, input().strip())))

q = deque()
q.append((0, 0, 1 , 1))
visited = [[[N*M + 1]*2 for _ in range(M)] for _ in range(N)]

while  q : 
    y, x, k, dist = q.popleft()
    if y == N-1 and x == M-1 :
        print(dist)
        sys.exit()
    for dy, dx in d :
        ny, nx = y + dy, x + dx
        if 0<= ny < N and 0 <= nx < M :
            if grid[ny][nx] == 1 and k == 1 :
                if visited[ny][nx][0] > dist + 1 :
                    visited[ny][nx][0] = dist + 1
                    q.append((ny, nx, k-1, dist + 1))
            if grid[ny][nx] == 0 :
                if visited[ny][nx][k] > dist + 1 :
                    visited[ny][nx][k] = dist + 1
                    q.append((ny, nx, k, dist + 1))
                    
print(-1)
sys.exit()    
                
