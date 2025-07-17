N, M = map(int, input().split())
answer = []

def backtrack(path, depth) :
    if depth == M :
        print(*path)
        return
    for i in range(1, N+1) :
        if i not in path :
            path.append(i)
            backtrack(path, depth+1)
            path.pop()

for first_num in range(1, N+1) :
    backtrack([first_num], 1)
