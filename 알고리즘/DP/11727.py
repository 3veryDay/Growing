n = int(input())

dp = [0, 1, 3]
while len(dp) <= n + 1 :
    dp.append((dp[-1] + 2*dp[-2])%10007)
print(dp[n])
