import sys

input = sys.stdin.readline


n = int(input())

dp = [0,1,2,3,5]
for _ in range(1000) :
    dp.append(dp[-1] + dp[-2])
    
print(dp[n]%10007)
