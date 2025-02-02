


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
    
    
'''
1. key pop
dic.pop('key')
del dic[key]

dic.popitem() : 딕셔너리의 마지막 항목을 제거하고, 그 항목을 튜플로 반

두개 이상의 딕셔너리를 병합할 때 update() 메소드 사용 가능
dict 1, dict2가 있을 때. 
dict1.update(dict2)

merged = dict1 | dict2  3.9 이상 사용 가능 


'''
