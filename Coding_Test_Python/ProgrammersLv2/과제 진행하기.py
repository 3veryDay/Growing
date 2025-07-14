from collections import deque
def solution(plans):
    plans.sort(key = lambda x : x[1])
    answer = []
    def time_change(string) :
        return 60*int(string[:2]) + int(string[3:])
    plans = deque(plans)
    q = []
    while plans :
        name, start, time = plans.popleft()
        start = time_change(start)
        time = int(time)
        end = start + time
        if not plans :
            end = time_change("23:99")
        if plans :
            next_start = time_change(plans[0][1])
        if plans and end > next_start :
            q.append([name, end - next_start]) #name, remaining time
        elif end == next_start :
            answer.append(name) 
            continue
        else :
            
            answer.append(name)
            if not q :
                continue
            name, time = q.pop()
            remaining_time = next_start - end
            while remaining_time != 0 :
                time -= 1
                if time == 0   :
                    answer.append(name)
                    if q :
                        name, time = q.pop()
                    else :
                        break
                remaining_time -= 1
            if time != 0 :
                q.append([name, time])
                
        
    return answer



'''
다른 멋ㅈ?ㅣㄴ 풀이 
'''
def solution(plans):
    plans = sorted(map(lambda x: [x[0], int(x[1][:2]) * 60 + int(x[1][3:]), int(x[2])], plans), key=lambda x: -x[1])

    lst = []
    while plans:
        x = plans.pop()
        for i, v in enumerate(lst):
            if v[0] > x[1]: 
                lst[i][0] += x[2]
        lst.append([x[1] + x[2], x[0]])
    lst.sort()

    return list(map(lambda x: x[1], lst))
  # 여기서는 answer에 하나씩 append하는게 아니라, 끝나는 시간을 그냥 lst에 추가하고, 이걸 나중에 sort 하는 걸로
