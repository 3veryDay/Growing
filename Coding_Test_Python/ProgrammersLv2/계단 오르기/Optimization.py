"""
이미 풀어봤기 때문에,

이는 dp를 전체를 저장할 필요 없이, 전 값과 전전 값만 알면 됨에서 나올 수 있는 최적화 코드이다.

"""

def solution(n) :
    if n <= 3:
        return n
    prev, curr = 1,2 
    for _ in range(n - 2) :
        prev, curr = curr,( prev + curr) % 1234567
        
    return curr
