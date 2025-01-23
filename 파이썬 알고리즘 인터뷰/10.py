# n 개의 페어를 이용한 min( a, b ) 의 합으로 만들 수 있는 가장 큰 수 

# 입력  : [1,4,3,2] => [1,2,3,4]
# 출력 : 4

# 설명
# n 은 2가 되며 최대 합은 4이다. 
# min(1,2) + min(3,4) = 4

import time

import numpy as np

tmp = np.random.randint(0,50, 100000)

def basic( nums ) :
    start = time.time_ns()
    nums.sort()
    sum = 0
    if len(nums) % 2 == 0 :
        i = 0
        while i < len( nums ) :
            sum += nums[i]
            i += 2
            
    else :
        sum += nums[1]
        i = 3
        while i < len(nums) :
            sum += nums[i]
            i += 2
    print(time.time_ns() - start)
    return sum
print(basic(tmp))
print("********")

def pythonic( nums ) :
    start = time.time_ns()
    nums = sorted(nums, reverse= True)
    print(time.time_ns() - start)
    return  sum(val for i, val in enumerate(nums[:-1]) if i % 2 == 1)

def realPythonic(nums) :
    return sum(nums[::2])
print(pythonic(tmp))
print(realPythonic(tmp))
