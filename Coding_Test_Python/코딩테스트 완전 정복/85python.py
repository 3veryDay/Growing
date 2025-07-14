def solution(N ,stations ,W) :
    answer = 0
    location = 1
    idx = 0
    
    while location <= N :
        if idx< len(stations) and location >= stations[idx] - W :
            location = stations[idx] + W + 1
            idx += 1
            
        else :
            location += 2 * W + 1
            answer += 1
            
    return answer