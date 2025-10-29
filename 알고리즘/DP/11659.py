import sys

input = sys.stdin.readline

N, M = map(int, input().split())

nums = list(map(int, input().split()))
dp = []
sum = 0
for n in nums :
    sum += n
    dp.append(sum)
for _ in range(M) :
    i, j = map(int, input().split())
    i, j = i-1, j-1
    if i == 0 :
        print(dp[j])
    else :
        print(dp[j] - dp[i-1])
