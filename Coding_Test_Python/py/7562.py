
import sys
input = sys.stdin.readline
from collections import deque
dy = [-2, -1, -2, -1, 2, 1, 2, 1]
dx = [-1, -2, 1, 2, -1, -2, 1, 2]

def solve(l, y, x, yy, xx) :
    visited = set()
    q= deque()
    q.append((y, x, 0))  # 첫 위치 추가
    visited.add((y, x))

    while q :
        ny, nx, cnt = q.popleft()
        if ny == yy and nx == xx :
            return cnt
        for i in range(8) :
            ty, tx = ny + dy[i] , nx + dx[i]
            if ty < 0 or ty >= l or tx < 0 or tx >= l : continue
            if (ty, tx) not in visited :
                q.append((ty, tx, cnt + 1))
                visited.add((ty, tx))


T = int(input())
for _ in range(T) :
    l = int(input())
    y, x = map(int, input().split())
    yy, xx = map(int, input().split())
    print(solve(l, y, x, yy, xx))
    
