'''
answer 초기화하는게 제일 큰 문제였음
'''



# 3 이상 50 이하
N = int(input())

board = []
for _ in range(N) :
    board.append(list(input()))

def find(board) :
    dif_candy = set()
    d = [[0,1], [1,0], [0,-1], [-1,0]]
    for y in range(N) :
        for x in range(N) :
            for dir in range(4) :
                ny, nx = y+d[dir][0], x + d[dir][1]
                if ny<0 or ny >=N or nx <0 or nx >= N :
                    continue
                if board[ny][nx] != board[y][x]: 
                    dif_candy.add((y,x,ny,nx))
                    dif_candy.add((ny,nx,y,x))
    # print(dif_candy)
    return dif_candy

def trade(y,x,ny,nx) :
    board[y][x], board[ny][nx] = board[ny][nx], board[y][x]
    return board
def return_trade(y,x,ny,nx)    :
    board[y][x], board[ny][nx] = board[ny][nx], board[y][x]
    return board
def eat(board):
    max_eaten = 1  # 최소 1개 이상 존재
    # 가로 검사
    for i in range(N):
        cnt = 1
        for j in range(1, N):
            if board[i][j] == board[i][j-1]:
                cnt += 1
            else:
                max_eaten = max(max_eaten, cnt)
                cnt = 1
        max_eaten = max(max_eaten, cnt)

    # 세로 검사
    for j in range(N):
        cnt = 1
        for i in range(1, N):
            if board[i][j] == board[i-1][j]:
                cnt += 1
            else:
                max_eaten = max(max_eaten, cnt)
                cnt = 1
        max_eaten = max(max_eaten, cnt)

    return max_eaten

possible_trade_candies = find(board)
answer = 0
for candy in possible_trade_candies :
    # print("---")
    a,b,c,d = candy
    board = trade(a,b,c,d)
    answer = max(answer, eat(board))
    # for line in board :
    #     print(line)
    board = return_trade(a,b,c,d)
    if answer == N :
        print(answer)
        exit()
print(answer)

