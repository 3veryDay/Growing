def solution(nums) :
    n = len(nums) // 2
    nums_s = set(nums)
    n_s = len(nums_s)
    
    if n_s <= n :
        return n_s
    else:
        return n
    
print(solution([3,3,3,2,2,2]))