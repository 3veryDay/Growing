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

## 규칙 찾기

나온 문제 :
<https://school.programmers.co.kr/learn/courses/30/lessons/12899#>

-----
<details>
<summary> all </summary>
all() 함수는 반복 가능한 (iterable) 객체의 모든 요소가 True인지 확인하는 함수

- 모든 요소가 `True` => `True` 반환
- 하나라도 `False` => `False` 반환
- 빈 리스트 => `True` 반환

all(조건문 for --)
all(num % 2 == 0 for num in numbers) 
all(num % 2 for num in numbers) 하면 완전 다른 느낌
0만 False, 나머지 숫자는 True를 의미하기에, 

all(num % 2 == 0 for num in numbers) => numbers 배열의 모든 숫자가 짝수이어야지, True
all(num % 2 for num in numbers) => numbers 배열의 모든 숫자가 홀수이어야지 , True
  
<summary> heapq</summary>

나온 문제 : <https://school.programmers.co.kr/learn/courses/30/lessons/155651>

<summary> collections </summary>

1. counter
- 정말 간단한 문제이지만, 중복이 있어서, 시간 복잡도가 높아서 문제가 안 풀리는 경우가 있음. 단순한 문제에서 중복 값의 가능성이 있다면 한번 생각해보기를.

나온 문제 :
<https://school.programmers.co.kr/learn/courses/30/lessons/152996>
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

2. reduce
reduce(함수, 반복가능한_객체, 초기값)  # 초기값은 선택사항
`함수`는 두개의 값을 받아서 하나로 줄이는 연산을 수행하는 함수(ex : gcd, min, max)
-> list에서 최대공약수를 구하거나 최소공배수를 구할 때 사용할 수 있음.

나온 문제:
<https://school.programmers.co.kr/learn/courses/30/lessons/42746#> - cmp_to_key
<https://school.programmers.co.kr/learn/courses/30/lessons/135807> - reduce

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

`교집합` = &
- 중복된 것 없애기 위해서 사용


나온 문제 :
<https://school.programmers.co.kr/learn/courses/30/lessons/42862#>

</details>

## 오류문 해석

## 런타임 에러

- TypeError: 'int' object is not callable => 곱하기 했는데, () () 이런식으로, 중간에 곱하기 기호 제외하고 했음.

## 사소하지만 중요

int(--)는 소숫점을 버리는 거거

# 다시 풀어 보자 문제들
1. https://school.programmers.co.kr/learn/courses/30/lessons/12899#

## 변수

sum대신 total, totalSum, accumulated, overall, summation

