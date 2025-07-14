from collections import deque
def solution(queue1, queue2):
    q1, q2 = deque(queue1), deque(queue2)
    s1, s2 = sum(q1), sum(q2)
    cnt = 0
    lim = len(q1)
    
    if (s1 + s2) % 2 != 0 :
        return -1
    
    #answer_limit = queue1.size() * 2 + 1;
    while s1!= s2 and cnt <= lim*3 + 1:
        if s1 > s2 :
            item = q1.popleft()
            q2.append(item)
            
            s1 -= item
            s2 += item
            cnt += 1
        else :
            item = q2.popleft()
            q1.append(item)
            
            s2-= item
            s1 += item
            cnt += 1
        print(q1, q2 )
    print(cnt)    
    # if cnt > lim*2  :
    #     return -1
    # else :
    #     return cnt
