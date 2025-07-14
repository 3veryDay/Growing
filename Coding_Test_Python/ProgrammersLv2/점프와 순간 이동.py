def solution(n):
    ans = 0
    # 거리*2 => 베터리 사용 안함
    # 거리 + 1 => 베터리 사용함 
    
    '''
    0 124 5
    0 12 36
    0
    
    '''
    cnt = 0
    while n!= 0 :
        if n %2 == 0 :
            n //= 2
        else :
            n -= 1
            cnt += 1
    return cnt
