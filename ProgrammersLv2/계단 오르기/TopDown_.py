def solution(n) :
    if n <= 3 :
        return n
    dp = [-1] * (n+1)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3 
    def rec(N) :
        if dp[N] != -1 :
            return dp[N]
        dp[N] = ( rec(N-1) + rec(N-2) ) % 1234567
        return dp[N] 
    return rec(n)


"""
TopDown.에서도 동일한 공간 활용도 문제가 발생한 것 같다. 
2000이라는 n을 넣었을 때 recursion error가 뜬다. 

스택을 사용하기 때문에, 재귀 호출로 인한 스택 오버플로우가 발생한 것이다. 
작은 입력에 적합하기 때문에, 이는 좋은 방법이 아니었다..


똑같은 DP라도 방식에 따라서, 하나는 되고 하나는 되지 않는다.
신기하다.
"""
