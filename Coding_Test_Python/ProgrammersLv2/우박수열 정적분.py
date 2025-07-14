def solution(k, ranges):
    lst = [k] 
    def calculate(start, end, n ) :
        total = 0
        if start == n + end :
            return 0
        if start > n + end :
            return -1
        for i in range(start, n + end) :
            total += (lst[i] + lst[i+1])/2
        return total
    
    while k != 1 :
        if k % 2 == 0 :
            k //= 2
        else :
            k = k* 3 + 1
        lst.append(k)
    dp = []
    answer = []
    for r in ranges :
        start, end = r
        answer.append(calculate(start, end ,len(lst)-1))
    return answer

def solution(k, ranges):
    lst = [k] 
    dp = {}
    def calculate(start, end, n ) :
        total = 0
        if start == n + end :
            return 0
        if start > n + end :
            return -1
        if (start, end) in dp :
            return dp[(start, end)]
        for i in range(start, n + end) :
            total += (lst[i] + lst[i+1])/2
        dp[(start, end)] = total
        return total
    
    while k != 1 :
        if k % 2 == 0 :
            k //= 2
        else :
            k = k* 3 + 1
        lst.append(k)
    dp = {}
    answer = []
    for r in ranges :
        start, end = r
        answer.append(calculate(start, end ,len(lst)-1))
    return answer
