## 트리 DP란
트리 위에서 DP 사용하는 것

트리는 cycle이 없기 때문에, DFS를 사용해서 자식 노드의 결고를 이용해서 부모 노드를 계산할 수 있음.
**부모 방향으로 모아가는 DP**

## 기본 틀
- 그래프는 인접 리스트로
- DP[node] 혹은 DP[node][state]으로 DP 배열 관리
- visited으로 방문 체크
- DFS를 통해서 자식 노드 탐색 후 DP 갱신

## 기본 틀 코드
```python
def dfs(node) :
  visited[node] = True

  dp[npde] = 초기 값?

  for nxt in graph[node] : 
    if not visited[nxt] :
      dfs(nxt)
      dp[node] = 점화식(dp[node], dp[nxt])

```
