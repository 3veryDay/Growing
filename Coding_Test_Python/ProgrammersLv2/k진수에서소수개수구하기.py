from math import sqrt
from collections import deque
def solution(n, k):
    def convert(n, k) :
        if n == 0 :
            return 0
        res = []
        
        while n != 0 :
            
            res.append(str(n % k))
            n = n // k
        return ''.join(reversed(res))
    
    
    def check_sosu(num) :
        if num == 1 :
            return False
        elif num == 2 or num == 3 :
            return True
        elif num % 3 == 0 or num % 2 == 0 :
            return False
        for i in range(5, int(sqrt(num)) + 1, 2 ) : # 정수 변환 필수
            if num % i == 0 :
                return False
        return True
    
    convert_result = convert(n,k)       
    
    q = deque()
    cnt = 0
    for s in str(convert_result) :
        if int(s) != 0  :
            q.append(s)
        if int(s) == 0 and q :
            tmp = ''
            while q :
                tmp += q.popleft()
            
            tmp = int(tmp)
            if check_sosu(tmp) :
                cnt += 1
    if q :
        tmp = ''.join(q)
        tmp = int(tmp) 
        if check_sosu(tmp) :
            cnt += 1
    return cnt
        
                
'''
ValueError: invalid literal for int() with base 10: ''
'' 를 int 변환 시도 했다

빈 문자열을 int로 변환하면 다음과 같은 에러가 뜬다.
체크 하는 습관 기르기.
'''
        
