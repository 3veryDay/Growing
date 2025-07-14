'''
맨땅에 해딩, 점수 :80 
시간초과!
'''

from itertools import permutations
def solution(n):
    answer = 0
    lsts = permutations([i for i in range(n)])
    for lst in lsts :
        #lst = (0,1,2,3)
        left = [0]*(2*n-1)
        right = [0]*(2*n-1)
        status = 0
        for idx, val in enumerate(lst) :
            if left[idx + val] != 0 or right[val-idx+n-1]!= 0 :
                status = 1
                break
            left[idx + val],  right[val-idx+n-1] = 1, 1
        if status == 0 :
            answer += 1
    return answer
'''
백트래킹으로 했어야 함
내일은 백 트래킹 연습하자/.
'''

def getAns(n, y, garo, left, right):
    ans = 0
    #y는 순차적으로 늘리는 애
    
    # 모든 행에 대해서 다 구했을 때
    if y == n :
        ans += 1
    else :
        for i in range(n) :
            if garo[i] or left[i+y] or right[i-y+n] :
                continue
            garo[i]  =left[i+y] = right[i-y+n]=True
            ans += getAns(n, y+1, garo, left, right)
            garo[i] = left[i+y] = right[i-y +n] = False
    return ans

def solution(n) :
    ans = getAns(n, 0, [False]*n , [False]*(2*n), [False]*(2*n))
    return ans
    
