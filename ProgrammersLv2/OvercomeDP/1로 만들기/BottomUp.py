def BottomUp(num) :
    dp = [-1] * (num + 1) 
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    dp[4] = 2
    for i in range(5, num + 1) :
        if i%3 == 0 and i %2 == 0:
            dp[i] = min(dp[i-1], dp[i//2], dp[i//3]) + 1
        elif i%3 == 0 and i% 2 != 0 :
            dp[i] = min(dp[i-1], dp[i//3]) + 1
        elif i%3 != 0 and i % 2 == 0 :
            dp[i] = min(dp[i-1], dp[i//2]) + 1
        else:
            dp[i] = dp[i-1] + 1    
    return dp[num]
