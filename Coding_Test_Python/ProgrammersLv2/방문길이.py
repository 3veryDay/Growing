# 44분!
def solution(dirs):
    dic = {}
    dic['U'], dic['D'], dic['R'], dic['L'] = [1, 0], [-1, 0], [0, 1], [0, -1]
    x,y = 5,5
    garo =set()
    saero = set()
    def move(direction, y,x) :
        dy, dx = dic[direction]
        dy = dy + y
        dx = dx + x
        
        if 0 <= dx <= 10 and 0 <= dy <= 10 :
            return [dy, dx]
        else :
            return [y, x]    
    
    for d in dirs :
        print(d)
        if d == 'U' :
            dy, dx = move(d, y, x)
            if dy != y : 
                saero.add(y + 10 * x)
                y,x = dy, dx

        elif d =='D' :
            dy, dx = move(d, y, x)
            if dy != y : 
                y,x = dy, dx
                saero.add(y + 10 * x)
        
        elif d == 'R' :
            dy , dx = move(d, y, x)
            if dx != x :
                garo.add(x + 10* y)
                y,x = dy, dx
        elif d =='L' :
            dy, dx = move(d,y,x)
            if dx != x :
                y,x = dy, dx
                garo.add(x + 10* y)
            
        print(f'{y}, {x}  garo : {garo} saero : {saero}')
        
    return len(garo) + len(saero)

# 다른 사람의 풀이.

def solution(dirs):
    s = set()
    d = {'U': (0,1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    x, y = 0, 0
    for i in dirs:
        nx, ny = x + d[i][0], y + d[i][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            s.add((x,y,nx,ny))
            s.add((nx,ny,x,y))
            x, y = nx, ny
    return len(s)//2

'''
(출발점, 도착지점)
(도착지점, 출발점)

(x,y,dx,dy)
(dx,dy,x,y)
로 방향을 표현한 후,

return len(s) // 2
'''


'''소름!
def solution(dirs):
    point = [0,0]
    answer = set()

    for _dirs in dirs:
        if _dirs == 'U' and point[1]!=5:
            point[1]+=1
            nn = (point[0], point[1]-.5)
        elif _dirs == 'D' and point[1]!=-5:
            point[1]+=-1
            nn = (point[0], point[1]+.5)
        elif _dirs == 'R' and point[0]!=5:
            point[0]+=1
            nn = (point[0]-.5, point[1])
        elif _dirs == 'L' and point[0]!=-5:
            point[0]+=-1
            nn = (point[0]+.5, point[1])
        else: pass

        answer.add(nn)

    return len(answer)

    중간 선을 0.5로 표현...!! 
    대박 아이디어.
    
'''
