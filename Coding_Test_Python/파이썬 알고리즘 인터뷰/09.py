# 배열을 입력 받아 합으로 0을 만들 수 있는 3개의 엘레멘트를 출력하라
# 입력 : [-1, 0, 1,2, -1, -4]

# 출력  
#    [
#    [-1, 0, 1],
#    [-1, -1,]
#    ]
import time

import numpy as np

tmp = np.random.randint(-50, 50, size = 100)

#일단 너무 오래 걸려
def bruteforce ( nums ) :
    start = time.time_ns()
    nums.sort()
    answer = []
    for i in range(len(nums)-2) :
        for j in range(i+1, len(nums) - 1) :
            for k in range( j+1 , len(nums)) :
                if nums[i] + nums[j] + nums[k] == 0 :
                    sequential = [nums[i], nums[j], nums[k]]
                    if sequential not in answer:    
                        answer.append(sequential)
                        
    print(time.time_ns() - start)                
    return  len(answer)

print(bruteforce(tmp))
print("****************************")

def leftTwoPointer( nums ) :
    start = time.time_ns()
    answer = []
    nums.sort()
    
    for center in range(len(nums)-2) :
        # 전 center 값값에서 고려됐을 거기에 고려할 필요 없음음
        if center != 0  and nums[center] == nums[center -1] :
            continue
        left, right = center + 1, len(nums) -1
        while left < right :
            if nums[left] + nums[right] + nums[center] == 0 and [nums[center], nums[left], nums[right]] not in answer :
                answer.append([nums[center], nums[left], nums[right]] )
            
            if nums[left] + nums[right] + nums[center] < 0:
                
                left += 1
            else :
                right -= 1
    print(time.time_ns() - start)            
    return len(answer)
    
print(leftTwoPointer(tmp))
print("****************************")


def qleftTwoPointer( nums ) :
    start = time.time_ns()
    answer = []
    nums.sort()
    
    for center in range(len(nums)-2) :
        # 전 center 값값에서 고려됐을 거기에 고려할 필요 없음음
        if center != 0  and nums[center] == nums[center -1] :
            continue
        left, right = center + 1, len(nums) -1
        while left < right :
            if nums[left] + nums[right] + nums[center] == 0 and [nums[center], nums[left], nums[right]] not in answer :
                answer.append([nums[center], nums[left], nums[right]] )
            
            if nums[left] + nums[right] + nums[center] < 0:
                if nums[left] == nums[left + 1] :
                    while nums[left] == nums[left + 1 ] :
                        left += 1
                else :
                    left += 1
            else :
                if nums[right] == nums[right - 1] :
                    while nums[right] == nums[right - 1 ] :
                        right -= 1
                else :
                    right -= 1
    print(time.time_ns() - start)            
    return len(answer)
    
print(qleftTwoPointer(tmp))