from collections import deque
def solution(skill, skill_trees):
    cnt = 0
    
    for user in skill_trees :
        q = deque(skill)
        possible = []
        condition = True
        for u in user :
            if u in q and u == q[0] :
                possible.append(q.popleft())
            
            if u in q and u != q[0] :
                if u not in possible :
                    condition = False
        if condition is True :
            cnt += 1
    return cnt
    
    
    
    answer = -1
    return answer
