def solution(arr1, arr2 ) :
    i , j  = 0 , 0
    merged = []
    
    
    while i <len(arr1) and j < len(arr2) :
        if arr1[i] < arr2[j] :
            merged.append(arr1[i])
            i += 1
        else : 
            merged.append(arr2[j])
            j += 1
    if i >= len(arr1) and j >= len(arr2) :
        return merged
    
    if i >= len(arr1) :
        for tmp in range(j, len(arr2)) :
            merged.append(arr2[tmp])
    else :
        for tmp in range(i, len(arr1)) :
            merged.append(arr1[tmp])
    
    return merged

