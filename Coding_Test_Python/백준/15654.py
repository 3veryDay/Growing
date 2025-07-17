N, M = map(int, input().split())

numbers = list(map(int, input().split()))
numbers.sort()

def backtrack(path, depth) :
    # 종료 조건
    if depth == M :
        print(*path)
        return
    
    # 후보군 탐색
    for next_idx in range(N) :
        # 유효한 선택 인 겨우(중복이 불가능한 경우 제외)
        if numbers[next_idx] not in path :
            # 상태 변경
            path.append(numbers[next_idx])
            backtrack(path, depth + 1)
            #상태 복원
            path.pop()
            
for first_idx in range(N) :
    backtrack([numbers[first_idx]], 1)
