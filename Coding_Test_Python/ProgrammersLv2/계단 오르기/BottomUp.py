def solution( n ) :
    
    if n <= 3 :
        return n
    
    dp = [-1] *( n + 1 )
    
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3 
    
    for idx in range(3, n+1) :
        dp[idx] =( dp[idx-1] + dp[idx-2]) % 1234567
        
    return dp[n] %  1234567
"""
def solution( n ) :
    dp = [-1] *( n + 1 )
    
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3 
    if n <= 3 :
        return n
    
    
    
    for idx in range(3, n+1) :
        dp[idx] =( dp[idx-1] + dp[idx-2]) % 1234567
        
    return dp[n] %  1234567

여기서 잘못 생각해서 시간이 오래 걸렸음
n이 만약 1, 이라면 dp[3]을 정의할 수 없음.


"""
