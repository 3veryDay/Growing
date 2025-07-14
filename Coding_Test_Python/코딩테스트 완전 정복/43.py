def solution(n, computers):
    
    visited = [0] * n
    cnt = 0
    
    def dfs(start) :
        stack = [start]
        while stack :
            here = stack.pop()
            
            for i in range(n) :
                if computers[here][i] == 1 and visited[i] == 0 :
                    visited[i] = 1
                    stack.append(i)
        return 1
        
    for i in range(n) :
        if visited[i] == 0 :
            cnt += dfs(i)
    return cnt

print(solution(3	,[[1, 1, 0], [1, 1, 1], [0, 1, 1]]	))