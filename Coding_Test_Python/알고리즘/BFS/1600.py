import sys
from collections import deque

input = sys.stdin.readline

d = [[0,1], [1,0], [0,-1], [-1,0]]

h_d = [[-2,-1], [-1,-2], [1,-2],[2,-1],[-2,1],[-1,2],[1,2],[2,1]]

K = int(input())
M, N = map(int, input().split())
grid = []
for _ in range(N) :
    grid.append(list(map(int, input().split())))

visited = [[[M*N + 1]*(K+1) for _ in range(M)] for _ in range(N) ]

q = deque()
# y, x, moves, k
q.append((0,0,0,K))
while q :
    y, x, moves, k = q.popleft()
    if y == N - 1 and x == M - 1 :
        print(moves)
        sys.exit()
    # 일반 원숭이의 움직임
    for dy, dx in d :
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0<= nx < M :
            if grid[ny][nx] == 0 :
                if visited[ny][nx][k] > moves + 1 :
                    visited[ny][nx][k] = moves + 1
                    q.append((ny, nx, moves + 1, k))
                    
    # 말의 움직임
    if k > 0 :
        for dy, dx in h_d :
            ny, nx = dy + y, x + dx
            if 0<= ny < N and 0 <= nx  < M :
                if grid[ny][nx] == 0 :
                    if visited[ny][nx][k-1] > moves + 1 :
                        visited[ny][nx][k-1] = moves + 1
                        q.append((ny, nx, moves + 1, k - 1))
                        
                        
print(-1)
sys.exit()
