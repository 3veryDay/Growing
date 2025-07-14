def solution(m,n,board) :
    b = [['-']*m for _ in range(n)]
    for i in range(m) :
        for j in (range(n)) :
            b[j][m-i-1] = (board[i][j])
    # print(b)
    #이것도 오래 걸림...ㅎ 정리해두자.
    # for i in range(len(board)) :
    #     b.append(list(map(str, board[i])))
    
    def check(b) :
        # print("before")
        # print(b)
        cnt = 0
        for y in range(n-1) :
            for x in range(len(b[y])-1) :
                if x < len(b[y+1]) - 1 :
                    if b[y][x].lower() == b[y+1][x].lower() == b[y][x+1].lower() == b[y+1][x+1].lower() :
                        b[y][x],b[y+1][x],b[y][x+1],b[y+1][x+1]  = b[y][x].lower(),b[y][x].lower(),b[y][x].lower(),b[y][x].lower()
        # print("between")
        # print(b)
        for y in range(len(b)) :
            x = 0
            while x < len(b[y]) :
                if b[y][x] == b[y][x].lower() :
                    b[y].pop(x)
                    cnt += 1
                else :
                    x += 1
        # print("after")
        # print(b)
        # print(cnt)
        return b, cnt
    answer = 0
    cnt = -1
    while cnt != 0 :
        b, cnt = check(b)
        
        answer += cnt
    return answer
    
    
        
                    
