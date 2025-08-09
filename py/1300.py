import sys

input = sys.stdin.readline
N = int(input())
k = int(input())

lo, hi = 1, k
ans = 0

while lo <= hi:
    mid = (lo + hi) // 2
    cnt = 0
    # mid 이하의 수가 몇 개인지 계산
    for i in range(1, N + 1):
        cnt += min(N, mid // i)
    if cnt >= k:
        ans = mid
        hi = mid - 1
    else:
        lo = mid + 1

print(ans)
