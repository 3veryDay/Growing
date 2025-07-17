N, M = map(int, input().split())

numbers = list(map(int, input().split()))
numbers. sort()

# 전 문제에서 numbers[idx]로 접근했기 때문에, 이번에는 idx로만 접근하겠다

# idx가 담긴 arr을 넣으면 실제 숫자를 출력
def print_arr(arr) :
    answer = ''
    for a in arr :
        answer += str(numbers[a]) + " "
    print(answer)

def backtrack(path, depth) :
    # 종료 조건
    if depth == M :
        print_arr(path)
        return
    
    # 후보군 탐색
    for next_idx in range(path[-1]+1, N) :
        # 상태 변경
        path.append(next_idx)
        backtrack(path, depth + 1)
        # 상태 복원
        path.pop()

for first_idx in range(N) :
    backtrack([first_idx], 1)
