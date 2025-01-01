from collections import Counter


def solution(toppings) :
    
    cnt = 0
    Tom = set()
    Jerry = Counter(toppings)
    for topping in toppings :
        if topping not in Tom :
            Tom.add(topping)
        
        Jerry[topping] -= 1
        
        if Jerry[topping] == 0 :
            Jerry.pop(topping)
            
        if len(Jerry) == len(Tom) :
            cnt += 1
            
    return cnt

print(solution([1,2,3,1,4]))
        