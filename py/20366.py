import sys

input = sys.stdin.readline
from itertools import combinations

N= int(input())
balls = list(map(int, input().split()))

pairs = set()

for first_idx in range(N - 1) :
    for second_idx in range(first_idx + 1 , N) :
        # 합, i , j
        pairs.add((balls[first_idx] + balls[second_idx], first_idx, second_idx))

pairs = list(pairs)
pairs.sort()
print(pairs)
answer = float('inf')


# 인접 pair만 비교하면 됨
for i in range(len(pairs) - 1):
    s1, i1, j1 = pairs[i]
    s2, i2, j2 = pairs[i+1]

    # 4개의 index가 전부 달라야 함
    if len({i1, j1, i2, j2}) == 4:
        answer = min(answer, abs(s1 - s2))
        if answer == 0:
            print(0)
            sys.exit()

print(answer)
