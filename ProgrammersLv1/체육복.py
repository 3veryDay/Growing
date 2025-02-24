'''


5, [2, 3], [3, 4]
'''

def solution(n, lost, reserve) :
    
    if len(lost) < len(reserve) :
        for l in lost :
            if l in reserve :
                lost.remove(l)
                reserve.remove(l)
    else :
        for r in reserve :
            if r in lost :
                lost.remove(r)
                reserve.remove(r)
    
    
    answer = n - len(lost)
    
    lost.sort()
    
    for l in lost :
        if l in reserve :
            reserve.remove(l)
            answer += 1
        elif (l-1) in reserve :
            reserve.remove(l-1)
            answer += 1
        elif (l+1) in reserve :
            reserve.remove(l+1)
            answer += 1
    return answer
