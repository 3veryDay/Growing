from collections import defaultdict

grid = [[0]*100 for _ in range(100)]
# 초기 가로, 세로
width, height = 3, 3
r,c,k = map(int, input().split())
r -= 1
c -= 1
for _ in range(3) :
    grid[_][0], grid[_][1], grid[_][2] = map(int, input().split())

def R():
    """R 연산: 각 행 단위로 정렬"""
    global width
    new_width = 0
    for i in range(height):
        cnt = Counter()
        for j in range(width):
            if grid[i][j] != 0:
                cnt[grid[i][j]] += 1

        new_line = sorted(cnt.items(), key=lambda x: (x[1], x[0]))[:50]

        # 먼저 해당 행 초기화
        for j in range(100):
            grid[i][j] = 0

        idx = 0
        for num, c_ in new_line:
            grid[i][idx] = num
            grid[i][idx+1] = c_
            idx += 2

        new_width = max(new_width, idx)
    width = new_width

        

def C():
    """C 연산: 각 열 단위로 정렬"""
    global height
    new_height = 0
    for j in range(width):
        cnt = Counter()
        for i in range(height):
            if grid[i][j] != 0:
                cnt[grid[i][j]] += 1

        new_line = sorted(cnt.items(), key=lambda x: (x[1], x[0]))[:50]

        # 먼저 해당 열 초기화
        for i in range(100):
            grid[i][j] = 0

        idx = 0
        for num, c_ in new_line:
            grid[idx][j] = num
            grid[idx+1][j] = c_
            idx += 2

        new_height = max(new_height, idx)
    height = new_height


time = 0
while grid[r][c] != k and time < 100 :
    time += 1
    for l in grid :
        if l[0] == 0 :break
        s = ''
        for i in l :
            if i == 0 :break
            s += str(i)
            
        print(s)
    print('-------')
    #행 >= 열
    if width >= height :
        R()
    
    # 행 < 열
    else : 
        C()
if time >= 100 :
    print (-1) 
else :print(time)
