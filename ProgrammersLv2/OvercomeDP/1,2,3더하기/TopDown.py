"""top down에서 계속 dp[1],dp[2] 와 같은 초기값 설정 계속 까먹고 있음!
"""


def solution(num) :
    if num <= 2 :
        return num
    if num == 3 :
        return 4
    
    dp = [-1] * (num + 1)
    
    dp[1], dp[2], dp[3] = 1,2,4
    
    def topDown(n) :
        if dp[n] != -1 :
            return dp[n]
        else :
            dp[n] = topDown(n-1) + topDown(n-2) + topDown(n-3)
            
        return dp[n]
    
    return topDown(num)
