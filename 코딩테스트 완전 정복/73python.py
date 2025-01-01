def solution(n) :
    if n == 3 :
        return 3
    arr = [0,1,1]
    
    for i in range(3, n + 1) :
        arr.append(arr[i-1] + arr[i-2])
        
    return arr[n] % 1234567

print(solution(5))
        
        