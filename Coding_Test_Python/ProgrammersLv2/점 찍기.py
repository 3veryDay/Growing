# 1,000,000 일 떄는 시간 복잡도를 O(n**2) 면 안됨!

from math import sqrt
def solution(k, d):
    answer = 0
    for x in range(0, d+1) :
        if x % k == 0 :
            max_y = sqrt(d**2 - x**2)
            answer += (max_y // k + 1)
    return answer
