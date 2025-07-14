def solution(s) :
    s = s[2:-2].split("},{")
    s = sorted(s, key= len)
    answer = []
    
    for element in s :
        numbers = element.split(',')
        
        for number in numbers :
            if int(number) not in answer :
                answer.append(int(number))
                
    return answer

s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
print(solution(s))