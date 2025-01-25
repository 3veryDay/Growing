def solution(board):
    garo = len(board[0])
    saero = len(board)
    answer = 1
    for i in range(1, saero) :
        for j in range(1, garo) :
            a,b,c = board[i][j-1], board[i-1][j], board[i-1][j-1]
            if a== b== c :
                board[i][j] = a + 1
            if a==b!=c or a!= b == c or a == c != b:
                board[i][j] = min(a,b,c)+1
            if a!= b != c :
                board[i][j] = min(a,b,c)+1
            if board[i][j] > answer :
                answer = board[i][j]
            print(board)
    return answer**2

print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))