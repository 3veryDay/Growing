import copy
import sys

input =  sys.stdin.readline

from collections import deque

# T시간 안에 도달해야 함
d = [[-1, 0], [1, 0], [0, 1], [0,-1]]
N, M , T = map(int, input().split())

grid = []
for _ in range(N) :
    grid.append(list(map(int, input().split())))

q = deque()
# y, x, dist, 마법 검 있음(1) 없음(0) 
q.append((0, 0, 0, 0))
visited = [[[N*M+1]*2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 0
while q :
    y, x, time, sword= q.popleft()
    if y == N-1 and x == M-1 and time <= T:
        print(time)
        print(visited)
        sys.exit()
    if time > T :
        print("Fail")
        sys.exit()
    for dy, dx in d :
        ny, nx = y + dy, x + dx
        if 0<= ny < N and 0 <= nx < M :
            
            # 검 찾음
            if grid[ny][nx] == 2 :
                if visited[ny][nx][1] > time + 1 :
                    visited[ny][nx][1] = time + 1

                    q.append((ny, nx, time + 1, 1))
                
            
            # 검 필요 없음
            if grid[ny][nx] == 0 :
                if visited[ny][nx][sword] > time + 1 :
                    visited[ny][nx][sword] = time + 1
                    q.append((ny, nx, time + 1, sword ))
            # 검 필요 함
            if grid[ny][nx] == 1 and sword == 1 :
                if visited[ny][nx][sword] > time + 1 :
                    visited[ny][nx][sword] = time + 1
                    q.append((ny, nx, time + 1, sword))
print("Fail")
sys.exit()

