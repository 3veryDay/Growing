def solution(num) :
    
    
    def dfs(n) :
        if n == num :
            return 1
        if n > num :
            return 0
        answer = 0
        for i in (1,2,3) :
            if i +n > num :
                break;
            
            answer += dfs(n + i)
            
        return answer
    
    tmp = dfs(0)
    return tmp
    
