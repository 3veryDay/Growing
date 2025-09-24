기본 틀 
```python
from collections import deque

q.append((첫번째 노드, 방문 기록, 방문횟수))
while q :
 노드, 방문횟수 = q.popleft()
 if 노드 = 목표 노드 :
  정답 출력, 갱신, 끝 중에 하나
  break
 for neighbor in neighbors :
  if neighbor not in visited : 
   visited.add(neighbor)
   q.append((neighbor, 방문횟수 + 1))
```

## 중요 키 포인트
q에 넣기 전에 방문 처리
visited는 하나 통틀어서 관리


# 추가 조건 없음
### 2178.py
제일 쉬운 경우, 이동 경로에만 제한이 있고, 다른 조건이 없을 때에는
```python
visited는 2차 배열, q는 (y, x, dist)
while q :
 y, x, dist = q.popleft()
 if y와 x가 조건 :
  print(dist)
  end
for 가능한 다음 좌표 ny, nx : 
 if ny nx가 이동 가능한 좌표 : 
  visited[ny][nx] = 1
  q.append(ny, nx, dist + 1)
```
### 7576.py
다른 조건 없음. 여기에서도.

# 추가 조건 하나 있음
### 2206.py
기존 이동 문제에서 벽을 하나 깰 수 있다는 조건이 붙음.
그렇다면 visited을 처리할 떄, 벽을 하나 깬 상태여서 더이상 벽을 깨지 못하는 경우와, 벽을 아직 깨지 않아서 벽을 추가로 깰 수 있는 경우, 2가지가 있음.
그러므로 visited[ny][nx]를 하나로 처리할 수가 없음. 그렇기에 3차 배열로 처리하는 거싱고, 여기에 k라는 벽을 깬 횟수를 추가하는 것이다.

추가로 q에서 값을 넣고, 뺄 때, k를 추가로 관리하게 되어있음.

즉 -> 하나의 조건이 추가되면서 visited에서 하나의 차원도 추가되었고, q에서 관리하는 인수도 하나 추가되었음.

### 1600.py
기존 이동 문제에서 이동 조건, k가 줄어들기 시작함 0,1의 값이 아닌 더 있음. 이럴 경우에도 visited와 q에서 다루는 인자가 하나씩 추가됨. 

# 추가 조건 많음
### 17836.py
조건이 시간, 검 여부가 추가되었음에도 불구하고, 애초에 증가하는 시간은 하나의 인수로 늘어나긴 하지만, 여기서는 sword 여부의 차원 하나만 추가됨.
q에는 시간, 칼 여부를 둘다 추가하지만. visited에서는 값으로 시간을 관리함. 


### 
