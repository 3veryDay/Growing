def solution(array, commands):
    answer = []
    for c in commands :
        start, end, num = c
        if start == end :
            answer.append(array[end-1])
        else : 
            tmp = array[start-1 : end ]
            tmp.sort()
            answer.append(tmp[num-1])
    
    return answer
