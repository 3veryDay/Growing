
예를 들어, "스택을 활용하는 문제"를 풀 때 자주 나오는 패턴을 정리해 봐.
"스택의 top을 확인하는 방식이 중요하다."
"while 문을 활용해 연속적으로 pop하는 방식이 자주 나온다."

## 변수

sum대신 total, totalSum, accumulated, overall, summation

나온 문제:

## Sliding Window

- 하나의 배열안에서 고정된(혹은 고정되지 않은) 끝과 끝을 따질 때

나온 문제:

## Greedy

- 스택 사용한 그리디
나온 문제 :
<https://school.programmers.co.kr/learn/courses/30/lessons/42883#>


-----
<details>
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
</details>

------
집합
<details>
  <summary> 집합 연산</summary>
 합집합 = |

 나온 문제 :
 <https://school.programmers.co.kr/learn/courses/30/lessons/42839#>
  
</details>
