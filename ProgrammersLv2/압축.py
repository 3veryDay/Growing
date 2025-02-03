'''
A -> 65 ord('A')

65 -> A chr(65)

'''


from collections import deque


def solution(msg) :
    q = deque(msg)

    dict = {}
    for i in range(65, 65+ 26 ) :
        dict[chr(i)] = i-64
        
    answer = []
    last = 27
    while q :
        string = q.popleft()
        if not q :
            answer.append(dict[string])
            break
        if string+q[0] not in dict :
            answer.append(dict[string])
            dict[string + q[0]] = last
            last += 1
        else : 
            string += q.popleft()# string 이 dict.keys()에 있는 경우
            while q :
                if string + q[0] not in dict :
                    break;
                string += q.popleft()
            answer.append(dict[string])
            if q :
                dict[string + q[0]] = last
            
            last += 1
        
    return answer
