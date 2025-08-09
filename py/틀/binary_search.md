### 조건을 만족하는 가장 작은 값 찾기

```python
# 단조 증가 일 경우
l, r = 최소_가능값, 최대 가능값 + 1
while l < r :
  m = (l + r ) // 2
  if condition(m) :  # 참이면 왼쪽으로 이동
    r = m
  else :
    l = m + 1  # 거짓이면 오른쪽으로 이동

return l
```

### 조건을 만족하는 가장 큰 값 찾기
```python
while l < r :
  m = (l + r) // 2
  if condition(m) :
    l = m + 1  # 참이면 오른쪽으로 이동
  else :
    r = m
return l - 1
```

### 최소 참은 `r=m`
### 최대 참은 `l=m+1`
