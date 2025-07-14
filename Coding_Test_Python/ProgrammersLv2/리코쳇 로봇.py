from collections import deque

def solution(board):
    answer = 0
    dp = [[0] * len(board[0]) for _ in range(len(board))]
    def possible(y,x, cnt) :
        #[y+1,x] [y-1,x] [y, x+1] [y, x-1]
        p = []
        Y,X = y,x
        if Y< len(board)-1 and board[Y+1][x] != 'D' :
            while Y < len(board)-1 and board[Y+1][x] != 'D' :
                Y += 1
            p.append([Y,x, cnt + 1])
        Y,X = y,x
        if Y>0 and board[Y-1][x] != 'D' :
            while Y > 0 and board[Y-1][x] != 'D' :
                Y -= 1
            p.append([Y,x, cnt + 1])
        Y,X = y,x
        if X< len(board[0])-1 and board[y][X+1] != 'D' :
            while X < len(board[0])-1 and board[Y][X+1] != 'D' :
                X += 1
            p.append([Y,X, cnt + 1])
        Y,X = y,x
            
        if X > 0 and board[y][X-1] != 'D' :
            while X > 0 and board[Y][X-1] != 'D' :
                X -= 1
            p.append([Y,X, cnt + 1])
        return p
    
    
    for i in range(len(board)) :
        for j in range(len(board[0])) :
            if board[i][j] == "R" :
                starting_point = [i,j, 0]
                break;
                
    q = deque()
    q.append(starting_point)
    cnt = 0
    while q:
        y, x, cnt = q.popleft()
        if dp[y][x] == 1 :
            continue
        dp[y][x] = 1
        if cnt > len(board) * len(board[0]) :
            return -1
        # print(f'y:{y}, x:{x}, cnt : {cnt}')
        if board[y][x] == "G" :
            return cnt
        q.extend(possible(y,x,cnt))
        
    return -1
