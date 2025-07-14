from itertools import permutations as pp
def solution(board):
    answer = -1
    O_lst =[]
    X_lst=[]
    # 규칙을 지켜서 진행한 틱택토에서 나올 수 있는 상황이면 1리턴
    maps = [['.']*3 for _ in range(3)]
    def check(maps) :
        if maps[0][0] == maps[0][1] == maps[0][2] !='.' or maps[1][0] == maps[1][1] == maps[1][2]!='.'  or maps[2][0] == maps[2][1] == maps[2][2] !='.'or maps[0][0] == maps[1][0] == maps[2][0]!='.'  or maps[0][1] == maps[1][1] == maps[2][1]!='.' or maps[0][2] ==  maps[1][2] == maps[2][2]!='.' or maps[0][0] == maps[1][1] == maps[2][2]!='.' or maps[0][2] ==maps[1][1]==maps[2][0]!='.' :
            return 1
    def mapping(o,x) :
        maps = [['.']*3 for _ in range(3)]
        for o_idx,oo in enumerate(list(o)) :
            o_x, o_y = oo
            maps[o_x][o_y] = 'O'
            for x_idx, xx in enumerate(list(x)) :
                x_x , x_y = xx
                maps[x_x][x_y] = 'X'
                # print("**",oo,xx)
                if check(maps) == 1 :
                    if o_idx != len(o)-1 or x_idx != len(x)-1:
                        # print(maps)
                        return False
                    return True
        return True
                
        
    for x in (range(len(board))) :
        for y in range(len(board[0])) :
            if board[x][y] == 'X' :
                X_lst.append([x,y])
            if board[x][y] == 'O' :
                O_lst.append([x,y])
    o = list(pp(O_lst))
    x = list(pp(X_lst))
    if o == [()] and x ==[()] :
        return 1
    if o==[()] :
        return 0
    for o_ in o :
        for x_ in x :
            T = mapping(o_, x_)
            if T :
                return 1
    
    return 0






def solution(board) :
    def check(maps) :
        state = 0
        if maps[0][0] == maps[0][1] == maps[0][2]=='X' or maps[1][0] == maps[1][1] == maps[1][2]=='X'    or maps[2][0] == maps[2][1] == maps[2][2]=='X' or maps[0][0] == maps[1][0] == maps[2][0]=='X'   or maps[0][1] == maps[1][1] == maps[2][1]=='X'  or maps[0][2] ==  maps[1][2] == maps[2][2]=='X'  or maps[0][0] == maps[1][1] == maps[2][2]=='X'  or maps[0][2] ==maps[1][1]==maps[2][0]=='X'  :
            state = 1
        if maps[0][0] == maps[0][1] == maps[0][2] !='.' or maps[1][0] == maps[1][1] == maps[1][2] =='O'  or maps[2][0] == maps[2][1] == maps[2][2] =='O' or maps[0][0] == maps[1][0] == maps[2][0]=='O'  or maps[0][1] == maps[1][1] == maps[2][1]=='O' or maps[0][2] ==  maps[1][2] == maps[2][2]=='O' or maps[0][0] == maps[1][1] == maps[2][2]=='O' or maps[0][2] ==maps[1][1]==maps[2][0]=='O' :
            if state == 1 :
                state = 3
            else :state = 2
        return state
    
    x= 0
    o = 0
    for xx in range(3) :
        for y in range(3) :
            if board[xx][y] == 'X' :
                x += 1
            if board[xx][y] == 'O' :
                o += 1
    state = check(board) 
    '''
    0 없음
    1 X
    2 O
    3 X, O
    
    '''
    
    if o == x :
        if state == 1 or state == 0:
            return 1
        return 0
        
    if o == x+1 :
        if state == 0 or state == 2 :
            return 1
        
    return 0
