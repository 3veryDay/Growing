## 탐색

#### 🚀 이분 탐색(Binary Search)

 **정렬된 데이터에서 특정 값을 빠르게 찾는 알고리즘**
 
 
 📌 핵심 개념
 
1. **정렬된 범위를 반으로 나눠서 탐색**
   - 보통 left, right, mid = (left+right)//2 로 진행
   - mid을 기준으로 찾고자 하는 값이 왼쪽에 있는지, 오른쪽에 있는지 판단
2. **탐색 범위를 반으로 줄임**
   - 오른쪽에 있으면 left = mid + 1
   - 왼쪽에 있으면 right = mid -1
     
👩‍👩‍👧‍👧 이런 상황에서도 이분 탐색이 쓰이더라

- 싸울 수 있는 최대 라운드(BFS로 하면 시간 복잡도가 너무 크기에)

<details>
  <summary>나온 문제🔦</summary>
  
<https://school.programmers.co.kr/learn/courses/30/lessons/142085>
<https://school.programmers.co.kr/learn/courses/30/lessons/340212>
</details>


## BFS

 - visited 을 사용해서, 한번 방문했으면 끝
 - deque를 사용
 - while q : 사용


🥇 최단 거리 탐색

🥇 모든 노드를 같은 깊이에서 탐색(네트워크 연결 상태)

🥇 탐색 노드 많지만, 탐색 깊이가 얕을 때 

이외

🥈 2D 행렬에서 영역 탐색 문제

🥈 최소 단계로 특정 상태 변경 문제 (ex. 한 글자씩 바꿔서 목표 단어 만들기)

🥈 위상 정렬(순서가 있는 그래프 탐색) (ex. 주어진 조건을 만족하는 강의 순서 정하기)
<details>
  <summary>나온 문제🔦</summary>
  
<https://school.programmers.co.kr/learn/courses/30/lessons/154540>
<https://school.programmers.co.kr/learn/courses/30/lessons/159993>
</details>

시행착오😫

while q 가 한번에 끝나면, visited을 미리 처리한 게 아닐까 
## 1차 배열

<details>
  <summary>나온 문제🔦</summary>
  
<https://school.programmers.co.kr/learn/courses/30/lessons/92341>
</details>

## 2차 배열

<details>
  <summary>나온 문제🔦</summary>
  
<https://school.programmers.co.kr/learn/courses/30/lessons/17679>
</details>

## DICT

✅ dict의 key로는 **immutable type**만 사용 가능하다. 즉, `tuple () ` 은 사용 가능하다.

❌ 이유: 리스트는 변경 가능(mutable)하기 때문

dict의 요소 순으로 정렬을 원할 시에는, `dic.items()`을 꺼내서 정렬을 해야 한다.
sorted_dict = dict(sorted(data.items(), key=lambda x: x[1])) (reverse = True 별도)

## Sliding Window

- 하나의 배열안에서 고정된(혹은 고정되지 않은) 끝과 끝을 따질 때

<details>
  <summary>나온 문제🔦</summary>
  
</details>

## Greedy

- 스택 사용한 그리디

<details>
  <summary>나온 문제🔦</summary>
  
<https://school.programmers.co.kr/learn/courses/30/lessons/42883#>
</details>

## DP

## HEAP
-DFS말고 HEAP

heapq의 heappop, heappush등
max와 min을 동시에 관리해야 할 때는 max_heap, min_heap을 두개 관리하면서
max_heap에는 -num을 붙여서 큰 수가 작은 수가 되어서 먼저 pop되도록!

<details>
  <summary>나온 문제🔦</summary>
  
<https://school.programmers.co.kr/learn/courses/30/lessons/142085>
<https://school.programmers.co.kr/learn/courses/30/lessons/42628>
</details>

## 규칙 찾기

<details>
  <summary>나온 문제🔦</summary>
  
<https://school.programmers.co.kr/learn/courses/30/lessons/12899#>
</details>

-----
## 메서드, 모듈

<details>
<summary> re 모듈 </summary>

 1. `re.**match**(pattern, string)` : 문자열의 시작 부분이 패턴과 일치하는지 확인
 2. `re.**search**(pattern, string)` : 문자열 **어디든** 패턴과 일치하는 부분이 있는지 확인
 3. `re.**findall**(pattern, string)` : 패턴과 **일치하는 모든 부분을 LIST으로 반환**
 4. `re.**finditer**(pattern, string)` : 패턴과 일치하는 부분을 iterator로 반환
 5. `re.**sub**(pattern, repl, string)` : 패턴과 일치하는 부분을 `repl`로 치환
 6. `re.**split**(pattern, string)` : 패턴을 기준으로 문자열을 **분할하여 LIST로 반환**

기본적으로 사용하는 건 : **s = re.search(r"\d{4}-\d{2}-\d{2}", text)**

#### 메타 문자

1. 숫자 관련
 - `\d` → 숫자 (0~9)
   예: \d+ → "2025년"에서 2025만 매칭됨
 - `\D` → 숫자가 아닌 문자
   예: \D+ → "2025년"에서 년만 매칭됨

2. 문자 관련
 - `\w` → 문자 + 숫자 + _(언더스코어)
   [a-zA-Z_]와 같음,
   예 : \w+ → "Hello_123!"에서 "Hello_123" 매칭됨
 - `\W` → \w가 아닌 문자(공백, 특수 문자 등)
   예 : \w+ → "Hello_123!"에서 "!" 매칭됨

3. 공백
 - `\s` → 공백
 - `\S` → 공백이 아닌 문자

4. 기타 특수 문자

   문장 : text = "I love cats and categories."
   
- `\.` → 아무 문자
  예 : "a.c" 에서 "abc", "a#c" 매칭
- `^` → 문자열 시작
  예 : ^Hello 에서 "Hello world"에서만 매칭
- `$` → 문자열 끝
  예 : World$ 에서 "Hello World"에서만 매칭
- `\b` → 단어 경계
  예 : \bcat\b 에서 cat은 매칭되지만 category는 매칭 안


<details>
  <summary>나온 문제🔦</summary>
  <https://school.programmers.co.kr/learn/courses/30/lessons/67257>
</details>

</details>

<details>
 <summary> math</summary>
 -factorial
 
 ✅ ceil, floor : 올림, 내림
</details>
<details>
<summary> all </summary>
  
`all()` 함수는 반복 가능한 (iterable) 객체의 모든 요소가 True인지 확인하는 함수

- 모든 요소가 `True` => `True` 반환
- 하나라도 `False` => `False` 반환
- 빈 리스트 => `True` 반환

all(조건문 for --)
all(num % 2 == 0 for num in numbers) 
all(num % 2 for num in numbers) 하면 완전 다른 느낌
0만 False, 나머지 숫자는 True를 의미하기에, 

all(num % 2 == 0 for num in numbers) => numbers 배열의 모든 숫자가 짝수이어야지, True
all(num % 2 for num in numbers) => numbers 배열의 모든 숫자가 홀수이어야지 , True
</details>
<details>
<summary> heapq</summary>
<details>
  <summary>나온 문제🔦</summary>
  
<https://school.programmers.co.kr/learn/courses/30/lessons/155651>
</details>

</details>


<details>
<summary> collections </summary>

1. counter
- `most_common()`  → 가장 흔한 값 하나가 아닌, count가 많은 순으로 set으로 반환
- `update()` → 개수 추가
- `subtract()` → 개수 빼기
- `del counter['p']`  → 'p' 제거


<details>
  <summary>나온 문제🔦</summary>
  
<https://school.programmers.co.kr/learn/courses/30/lessons/152996>
<https://school.programmers.co.kr/learn/courses/30/lessons/72411>
</details>

</details>

<details>
<summary> functools </summary>
  
1. cmp_to_key
res = sorted(기존 함수, key = `cmp_to*key`(비교 함수) )
비교함수 (a, b ) < 0 -> a가 b보다 앞에, 그대로 유지
비교함수 (a, b ) == 0 -> 두 값의 순서 유지
##### (양수)비교함수 (a, b ) > 0 -> b가 a보다 앞에, 순서 바꾸기

|장점|담점|
|---|---|
|비교 함수 사용 가능|비교 연산 여러번 수행, 성능 떨어짐|
|복잡한 정렬 기준이 있을 때| key를 직접 사용하는게 효율적|
|sorted, min, max 사용 가능 | |

2. reduce

reduce(함수, 반복가능한_객체, 초기값)  # 초기값은 선택사항
`함수`는 두개의 값을 받아서 하나로 줄이는 연산을 수행하는 함수(ex : gcd, min, max)
-> list에서 최대공약수를 구하거나 최소공배수를 구할 때 사용할 수 있음.
<details>
 <summary>자세한 사용법🚨</summary>
1️⃣ 리스트의 곱 구하기
 
 nums = [1,2,3,4,5]
 
 reduce(lambda x,y : x*y , nums)

 2️⃣ 문자열 연결하기

 lst = ["Hello", " ", "World", "!"]

 reduce(lambda x,y : x + y , lst )

 3️⃣ 최대 공약수(GCD) 구하기

 nums = [24, 36, 48]

 reduce(lambda x, y : math.gcd(x,y), nums )


</details>


<details>
  <summary>나온 문제🔦</summary>
<https://school.programmers.co.kr/learn/courses/30/lessons/42746#> - cmp_to_key
<https://school.programmers.co.kr/learn/courses/30/lessons/135807> - reduce
</details>
  
</details>

<details>
<summary> itertools  </summary>
  

1. Permutations
  `Permutationns(대상 집합, 몇개 선정)`

<details>
  <summary>나온 문제🔦</summary>
<https://school.programmers.co.kr/learn/courses/30/lessons/42839#>
</details>

2. chain
  여러개의 리터러블을 하나의 리터러블로 연결해주는 기능

**새로운 리스트를 생성하는게 아니라, 순차적으로 리스트를 참조하는 것이므로, 공간 효율성이 좋다.**
( + 로 연결하는 것보다 효율적이다.)


<details>
  <summary>나온 문제🔦</summary>
<https://school.programmers.co.kr/learn/courses/30/lessons/68645>
</details>
</details>

------

## 좌표

✅수학적 최적화 (원의 방정식 활용)

원에서 특정 좌표 구할 때, brute force가 아닌, 한가지 좌표를 고정하고 다른 좌표의 최소, 최대를 구하기.
위 방법은 불필요한 연산이 많으므로, 특정 𝑥에 대해 가능한 𝑦 값을 구하는 방식으로 최적화할 수 있습니다.
<details>
  <summary>나온 문제🔦</summary>
 <https://school.programmers.co.kr/learn/courses/30/lessons/140107#>
</details>
  
## 집합

<details>
  <summary> 집합 연산</summary>
 합집합 = |

<details>
  <summary>나온 문제🔦</summary>
 <https://school.programmers.co.kr/learn/courses/30/lessons/42839#>
</details>

`교집합` = &
- 중복된 것 없애기 위해서 사용

<details>
  <summary>나온 문제🔦</summary>
<https://school.programmers.co.kr/learn/courses/30/lessons/42862#>
</details>
</details>

## 오류문 해석
- TypeError: 'itertools.combinations' object cannot be interpreted as an integer
  list, dic 등이 int 처럼 더해지거나, dic의 요소로 사용되고 있다.
- ValueError: max() arg is an empty sequence
  max(iterable) 에서 iterable이 비어있다. 이럴 때에는 if iterable : 한다음에 max 처리

## 런타임 에러

- TypeError: 'int' object is not callable 👉 곱하기 했는데, () () 이런식으로, 중간에 곱하기 기호 제외하고 했음.
- TypeError: 'list' object cannot be interpreted as an integer 👉 for i in range(maps(**여기에 배열을 넣었을 수 있음**)) 
- SyntaxError: unexpected EOF while parsing 👉 안 닫힌 괄호가 있을 수 있음
## 사소하지만 중요

int(--)는 소숫점을 버리는 거거

## 다시 풀어 보자 문제들
1. https://school.programmers.co.kr/learn/courses/30/lessons/12899#

## 변수

sum대신 total, totalSum, accumulated, overall, summation

