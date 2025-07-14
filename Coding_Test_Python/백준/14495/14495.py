n = int(input())
lst = [0] * (n+1)
if n == 1 or n == 2 or n == 3 :
    print(1)
else : 
    lst[1], lst[2], lst[3] = 1,1,1
    for idx in range(4, n+1) :
        lst[idx] = lst[idx-1] + lst[idx -3]
    
    print(lst[n])


    
