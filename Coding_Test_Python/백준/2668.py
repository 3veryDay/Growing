N = int(input())
board = [0] + [int(input()) for _ in range(N)]
answer = []

def dfs(now, start):
    if not visited[now]:
        visited[now] = True
        dfs(board[now], start)
    elif now == start:
        answer.append(start)

for i in range(1, N+1):
    visited = [False]*(N+1)
    dfs(i, i)

print(len(answer))
print(*sorted(answer), sep="\n")
