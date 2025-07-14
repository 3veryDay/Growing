def solution(data, col, row_begin, row_end):
    f = sorted(data, key = lambda x : (x[col-1], -x[0]))
    S = []
    for idx in range(row_begin, row_end + 1 ) :
        sum =0
        for d in f[idx-1] :
            sum += (d % idx)
        S.append(sum)
    answer = 0
    for s in S :
        answer ^= s
    return answer


"""
e다른 사람 풀이 
"""
from functools import reduce

def solution(data, col, row_begin, row_end):
    data.sort(key = lambda x : (x[col-1], -x[0]))
    return reduce(lambda x, y: x ^ y,
                  [sum(map(lambda x: x%(i+1), data[i])) for i in range(row_begin-1, row_end)])
