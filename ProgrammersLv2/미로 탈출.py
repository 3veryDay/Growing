from collections import deque


def solution(maps) :
    def bfs(start, dst, visited, cnt) :
        q = deque()
        q.append([start,0])      
        while q :
            # print(q)
            j, cnt = q.popleft()
            y,x = j[0], j[1]
            # print(y,x, maps[y][x], cnt)
            if maps[y][x] == dst :
                return cnt
            if visited[y][x] == 1 :
                continue
            visited[y][x] = 1
            
            if y >=1 and maps[y-1][x] != 'X' :
                q.append(([y-1,x], cnt + 1))
            if y < len(maps)-1 and maps[y+1][x] != 'X' :
                q.append(([y+1,x], cnt + 1))
            if x >= 1 and maps[y][x-1] != 'X' :
                q.append(([y,x-1], cnt + 1))
            if x < len(maps[0]) -1 and maps[y][x+1] != 'X' :
                q.append(([y,x+1], cnt + 1))
        return -1
    
    
    
    for i in range(len(maps)) :
        for j in range(len(maps[0])) :
            if maps[i][j] == "S" :
                start = [i,j]
            elif maps[i][j] == "L" :
                lever = [i,j]
    visited = [[0]*len(maps[0]) for _ in range(len(maps))]
    visited2 = [[0]*len(maps[0]) for _ in range(len(maps))]

    cnt1 = bfs(start, "L", visited, 0)
    cnt2 = bfs(lever, "E", visited2, 0)
    # print(cnt1, cnt2)
    if cnt1 == -1 or cnt2 == -1 :
        return -1
    return cnt1+  cnt2
