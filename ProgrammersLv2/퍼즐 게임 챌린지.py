def solution(diffs, times, limit):
    def calculate(level) :
        lst = zip(diffs, times)
        total_time = 0
        time_prev = 0
        for idx, l in enumerate(lst) :
            difficulty, time = l
            time_prev = times[idx-1] + times[idx]
            if difficulty <= level :
                total_time += time
                continue
            else :
                total_time += (difficulty - level) * time_prev + time
            print(f'diff : {difficulty} time : {time} time_prev : {time_prev} total_time : {total_time}')
            if total_time > limit :
                print(total_time, limit)
                return -1
        return total_time
    left, right, mid = 0,max(diffs), max(diffs)//2
    answer = limit
    while  left <= right :
        tmp = calculate(mid)
        print("*****", left, right,mid, tmp)
        if tmp == -1 :
            left = mid + 1
            mid = (left + right) // 2
        else :
            if tmp < answer :
                right_cal = calculate(right)
                if right_cal!= -1 and right_cal < tmp :
                    answer = right
                right = mid -1
                answer = mid
                mid = (left + right) // 2
    return answer
