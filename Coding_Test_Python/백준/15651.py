N, M = map(int, input().split())

def backtrack(path, depth) :
    # 종료 조건
    if depth == M :
        print(' '.join(map(str, path)))
        return
    
    # 후보군 탐색
    for next_num in range(1, N+1) :
        #상태 변경
        path.append(next_num)
        backtrack(path, depth + 1)
        #상태 복원
        path.pop()
        
for first_num in range(1, N+1) :
    backtrack([first_num], 1)
