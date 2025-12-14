import sys
input = sys.stdin.readline

N = int(input())
import heapq
from collections import deque

below_zero = []
above_zero= []
zero = 0
one = 0

for _ in range(N) :
    num = int(input())
    if num > 1 :
        above_zero.append(num)
    elif num ==1 :
        one += 1
    elif num == 0 :
        zero += 1
    else :
        heapq.heappush(below_zero,(num) )
        
        
answer = 0

if len(below_zero) % 2 == 0 :
    while below_zero :
        answer += (heapq.heappop(below_zero) * heapq.heappop(below_zero))
    
else :
    while len(below_zero) != 1 :
        answer += (heapq.heappop(below_zero) * heapq.heappop(below_zero))
        
    if zero != 0 :
        below_zero.pop()
        zero -= 1
        answer += 0
    else :
        answer += below_zero.pop()

answer += one
above_zero.sort()
if len(above_zero) % 2 == 0 :
    while above_zero :
        answer += (above_zero.pop()* above_zero.pop())
        
    
else :
    while len(above_zero) != 1  :
        answer += (above_zero.pop()* above_zero.pop())
        
    answer += above_zero.pop()
    
    
print(answer)
    
