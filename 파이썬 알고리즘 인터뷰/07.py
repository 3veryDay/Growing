nums = [2,7,11,15]
target = 9

# 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라
## 출력은 [0,1]

def sum_bruteforce(nums, target) :
    answer = []
    for i in range(len(nums) - 1) :
        for j in range(i+1, len(nums)) :
            if nums[i] + nums[j] == target :
                answer.append([i,j])
                
    return answer

def sum_bruteforce_backtrack(nums, target) :
    answer = []
    for i in range(len(nums) - 1) :
        if nums[i] >= target :
            continue
        for j in range (i, len(nums)) :
            if nums[j]>=target : 
                continue
            if nums[i] + nums[j] == target :
                answer.append([i,j])