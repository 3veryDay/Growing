N, M = map(int, input().split())
videos = list(map(int, input().split()))

def get(n) :
    if n < max(videos) :
        return M+1
    cnt = 0
    one_ray = 0
    for video in videos:
        if one_ray + video > n :
            one_ray = video
            cnt += 1
        else :
            one_ray += video

    return cnt + 1
def solve() :
    l, r = 1, sum(videos) + 1
    
    while l < r :
        m = (l + r) // 2
        if get(m) <= M :  # 참이면 왼쪽
            r = m
        else :
            l = m + 1
    return l

print(solve())
