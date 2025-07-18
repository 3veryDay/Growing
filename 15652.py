N, M = map(int, input().split())

def backtrack(path, depth) :
    # 종료 조건
    if depth == M :
        print(*path)
        return
    
    # 후보군 탐색
    for next_num in range(path[-1], N+1) :
        path.append(next_num)
        backtrack(path, depth + 1)
        path.pop()

for start in range(1, N + 1) :
    backtrack([start], 1)
