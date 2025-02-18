def solution(storey) :
    
    cnt = 0
    s = storey
    if s < 5 :
        return s
    
    
    while s != 0 :
        print(s, cnt)
        if str(s)[-1] != '0' :
            one = int(str(s)[-1])
            two = -1
            if s > 9 : two = int(str(s)[-2])
            if one < 5  :
                s -= one
                cnt += one
                
            elif one > 5 :
                s += (10-one)
                cnt += (10 - one)
            else :  # one이 5일때
                if two >= 5 :
                    s += (10-one)
                    cnt += (10 - one)
                else :
                    s -= one
                    cnt += one
                
        s //= 10
    return cnt
        
            


'''

def solution(storey):
    if storey < 10 :
        return min(storey, 11 - storey)
    left = storey % 10
    return min(left + solution(storey // 10), 10 - left + solution(storey // 10 + 1))

'''
        
        
