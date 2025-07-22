import sys
from collections import defaultdict, deque

input = sys.stdin.readline
sys.setrecursionlimit(2000)

N, M = map(int, input().split())

dic = defaultdict(list)

for _ in range(M) :
    a, b = map(int, input().split())
    dic[a].append(b)
    dic[b].append(a)
    


visited = [False] * (N + 1)


def bfs( node) :
    q = deque()
    q.append(node)
    while q :
        node = q.popleft()
        visited[node] = True
        for neighbor in dic[node] :
            if visited[neighbor] == False :
                visited[neighbor] = True
                q.append(neighbor)
            
            
answer = 0       
for i in range(1, N+1) :
    if visited[i] == False :
        bfs(i)
        answer += 1

print(answer)
