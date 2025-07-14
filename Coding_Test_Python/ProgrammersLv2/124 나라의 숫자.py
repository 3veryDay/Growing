def change(num : str ) -> str :
    n = int(num)
    r = ''
    while n != 0 :
        if n % 3 != 0 :
            tmp = n % 3 
            n //= 3
            r += str(tmp)
        else :
            n //= 3
            n -=1
            r += '4'
    
    return r[::-1]
def solution(num) :
    three = change(str(num)) 
    return str(three)
