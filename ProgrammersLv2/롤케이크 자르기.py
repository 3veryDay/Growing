


# Counter로 하겠다(15분 경과 후) 
from collections import Counter, defaultdict
def solution(topping) :
    bro = dict(Counter(topping))
    sis = defaultdict(int)
    cnt = 0
    for top in topping :
        bro[top] -= 1
        if bro[top] == 0 :
            bro.pop(top)
        sis[top] += 1
        
        if len(bro) == len(sis) :
            cnt += 1
            
    return cnt
    
    
