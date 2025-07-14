def solution( n ) :
    dp = [-1] * (n + 1)
    # dp[0] = 0
    dp[1] = 1
    dp[2] = 1
    def topdown( num ) :
        if dp[num] != -1 :
            return dp[num]
        
        dp[num] = topdown(num-1) + topdown(num-2)
        print(dp)
        return dp[num]
    
    return topdown(10)

"""
backtracking -> TopDown 방식이다. 
이는 위에서부터 1까지 내려오는 방식이다.
dp[num] = dp[num-1] + dp[num-2]라고 해서 오래동안 고생했다.



"""
