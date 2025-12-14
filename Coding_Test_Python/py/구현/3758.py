import sys

input = sys.stdin.readline

# 테스트 케이스 개수
t = int(input())

for _ in range(t) :
    # 팀 개수 n, 문제 개수 k, 내 팀 ID t, 로그 엔트리 개수 m
    n, k, t, M = map(int, input().split())
    # 제출 정보를 담은 submit
    submit = []
    scores = [[0]*k for _ in range(n)] # 팀당 점수
    submit_cnt = [0] * (n)  # 팀당 제출 횟수
    last_submit = [-1] * (n)  # 팀당 마지막 제출 idx
    for m in range(M) :
        # 제출되는 순서대로 정보 ID, 문제번호, 점수
        i, j, s = map(int, input().split())
        i-=1
        j-=1
        
        # 제출 된 문제라면 갱신
        scores[i][j] = max(scores[i][j] , s)
        submit_cnt[i] += 1
        last_submit[i] = m

    # dashboard에 score, 제출 횟수, 마지막 제출 시간을 저장해서 sort()했을 때 순위가 뜨도록
    dashboard = []
    for idx in range(n) :
        score = sum(scores[idx])
        dashboard.append([-score, submit_cnt[idx], last_submit[idx], idx])
    dashboard.sort()
    
    for place in range(n) :
        if dashboard[place][3] == t -1 :
            print(place + 1)
            break
