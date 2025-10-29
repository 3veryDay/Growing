import sys
N = int(input())

stairs = [0]
for _ in range(N) :
    stairs.append(int(input()))
if N == 1 :
    print(stairs[-1])
    sys.exit()
dp= [[0]*2 for _ in range(N+1)]
answer = 0
def dfs(n, score, jumped) :
    if n == N :
        return
    if jumped == 0 :
        if dp[n+1][1] < score + stairs[n+1] :
            dp[n+1][1] = score + stairs[n+1]
            dfs(n+1, score + stairs[n+1], 1)
        
    if n+2 <= N and dp[n+2][0] < score + stairs[n+2] :
        dp[n+2][0] = score + stairs[n+2]
        dfs(n+2, score + stairs[n+2], 0)
        
dfs(1, stairs[1], 0)
dfs(2, stairs[2], 0)

print(max(dp[N][0] ,dp[N][1]))
