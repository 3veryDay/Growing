import sys

input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())  # N은 matrix 크기, K는 바이러스 수

matrix = []
q = []
for _ in range(N) :
    matrix.append(list(map(int, input().split())))
for i in range(N) :
    for j in range(N) :
        if matrix[i][j] != 0 :
            q.append((i, j, matrix[i][j]))
q.sort(key = lambda x : x[2])

q = deque(q)
            
S, X, Y = map(int, input().split())
d = [[-1, 0], [1,0], [0,-1], [0,1]]




for second in range(S) :
    tmp_q = len(q)
    for _ in range(tmp_q) :
        y, x, k = q.popleft() 
        for dir in range(4) :
            ty, tx =  y + d[dir][0], x + d[dir][1]
            if ty <0 or ty >= N or tx < 0 or tx >= N :
                continue
            if matrix[ty][tx] != 0 : continue
            matrix[ty][tx] = k
            q.append((ty, tx, k))
print(matrix[X-1][Y-1])    
