def solution(numbers, target):
    n = len(numbers) - 1
    cnt = 0 
    def dfs(idx, addition) :

        minus = addition - numbers[idx]
        plus = addition  + numbers[idx]
        
        if idx == n :
            if minus == target :
                return 1
            if plus == target :
                return 1
            return 0
        else :
            cnt1 =dfs(idx + 1, minus)
            cnt2 = dfs(idx + 1, plus)
            
            
        return cnt1+ cnt2
    return dfs(0,0)
