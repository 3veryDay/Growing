import sys

input = sys.stdin.readline
answer = -(float('inf'))

N, M, K = map(int, input().split())
board = []
for _ in range(N) :
    board.append(list(map(int, input().split())))

def add_visit(y, x, visited) :
    new_visited = [row[:] for row in visited]
    d = [[0,1],[0,-1],[1,0],[-1,0]]
    new_visited[y][x] = True
    for dir in range(4) :
        ty, tx = y + d[dir][0], x + d[dir][1]
        if ty >=0 and ty < N and tx >= 0 and tx < M :
            new_visited[ty][tx] = True
    return new_visited


max_value = max(map(max, board))

def dfs(y, x, depth, total, visited ) :
    global answer
    if depth == K :
        answer = max(answer, total)
        return
    if total + (K - depth) * max_value < answer:
        return
    for i in range(N) :
        for j in range(M) :        
            #가능한 후보군
            if visited[i][j] is False:
                dfs(i, j, depth+1, total + board[i][j], add_visit(i, j, visited))
visited = [[False]*M for _ in range(N)]




for idx in range(N) :
    for jdx in range(M) :
        dfs(idx, jdx, 1, board[idx][jdx], add_visit(idx, jdx, visited))
print(answer)



'''가지치기가 제일 중ㅇ요했음!!! '''




