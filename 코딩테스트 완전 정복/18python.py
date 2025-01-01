def solution(arr, target) :

    for a in arr : 
        print("new a", a)
        if target//2 == a:
            continue;
        if (target - a) in arr :
            
            return True;
    return False

print(solution([2,3,5,7,9], 10))