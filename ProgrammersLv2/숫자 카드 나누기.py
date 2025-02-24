import math

def solution(arrayA, arrayB) :
    #[10, 17] , 5 가 들어갔을 때 -> False가 나옴
    #    10                         
    def check(array, num) :
        status = 0  #시작 전
        for a in array :
            
            if a % num == 0 :
                if status == 0 or status == 1:
                    status = 1 # 나눌 수 있음!
                    continue
                else :
                    status = -1 #이도저아님.
                    return status
            else :
                if status == 0 or status == 2 :
                    status = 2 #나눌 수 없음!
                    continue
                else :
                    status = -1 
                    return status
        return status
    
    
    answer = 0
    
    a = min(arrayA)
    b = min(arrayB)
    a_yak = []
    b_yak = []
    for i in range(1, int(math.sqrt(a)) + 1) :
        if a % i == 0 : 
            a_yak.append(i)
            a_yak.append(a//i)
    for i in range(1, int(math.sqrt(b))+ 1 ) :
        if b % i == 0 :
            b_yak.append(i)
            b_yak.append(b//i)
    A = sorted(a_yak)[::-1]
    B = sorted(b_yak)[::-1]
    A.remove(1)
    B.remove(1)
    
    
    tmp = 0
    #A부터
    for a in A :
        if check(arrayA, a) == 1 :
            if check(arrayB, a) == 2 :
                # print("\n*", arrayA, arrayB, a)
                tmp = a
                break

    for b in B :
        if check(arrayB, b) == 1:
            if  check(arrayA, b ) == 2:
                # print("\n**", arrayA, arrayB, b)
                if b > tmp :
                    return b
                else :
                    break
    return tmp
        
        
    
    
