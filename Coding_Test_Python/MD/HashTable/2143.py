 ## 📄 문제 정보

- **플랫폼**: 백준
- **문제 번호 / 이름**: 두 배열의 합 / 2143
- **링크**: https://www.acmicpc.net/problem/2143

---

## ❓ 문제 설명

>한 배열 A[1], A[2], …, A[n]에 대해서, 부 배열은 A[i], A[i+1], …, A[j-1], A[j] (단, 1 ≤ i ≤ j ≤ n)을 말한다. 이러한 부 배열의 합은 A[i]+…+A[j]를 의미한다. 각 원소가 정수인 두 배열 A[1], …, A[n]과 B[1], …, B[m]이 주어졌을 때, A의 부 배열의 합에 B의 부 배열의 합을 더해서 T가 되는 모든 부 배열 쌍의 개수를 구하는 프로그램을 작성하시오.

---

## ✏️ 문제 조건

- **입력**: 첫째 줄에 T(-1,000,000,000 ≤ T ≤ 1,000,000,000)가 주어진다. 다음 줄에는 n(1 ≤ n ≤ 1,000)이 주어지고, 그 다음 줄에 n개의 정수로 A[1], …, A[n]이 주어진다. 다음 줄에는 m(1 ≤ m ≤ 1,000)이 주어지고, 그 다음 줄에 m개의 정수로 B[1], …, B[m]이 주어진다. 각각의 배열 원소는 절댓값이 1,000,000을 넘지 않는 정수이다.
- **출력**: 첫째 줄에 답을 출력한다. 가능한 경우가 한 가지도 없을 경우에는 0을 출력한다.
- **제약조건**: 2초, **64MB**

---

## 💡 아이디어 / 접근

- 처음 떠올린 풀이 아이디어
    - `defaultdict` 사용해서, 모든 가능한 a의 부분 합을 구하고, 동일한 방식으로 모든 가능한 b의 부분 합을 구하여, 가능한 조합을 cnt하도록 했는데, 이렇게 하면 64MB이라는 작은 메모리 제한에 걸려서 메모리 초과 에러가 뜬다. 그렇기에 default dict을 두개 사용하는 것이 아닌, A에 대해서만 default dict을 사용하도록 했다. default dict의 key는 부분합의 값, value로는 부분합이 그렇게 나오는 조합의 횟수를 저장하도록 했고, B에 대한 부분배열을 돌며, 매번 answer += A_dict[T-B의 부분합] 을 더하도록 했습니다. 


---

## ✅ 내 풀이

### 🔹 풀이 설명(알고리즘 면접이라고 생각하고)

##### 내가 작성

-  `Hash Table`로 구현된 파이썬의 자료형인 `DefaultDict`을 사용했습니다.  입력된 배열 A에 대해서 이중 루프를 돌며 `sum`과 인덱싱을 사용해서 부분합을 구했고, defaultdict(int)을 사용해서 특정 부분합이 몇번 나오는지를 저장하도록 했습니다. B도 동일한 방식으로 부분합을 구해도 되지만, 시간과 공간을 절약하기 위해서 B는 이중 루프를 돌며 부분합을 구한 다음, 목표 값인 T-부분합을 key로 하는 A의 defaultdict의 value값을 더했습니다. 

###### 다듬은 알고리즘 답변 
- `이중 반복문`을 사용해서 A의 부분합을 구하고, 해당 합이 몇 번 나오는지를 파이썬의 해시테이블 자료형인 `defaultdict`에 저장했습니다. 예를 들어, a=[1,3,1] 인 경우, 가능한 부분합은 1,3,1,4,4,5 이기에 key를 1로 가지면 value는 2입니다.
- 다음으로 B의 모든 부분합을 순회하면서 정답을 누적하도록 했습니다. B의 부분합을 구하고, 그 부분합을 B_sum 이라고 하면 T-B_sum에 해당하는 부분합이 몇번 나왔는지 해시맵을 통해 조회한 후, 그 횟수만큼 정답에 더해줍니다.
- 시간 복잡도는 A의 부분합을 구할 때 `O(N^2)`, B의 부분합 순회 및 조회 때 `O(N^2)` 이기에 전체 시간 복잡도는 `O(N^2)`입니다. A,B의 길이가 1000 이하이기 때문에 효율적인 풀이입니다. 
### 🔹 코드

```python
from collections import defaultdict

T = int(input())
A = int(input())
a = list(map(int, input().split()))

B = int(input())
b = list(map(int, input().split()))
answer = 0
A_dict = defaultdict(int)
for start in range(A) :
    for end in range(start, A) :
        if start == end :
            A_dict[a[end]] += 1
        else :
            A_dict[sum(a[start:end+1])] += 1


for start in range(B) :
    for end in range(start, B) :
        B_partial_sum = sum(b[start:end+1])
        answer += A_dict[T-B_partial_sum]
print(answer)
```
### 🔹 시간 복잡도

- `O(n^2)`

---

## 🔍 다른 풀이 / 참고 풀이

> 다른 사람의 풀이 아이디어나 블로그, 해설 등에서 참고한 풀이들을 적어보자.  
> → **내 풀이와 어떤 점이 다른지** 적어두면 나중에 복습에 도움돼!

---

### 풀이 #1

- 설명: 
    - `defaultdict` 대신 `Counter` 를 사용
    - `Counter`보다 `DefaultDict`가 더 빠름, 
       - most_common, +, - 등 사용할 수 있음.

- 코드:

```python
from collections import Counter
 
T = int(input()) # 부 배열의 합으로 만족되야 하는 값
n = int(input()) # 배열 A의 원소 개수
A = list(map(int,input().split())) # 배열 A
m = int(input()) # 배열 B의 원소 개수
B = list(map(int,input().split())) # 배열 B
 
result = 0 # 출력할 값 0으로 초기화
c = Counter() # 카운터 c 정의
 
for s in range(n):
    for e in range(s,n):
        c[sum(A[s:e+1])] += 1 # 배열 A의 모든 부배열의 합을 카운터에 개수로 센다
        
for s in range(m):
    for e in range(s,m):
        t = T - sum(B[s:e+1]) # 타겟 값 T에서 B의 부배열합을 뺀 값이
        result += c[t] # A의 부배열에 존재하면 result에 더해준다. 없으면 저절로 0이 나온다.
print(result)
```
---

### 풀이 #2

- 설명: 
    - 너무 별로. 근데 bisect.bisect_right(a, x) = 리스트 a에서 x가 들어갈 수 있는 오른쪽 경계 인덱스를 반환 
- 코드:

```python
import bisect
 
T = int(input()) # 부 배열의 합으로 만족되야 하는 값
n = int(input()) # 배열 A의 원소 개수
A = list(map(int,input().split())) # 배열 A
m = int(input()) # 배열 B의 원소 개수
B = list(map(int,input().split())) # 배열 B
 
result = 0 # 출력할 값 0으로 초기화
Asum,Bsum=A,B # 각 배열로 초기화
for s in range(n):
    for e in range(s+1,n):
        Asum.append(sum(A[s:e+1])) # 배열 A의 모든 부배열의 합을 추가해준다.
for s in range(m):
    for e in range(s+1,m):
        Bsum.append(sum(B[s:e+1]))# 배열 A의 모든 부배열의 합을 추가해준다.
 
Asum.sort();Bsum.sort()
 
for i in range(len(Asum)):
    l = bisect.bisect_left(Bsum, T-Asum[i])
    r = bisect.bisect_right(Bsum, T-Asum[i])
    result+=r-l
print(result)
```
