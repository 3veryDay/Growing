def solution(n, info) :
    
    score_diff = -1
    answer = []
    def backtrack(path, apeach_score, frodo_score, current_frodo_shots, idx, score_diff) :
        if idx > 10 :
            return
        if current_frodo_shots > n :
            return False
        if frodo_score > apeach_score and current_frodo_shots <= n :
            
        for choice in (0, info[idx]+ 1) :
            path[idx] = choice
            
            if choice == 0 :
                apeach_score += (10 - idx)
                backtrack(path, apeach_score, frodo_score,current_frodo_shots, idx + 1, score_diff )
                apeach_score -= (10 - idx)
            else :
                frodo_score += (10- idx)
                current_frodo_shots += (info[idx]+ 1)
                path[idx] = (info[idx]+ 1)
                backtrack(path, apeach_score, frodo_score,current_frodo_shots, idx + 1, score_diff )
                frodo_score -= (10 - idx)
                current_frodo_shots -=( info[idx] + 1)
                path[idx] = 0

    path = [0]*11
    backtrack(path, 0, 0, 0, 0,-1)
    
    return path
    
print(solution(5, 	[2,1,1,1,0,0,0,0,0,0,0]))