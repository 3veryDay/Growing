def solution(n) :
    n = str(n)
    res = sorted(n,reverse = True)
    
    return ''.join(res)
n = 123456774499
print(solution(n))