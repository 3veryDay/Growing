def solution(t) :
    if t == 1 or t == 2 :
        return 1
    
    return solution(t-1) + solution(t-2)
"""
이 경우의 문제점은
fibonacci_recursive(5)
├── fibonacci_recursive(4)
│   ├── fibonacci_recursive(3)
│   │   ├── fibonacci_recursive(2)
│   │   ├── fibonacci_recursive(1)
│   ├── fibonacci_recursive(2)
├── fibonacci_recursive(3)
│   ├── fibonacci_recursive(2)
│   ├── fibonacci_recursive(1)

이와 같이, n이 매우 작은 값이더라도 n이 1,2,3 인 경우 이미 값을 구했는데도, 또 다시 구하기 때문에, 시간 복잡도가 매우 높다.

반복적인 계산, 중복되는 부분 문제가 보이기 때문에, 이는 dp를 생각해 낼 수 있다.
"""
