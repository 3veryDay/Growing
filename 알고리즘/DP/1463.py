import sys
sys.setrecursionlimit
N = int(input())
dp = [sys.maxsize]*(N+1)

def dfs(n, cnt) :
    if n == 1 :
        dp[n]=min(dp[n], cnt)
        return
    if n % 3 == 0 :
        if dp[n//3] > cnt + 1 :
            dp[n//3] = cnt + 1
            dfs(n//3, cnt + 1)
    if n %2 == 0 :
        if dp[n//2] > cnt + 1 :
            dp[n//2] = cnt + 1
            dfs(n//2, cnt + 1)
    if dp[n-1] > cnt + 1 :
        dp[n-1] = cnt + 1
        dfs(n-1, cnt + 1)
        
dfs(N, 0)
print(dp[1])
