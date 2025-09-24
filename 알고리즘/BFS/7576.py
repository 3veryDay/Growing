import sys

input = sys.stdin.readline

from collections import deque

M ,N = map(int, input().split())
grid = []
for _ in range(N) :
    grid.append(list(map(int, input().split())))

q = deque()
d = [[0,1], [-1,0], [1,0], [0,-1]]
for n in range(N) :
    for m in range(M) :
        if grid[n][m] == 1 :
            q.append((n, m))
days = 0
while q :
    
    now = len(q)
    for i in range(now) :
        y, x = q.popleft()
        for dy, dx in d :
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M :
                if grid[ny][nx] == 0 :
                    grid[ny][nx] = 1
                    q.append((ny, nx))
    days += 1
for n in range(N ) :
    for m in range(M) :
        if grid[n][m] == 0 :
            print(-1)
            sys.exit()
print(days-1)
