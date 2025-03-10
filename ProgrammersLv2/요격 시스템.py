# 시간 초과 -> BFS는 아님

'''
1 ≤ targets의 길이 ≤ 500,000
targets의 각 행은 [s,e] 형태입니다.
이는 한 폭격 미사일의 x 좌표 범위를 나타내며, 개구간 (s, e)에서 요격해야 합니다.
0 ≤ s < e ≤ 100,000,000
'''

from collections import deque

def solution(targets) :
    q = deque()
    missiles = []
    idx = 0
    q.append([missiles, idx])
    targets.sort()
    answer = 10000000
    while q :
        missiles, idx = q.pop()
        # print(idx, missiles)
        if idx == len(targets):
            answer = min(answer, len(missiles))
            return answer
            
        #missiles가 비어있을 경우
        if not missiles :
            for loc in range(targets[idx][0], targets[idx][1]) :
                q.append([missiles + [loc], idx + 1])
            continue
        if targets[idx][0] < missiles[-1] +0.5 < targets[idx][1] :
            q.append([missiles, idx+1])
        else :
            for loc in range(targets[idx][0], targets[idx][1]) :
                q.append([missiles+[loc], idx + 1])
    return answer
