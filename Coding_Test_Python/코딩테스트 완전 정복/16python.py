from collections import deque


def solution(progresses, speeds) :
    
    queue = deque(progresses)
    speed = deque(speeds)
    
    answer = []
    cnt = 0
    while queue:
        
        for i in range(len(queue)) :
            cnt = 0
            queue[i] += speed[i]
        print(queue)
        if queue[0] >= 100 :
            print(queue)

            while queue and queue[0] >= 100 :
                queue.popleft()
                speed.popleft()
                cnt += 1
            answer.append(cnt)
    return answer

print(solution([95,90,99,99,80,99], [1,1,1,1,1,1]))