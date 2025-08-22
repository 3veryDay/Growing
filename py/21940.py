N, M = map(int, input().split())
INF = float('inf')
graph = [[INF]*N for _ in range(N)]
for i in range(N) :
    graph[i][i] = 0
for _ in range(M) :
    a, b, t = map(int, input().split())
    graph[a-1][b-1] = t
K = int(input())
C = list(map(int, input().split()))

for k in range(N) :
    for i in range(N) :
        for j in range(N) :
            if graph[i][j] > graph[i][k] + graph[k][j] :
                graph[i][j] = graph[i][k] + graph[k][j]

cities = [0] * (N)
for X in range(N) :
    maxValue = 0
    for c in C :
        if c == X or graph[c][X] == INF or graph[X][c] == INF : continue
        maxValue = max(maxValue, graph[X][c] + graph[c][X])
    cities[X] = maxValue
answer = []
target = min(x for x in cities if x != INF)
for X in range(N) :
    if cities[X] == target :
        answer.append(X+1)

print(*answer)
