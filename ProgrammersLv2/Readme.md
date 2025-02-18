#### 변수

sum대신 total, totalSum, accumulated, overall, summation

## 1차 배열

나온 문제 :
<https://school.programmers.co.kr/learn/courses/30/lessons/92341>

## 2차 배열

나온 문제 : 
<https://school.programmers.co.kr/learn/courses/30/lessons/17679>
## Sliding Window

- 하나의 배열안에서 고정된(혹은 고정되지 않은) 끝과 끝을 따질 때

나온 문제:

## Greedy

- 스택 사용한 그리디
나온 문제 :
<https://school.programmers.co.kr/learn/courses/30/lessons/42883#>

## DP


-----
<details>
<summary> heapq</summary>

나온 문제 : <https://school.programmers.co.kr/learn/courses/30/lessons/155651>

<summary> collections </summary>

1. counter
나온 문제 : <https://school.programmers.co.kr/learn/courses/30/lessons/152996>
  
<summary> functools </summary>
  
1. cmp_to_key
res = sorted(기존 함수, key = **cmp_to*key**(비교 함수) )
비교함수 (a, b ) < 0 -> a가 b보다 앞에, 그대로 유지
비교함수 (a, b ) == 0 -> 두 값의 순서 유지
##### (양수)비교함수 (a, b ) > 0 -> b가 a보다 앞에, 순서 바꾸기

|장점|담점|
|---|---|
|비교 함수 사용 가능|비교 연산 여러번 수행, 성능 떨어짐|
|복잡한 정렬 기준이 있을 때| key를 직접 사용하는게 효율적|
|sorted, min, max 사용 가능 | |

나온 문제:
<https://school.programmers.co.kr/learn/courses/30/lessons/42746#>

</details>

<details>
<summary> itertools  </summary>
  

1. Permutations
  Permutationns(대상 집합, 몇개 선정)


나온 문제 :
<https://school.programmers.co.kr/learn/courses/30/lessons/42839#>

2. chain
  여러개의 리터러블을 하나의 리터러블로 연결해주는 기능

**새로운 리스트를 생성하는게 아니라, 순차적으로 리스트를 참조하는 것이므로, 공간 효율성이 좋다.**
( + 로 연결하는 것보다 효율적이다.)
나온 문제 : 
<https://school.programmers.co.kr/learn/courses/30/lessons/68645>
</details>

------

## 집합

<details>
  <summary> 집합 연산</summary>
 합집합 = |

 나온 문제 :
 <https://school.programmers.co.kr/learn/courses/30/lessons/42839#>
  
</details>

## 오류문 해석

## 사소하지만 중요

int(--)는 소숫점을 버리는 거거

