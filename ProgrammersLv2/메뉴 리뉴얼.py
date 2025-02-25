from collections import defaultdict
from itertools import combinations 
def solution(orders, course):
    answer = []
    for num in course :
        dic = defaultdict(int)
        for order in orders :
            combin = combinations(order, num)
            for comb in combin :
                dic[''.join(sorted(list(comb)))] += 1
        sorted_dic = dict(sorted(dic.items(), key = lambda x : x[1], reverse = True))
        if sorted_dic :
            m = max(sorted_dic.values())
            if m == 1 :
                break
            for item, menu in sorted_dic.items() :
                if menu == m :
                    answer.append(item)
                else :
                    break
            
        
        
        
            
    answer.sort()   
    return answer


from collections import defaultdict, Counter
from itertools import combinations 
def solution(orders, course):
    answer = []
    for num in course :
        combin = []
        pre = []
        for order in orders :
            combin.extend(combinations(''.join(sorted(list(order))), num))
        lst = Counter(combin).most_common()
        print(lst)
        pre += [k for k, v in lst if v > 1 and v == lst[0][1]]
        
        for p in pre :
            answer.append(''.join(p))
        
        
            
    answer.sort()   
    return answer

# my answer
from collections import defaultdict, Counter
from itertools import combinations 
def solution(orders, course):
    answer = []
    for num in course :
        combin = []
        pre = []
        for order in orders :
            combin.extend(combinations(''.join(sorted(list(order))), num))
        lst = Counter(combin).most_common()
        print(lst)
        pre += [k for k, v in lst if v > 1 and v == lst[0][1]]
        
        for p in pre :
            answer.append(''.join(p))
        
        
            
    answer.sort()   
    return answer

