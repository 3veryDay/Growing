def solution(s) :
    count_zero = 0
    count_transform = 0
    
    while s != '1' :
        count_transform += 1
        
        count_zero += s.count("0")
        
        s = bin(s.count("1"))[2:]
    return [count_zero, count_transform]

print(solution("01110"))