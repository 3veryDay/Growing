
def solution(n):
    answer = 0
    cnt = 0
    for start in range(1, n+1) :
        total = 0
        for end in range(start, n+1) :
            total += end
            if total == n :
                cnt +=1
            if total > n :
                break
                
    return cnt
