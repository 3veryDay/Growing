def solution(n,a,b):
    round_count = 1
    
    while True :
        a = (a-1)//2 + 1
        b = (b-1)//2 + 1
        
        if a == b :
            return round_count
        else :
            round_count += 1
"""
일단 10분만에 풀기는 햇지만, 더 생각해보자.
그냥 이게 다른 사람들 풀이랑 비슷함.
a, b = (a+1)//2, (b+1)//2
로 단순하게 표현하는 것도 있었다.

다른 사람들의 풀이 중에서
def solution(n,a,b):
    return ((a-1)^(b-1)).bit_length()
"""
