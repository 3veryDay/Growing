from collections import defaultdict

N, M = map(int, input().split())

numbers = list(set(map(int, input().split())))
numbers.sort()

def backtrack(path, depth) :
    # 종료 조건
    if depth == M :
        print(*path)
        return
    
    # 후보군 탐색
    for num in numbers :
        path.append(num)
        backtrack(path, depth + 1)
        path.pop()
          
for start in numbers :
    backtrack([start], 1)
