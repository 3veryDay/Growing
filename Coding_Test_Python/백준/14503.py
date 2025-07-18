import sys

input = sys.stdin.readline

N, M= map(int, input().split())
y, x, dir = map(int, input().split())
# dir를 내 함수랑 맞도록 변경
board = []
for _ in range(N) :
    board.append(list(map(int, input().split())))
d = [[-1,0], [0,1], [1, 0], [0, -1]]
# 청소한 구역 관리 변수
cnt = 0 

def clean(y, x) :
    global cnt
    if board[y][x]==0:
        board[y][x] = 2
        cnt += 1
    
def is_all_clean(y,x) :
    for idx in range(4) :
        ty, tx = y + d[idx][0], x + d[idx][1]
        if board[ty][tx] == 0 :
            return False
    return True



while True :
    # for line in board:
    #     print(line)
    # print(f'y:{y} x:{x} dir : {dir} cnt : {cnt}')
    clean(y,x)
    if is_all_clean(y, x) : # 주변 공간이 모두 깨끗한 경우 후진
        y, x = y - d[dir][0], x - d[dir][1]
        if board[y][x] == 1 :
            print(cnt)
            exit()
        continue
    for i in range(4) :
        dir = (dir - 1) % 4
        ny, nx = y + d[dir][0], x + d[dir][1]
        if board[ny][nx] == 0 :
            y, x = ny, nx
            break
            
        
        
