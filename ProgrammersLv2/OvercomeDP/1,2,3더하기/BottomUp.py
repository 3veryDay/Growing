def solution(num ) :
    if num <= 2 :
        return num
    if num == 3 :
        return 4
    
    
    
    dp = [-1] * (num + 1)
    
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    
    
    for i in range(4, num + 1) :
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        
    return dp[num]

print(solution(7))
