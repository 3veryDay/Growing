"""
dic key, value를 서야하는데
if a != dic[tmp] :
                    return 0

여기서 a != tmp 으로 해서 몇 분을 날림.
dic을 사용할 때는 key, value 조금 더 주의하자
"""

from collections import deque
def solution(s):
    
    if len(s) % 2 != 0 :
        return 0
    
    
    dic = {}
    dic['{'] = '}'
    dic['('] = ')'
    dic['['] = ']'
    
    def check(arr) :
        q = []
        
        for a in arr :
            if a in dic.keys() :
                q.append(a)
            else :
                if len(q) == 0:
                    return 0
                tmp = q.pop()
                if a != dic[tmp] :
                    return 0
                elif a == dic[tmp] :
                    continue
                
        return 1
    ss = deque(s)
    count = 0
    for _ in range(len(s)) :
        count += check(ss)
        ss.append(ss.popleft())
        
    return count
