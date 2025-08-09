'''
N개의 랜선을 만들어야 해.

K개의 랜선을 가지고 있지만, 길이가 제각각
랜선을 모두 N개의 같은 길이의 랜선으로 만들고 싶음.
자른 랜선은 붙이는 건 불가능

자를 떄는 정수 길이 만큼


'''    
def cut(cable, length ) :
    return cable // length

def cut_cables(length) :
    cnt = 0
    for c in cables :
        cnt += cut(c, length)
    return cnt

def solve() :
    # N을 하나 뺴기 떄문에 N이 1인 경우 처리
    if K == 1 :
        return cables[0] // N

    l, r = 1, sum(cables) //N + 1
    while l < r :
        m = (l + r) //2
        if cut_cables(m) > N-1 :
            l = m + 1
        else :
            r = m
    return l-1


import sys

input = sys.stdin.readline
# 가지고 잇는 랜선 수는 k, 필요한 랜선 수는 n
K, N = map(int, input().split())
cables  = []
for _ in range(K) :
    cables.append(int(input()))
    
print(solve())
