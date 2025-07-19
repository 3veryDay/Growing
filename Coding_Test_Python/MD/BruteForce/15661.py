## 📄 문제 정보

- **플랫폼**: 백준
- **문제 번호 / 이름**: 링크와 스타트/15661
- **링크**: https://www.acmicpc.net/problem/15661

---

## ❓ 문제 설명

<img width="433" height="275" alt="image" src="https://github.com/user-attachments/assets/e8aa0b97-b779-4d74-b66e-ce20486ab714" />

---

## ✏️ 문제 조건

- **입력**: 첫째 줄에 N(4 ≤ N ≤ 20)이 주어진다. 둘째 줄부터 N개의 줄에 S가 주어진다. 각 줄은 N개의 수로 이루어져 있고, i번 줄의 j번째 수는 Sij 이다. Sii는 항상 0이고, 나머지 Sij는 1보다 크거나 같고, 100보다 작거나 같은 정수이다.
- **출력**: 첫째 줄에 스타트 팀과 링크 팀의 능력치의 차이의 최솟값을 출력한다
- **제약조건**: 2초, 512MB

---

## 💡 아이디어 / 접근

- 처음 떠올린 풀이 아이디어
    - Brute Force로 모든 가능한 경우를 다 탐색하도록 했다. 하지만, i와 j의 시너지 점수는 board[i][j] + board[j][i]이기 때문에 board[i][j] += board[j][i]로 합쳐서 생각했다. 하지만 이것은 크게 시간복잡도나 공간 복잡도에 영향을 미치지 않기 때문에 생략해도 될 것이다. 
- itertools의 combination을 사용해서 모든 가능한 조합을 생성했고, 외부 함수를 통해서 만들어진 조합에서 나오는 최소 시너지 차이값을 계산하도록 했다. 

---

## ✅ 내 풀이

### 🔹 풀이 설명

- Brute Force로 가능한 팀 조합을 모두 만들고, 각 조합에 대해 나머지 팀을 구해서, 두 팀의 시너지 합을 계산하고, 그 차이를 최소로 갱신했습니다.
- 중복 제거를 통해서 최적화를 했습니다. 

### 🔹 코드

```python
from itertools import combinations

N = int(input())
S = []
for _ in range(N) :
    S.append(list(map(int, input().split())))
for i in range(N) :
    for j in range(i+1, N) :
        S[i][j] += S[j][i]
        S[j][i] = 0


for line in S :
    print(line)



def calculate_difference( members1) :
    members = set(i for i in range(N))
    members2 = members - members1
    sum1 = 0
    members1 = list(members1)
    members1.sort()
    for idx, person1 in enumerate(members1) :
        for person2 in members1[idx:] :
            sum1 += S[person1][person2]
    sum2 = 0
    members2 = list(members2)
    members2.sort()
    for idx, person1 in enumerate(members2) :
        for person2 in members2[idx:] :
            sum2 += S[person1][person2]
    print(f'members1 : {members1} sum1 : {sum1} sum 2 :{sum2}')
    return abs(sum1-sum2)


# 인원수가 적은 팀의 인원수를 입력 -> 그때의 최소 리턴
def calculate(start_team_member) :
    answer = float('inf')
    members = set(i for i in range(N))
    small_team_member = list(combinations(members, start_team_member))
    print(small_team_member)
    for team_member in small_team_member :
        answer = min(answer, calculate_difference(set(team_member)))
    return answer    


result = float('inf')
for start_team_member in range(2, N//2 + 1) :
    result = min(result, calculate(start_team_member))
print(result)
```
### 🔹 시간 복잡도

- (예: O(N log N), O(N^2) 등과 왜 그렇게 되는지 간단히 설명)

---

## 🔍 다른 풀이 / 참고 풀이

> 다른 사람의 풀이 아이디어나 블로그, 해설 등에서 참고한 풀이들을 적어보자.  
> → **내 풀이와 어떤 점이 다른지** 적어두면 나중에 복습에 도움돼!

---

### 풀이 #1

- 설명: 
    -  비트 마스킹
    - 비트 마스킹 써서 훨씬 간단함. -> 근데 내가 처음 보는 개념임. 

- 코드:

```python
N=int(input())

s=[list(map(int,input().split())) for _ in range(N)]
answer=1e9

def cal(arr):
    sumValue=0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            sumValue+=s[arr[i]][arr[j]]+s[arr[j]][arr[i]]
    return sumValue

for i in range(1<<N):
    team1,team2=[],[]
    for j in range(N):
        if (1<<j)&i:
            team1.append(j)
        else:
            team2.append(j)
    if team1 and team2:
        answer=min(answer,abs(cal(team1)-cal(team2)))

print(answer)
```
---
비트 마스킹(Bit Masking)은 **정수의 비트를 이용해서 상태를 저장하고 조작하는 기법**으로, 알고리즘 인터뷰나 비트 연산이 필요한 문제에서 자주 사용됩니다. 특히 **부분 집합, 방문 처리, 상태 압축 DP** 등에서 유용합니다.

---

## ✅ 비트 마스킹 핵심 요약

| 연산 | 의미 | 예시 (비트 기준) | 파이썬 |
|------|------|------------------|--------|
| `|`  | OR (켜기) | `1010 \| 0100 = 1110` | `a | b` |
| `&`  | AND (확인) | `1010 & 0100 = 0000` | `a & b` |
| `^`  | XOR (반전) | `1010 ^ 0100 = 1110` | `a ^ b` |
| `~`  | NOT (반전) | `~1010 = -(1011)` | `~a` |
| `<<` | 왼쪽 시프트 | `0001 << 2 = 0100` | `a << 2` |
| `>>` | 오른쪽 시프트 | `0100 >> 2 = 0001` | `a >> 2` |

---

## ✅ 대표 예제: 부분집합 구하기 (비트마스크로)

```python
N = 4  # 원소 개수
arr = ['a', 'b', 'c', 'd']

for i in range(1 << N):  # 0부터 2^N - 1까지
    subset = []
    for j in range(N):
        if i & (1 << j):  # j번째 비트가 1인지 확인
            subset.append(arr[j])
    print(subset)
```

---

## ✅ 실전 팁

- `1 << x` → x번째 비트를 `1`로 만든다.
- `bitmask | (1 << x)` → x번째 비트를 켠다 (추가).
- `bitmask & ~(1 << x)` → x번째 비트를 끈다 (제거).
- `bitmask & (1 << x)` → x번째 비트가 켜져있는지 확인.
- `bin(mask).count('1')` → 켜진 비트 개수 = 선택된 원소 수.

---

## ✅ 사용되는 대표 알고리즘 문제 유형

| 유형 | 설명 |
|------|------|
| 부분 집합 탐색 | 최대 2ⁿ개의 조합을 비트로 표현 |
| 방문 처리 | DFS/BFS에서 `visited` 대신 `int` 사용 |
| 상태 압축 DP | 예: [외판원 순회 (TSP)]에서 `dp[현재 도시][방문 상태]` |
| 게임, 퍼즐 상태 저장 | 상태가 많을 때 비트로 압축 |

---
