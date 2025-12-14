### 에라토스테네스의 체 개념

소수 찾기 알고리즘으로
1. 2배수 다 지우기
2. 3배수 다 지우기
3. 그 다음 남아있는 5, 7... 순으로 진행해서
4. sqrt(N)까지만 확인
=> 결과적으로 모든 남은 수는 소수라고 볼 수 있음.


기본 알고리즘 틀
```python
def sieve(n) :
  prime = [True] * (n + 1)
  prime[0] = prime[1] = False  # 0과 1은 소수가 아님

  for i in range(2, int(n**0.5) + 1 ) :
    if prime[i] :
      for j in range(i * i, n+1, i ) :
        prime[j] = False
  return [i for i, is_prime in enumerate(prime) if is_prime]
```
