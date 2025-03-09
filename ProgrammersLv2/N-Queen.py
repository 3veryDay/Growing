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
