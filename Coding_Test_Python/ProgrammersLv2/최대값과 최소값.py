def solution(s):
    arr =[]
    for num in s.split() :
        arr.append(int(num))

    answer = ''
    
    answer += str(min(arr)) + " "
    answer += str(max(arr))
    
    return answer

"""
str에서 max, min을 따지면 절대값으로 따져진다.
즉, int 처리를 하지 않으면
str(-1000000) > str(1) 이게 성립한다.

항상 int 처리를 해야지 정확하게 처리할 수 있다.


"""
