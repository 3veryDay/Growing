# Union Find

### 기본 틀

```python
def find_parent(x) :
  while x != parent[x] :
    parent[x] = parent[parent[x]]
    x = parent[x]
 return x

def union(a, b) :
  a = parent[a]
  b = parent[b]
  // 그냥 부모만 따지는 게 아니라, 사이즈와 같이 따질 요소가 있을 때
  if a!= b :
    parent[b] = a

  // 그냥 합칠 때
  if a < b :
    parent[b] = a
  else :
    parent[a] = b
```
