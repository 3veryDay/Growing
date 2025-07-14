def wow(n)  :
    ans = 1
    if n == 1: 
        return 1
    for i in range(1, n+ 1) :
        ans *= i
    return ans

def solution(n) :
    #n이 짝수이면
    k = 0
    cnt = 0 
    if n % 2 == 0 :
        while n != 0 :
            n -= 2
            k += 1
            if n != 0 :
                cnt += wow(n+k) / (wow(n)*wow(k))

        return cnt + 2
    
    else :
        while n > 0 :
            n -= 2
            k += 1
            if n != 0 :
                cnt += wow(n+k) / (wow(n)*wow(k))
        return cnt + 1
    
    
print(solution(3))