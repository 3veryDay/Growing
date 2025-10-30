import sys

N = int(input())
lst = list(map(int, input().split()))

total = lst[0]
answer = -sys.maxsize
for idx in range(1, N) :
    answer = max(answer, total)
    if total < 0 :
        total = lst[idx]
    else :
        total += lst[idx]
    print(idx, answer)
answer = max(answer, total)
