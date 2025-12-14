import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
restrictions = list(map(int, input().split()))
M = int(input())
boxes = list(map(int, input().split()))
if max(restrictions) < max(boxes) :
    print(-1)
    exit()
restrictions.sort(reverse=True)
boxes.sort(reverse=True)
count = 0


positions = [0]*N  # 각 크레인이 boxes 어디까지 옮겼는지 인덱스
moved = [False]*M  # 옮겼는지 여부
count = 0
moved_count = 0

while moved_count < M:
    for i in range(N):  # 각 크레인 순서대로
        while positions[i] < M:
            # 아직 안 옮겼고, 크레인이 들 수 있으면
            if not moved[positions[i]] and boxes[positions[i]] <= restrictions[i]:
                moved[positions[i]] = True
                moved_count += 1
                positions[i] += 1
                break
            positions[i] += 1
    count += 1

print(count)
