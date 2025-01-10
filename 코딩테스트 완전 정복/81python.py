def solution(items, weight_limit) :
    
    for i, d in enumerate(items) :
        items[i][1] = d[1]/d[0]
    
    items.sort(key = lambda x : x[1], reverse = True)
    
    total_value_in_bag = 0 
    
    for weight, value in items:
        if weight_limit == 0:
            break;
        if weight_limit >= weight :
            total_value_in_bag += weight * value
            weight_limit -= weight
        elif weight_limit <= weight :
            total_value_in_bag += weight_limit * value
            weight_limit -= weight
            
    return total_value_in_bag
            
        
        
        
print(solution([[10,19], [7,10], [6,10]], 15))