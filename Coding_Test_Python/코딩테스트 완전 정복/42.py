from collections import deque


def solution(maps):
    n = len(maps)
    m = len(maps[0])
    dist = [[-1]*m for _ in range(n)]
    moves = [[1,0], [-1,0], [0,1], [0,-1]]
    
    
    def bfs(location ) :
        queue = deque([location])
        dist[location[0]][location[1]] = 1
        
        while queue :
            current_location = queue.popleft()
            x,y = current_location[0], current_location[1]
            for move in moves :
                dx, dy = move[0] + x, move[1] + y
                
                if 0 > dx or n <= dx or 0 > dy or m <= dy : 
                    continue
                
                if maps[dx][dy] == 0 :
                    continue
                
                
                if dist[dx][dy] == -1 :     
                    dist[dx][dy] = dist[x][y] + 1
                    queue.append([dx, dy])
        return dist
    bfs([0,0])
                        
            
    return dist[n-1][m-1]
    

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))