def solution(array, commands) :
    res = []
    for i, j, k in commands : 
        tmp = array[i-1: j]
        tmp.sort()
        
        res.append(tmp[k-1])
    
    return res
array = [1,5,2,6,3,7,4]
commands = [ [2,5,3], [4,4,1], [1,7,3] ]

print(solution(array , commands) )