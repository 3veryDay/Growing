from math import gcd

def solution(num) : 
    answer = num[0]
    
    for n in num :
        answer = (n * answer) // gcd(n, answer)
    return answer
