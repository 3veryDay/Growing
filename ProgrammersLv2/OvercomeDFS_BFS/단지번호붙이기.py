from collections import defaultdict


def possible_xy(x,y) :
    possible = []
    if y-1 >= 0 :
        possible.append([x, y-1])
    if y + 1 < N :
        possible.append([x, y+1])
    if x-1 >= 0 :
        possible.append([x-1,y])
    if x + 1 < N :
        possible.append([x+1, y])
    return possible

def dfs(x,y,curr_address,visited, map) :
    if map[y][x] == '1':
        visited[y][x] =1 
        answer[curr_address] += 1
    
    dxdy = possible_xy(x,y)
    
    for dx, dy in dxdy :
        if visited[dy][dx] == 0 and map[dy][dx] == '1':
            dfs(dx,dy,curr_address,visited, map)

N = int(input())

map = []
for n in range(N) :
    map.append(list(input()))
visited = [[0]*N for _ in range(N)]
answer = defaultdict(int)

curr_address = 1


for j in range(N) :
    for i in range(N) :
        if visited[i][j] == 0 and map[i][j] == '1' :
            dfs(j,i,curr_address,visited,map)
            curr_address += 1
            
print(len(answer))
for a in sorted(answer.values()) :
    print(a)
