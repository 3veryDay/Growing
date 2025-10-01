MST : 프림 알고리즘이란

모든 정점을 연결하는 최소 비용의 트리(사이클 없음)을 구하는 알고리즘
##### 방식
임의의 시작 정점에서 출발
-> 연결 가능한 간선 중 **가장 작은 가중치를 가진 간선**을 선택
-> 점점 확장해 나가며 MST 완성


크루스칼은 간선을 기준으로 정렬하고, Union-find를 사용해서 사이클 안 생기게 하나씩 선택
프림은 정점을 기준으로 확장.

동작 원리
1. 시작 정점 선택
2. 그 정점과 연결된 간선들을 heapq에 넣음
3. pop! 
  - 만약 MST에 포함되지 않은 정점이면, 정점 포함시키고, 간선을 다시 큐에 추가
  - 이미 포함된 정점이면 무시
4. 포함 다 될때까지 반복



```python
import heapq

def prim(start, graph, n) :
 visited = 0 * n
 pq = [(0, start) ]
 total = 0

 while pq :
  w,u = heapq.heappop(pq)
  if visited[u] == 1 :
   continue
  visited[u] = 1
  total += w

  for nw, v in graph[u] :
   if not visited[v] : 
    heapq.heappush(pq, (nw, v) )
return total
```
