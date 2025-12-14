import sys

input = sys.stdin.readline

N, S = map(int, input().split())

lst = list(map(int, input().split()))
if sum(lst) < S :
    print(0)
    sys.exit()
i, j = 0 , 0
total = 0
answer = sys.maxsize
flag = False
while i < N  :
    print(f'i : {i} j : {j} total : {total}')
    if total < S :
        if j == N:
            break
        total += lst[j]
        j += 1
        
    elif total >= S :
        answer = min(answer , (j-i))
        total -= lst[i]
        i += 1
print(answer)
