def solution(n) :
    if n == 1 or n == 2 :
        return 1
    prev, curr = 1, 1
    for i in range(3, n+1) :
        prev, curr = curr, prev + curr
    return curr
"""
여기서, optimization은 결국, 모든 값을 dp 배열에 저장할 필요가 없기 때문에 가능하다.
결론은 하나의 값만 도출하면 되는 것이고, 그것을 계산하기 위해서 필요한 것은 결국 전값과 전전 값 그거면 되기 때문에, 
dp에 전체 값을 저장하는 것보다 이렇게 하면 ==> 공간 복잡도가 O(1)이다.


최적화는 공간 줄이기로 직접 구현해보자.
"""
