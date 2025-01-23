# 자신을 제외한 배열의 곱

# 배열을 입력 받아 output[i]가 자신을 제외한 나머지 모든 요소의 곱셈 결과가 되도록 출력하라

# 입력 [ 2,3,4, 5 ]
# 출력 [60, 40, 30, 24
# ]

# 주의

import time

# 나눗셈을 하지 않고 O(N)에 풀이하라.
import numpy

tmp = numpy.random.randint(1,10, 100)

def basic( nums ):
    start = time.time_ns()
    answer = []
    left = [1 for _ in range(len(nums))]
    right = [1 for _ in range(len(nums))]
    
    for i in range(1, len(nums)) :
        
        left[i] = left[i-1]* nums[i-1]
        right[len(nums) - i - 1] = right[len(nums) - i ]*nums[len(nums)-i]
        print("i = " , i, left[i], right[len(nums) - i - 1])
    print(nums)  
    print(right, left)
    for idx in range(len(nums) ) :
        answer.append(left[idx] * right[idx])
    print(time.time_ns() - start)
    return answer

print(basic(tmp))
print("****************")
def paper(nums ) :
    out = []
    p = 1
    
    for i in range(len(nums)) :
        out.append(p)
        p = p * nums[i]
        
    p = 1
    
    for i in range(len(nums ) - 1, 0 - 1, -1) :
        out[i] = out[i] * p
        p = p * nums[i]
        
    return out

print(paper(tmp))