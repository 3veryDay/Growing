from collections import deque


def solution(N, K) :
    queue = deque()
    for i in range(1,N+1) :
        queue.append(i)
    
    
    while len(queue) != 1 :    
        for i in range(K-1) :
            popped_left = queue.popleft()
            queue.append(popped_left)
            # print(2, queue) 
        
        queue.popleft()
        # print(3, queue) 
    
    return(queue.popleft())
print(solution(5,2))