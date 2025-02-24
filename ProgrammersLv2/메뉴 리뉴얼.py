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

#TypeError: 'itertools.combinations' object cannot be interpreted as an integer

#alueError: max() arg is an empty sequence

#sorted_dict = dict(sorted(data.items(), key=lambda x: x[1]))
