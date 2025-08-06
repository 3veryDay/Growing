import sys

input = sys.stdin.readline
from collections import Counter, defaultdict


def get_winner(runners, n) :
    team_cnt = defaultdict(int)
    score = defaultdict(int)
    fifth_ = {}
    score_cnt = defaultdict(int)
    for idx, runner in enumerate(runners) :
        team_cnt[runner] += 1
        
        # 5번째 들어온 사람의 idx 저장
        if team_cnt[runner] == 5 :
            fifth_[runner] = idx
    place = 0
    for runner in (runners) :
        place += 1
        if team_cnt[runner]<6 or score_cnt [runner] == 4  : continue
        score[runner] += place
        score_cnt[runner] += 1
    dashboard = []
    for team, cnt in team_cnt.items() :
        if cnt == 6 :
            dashboard.append([score[team], fifth_[team], team])
    
    dashboard.sort()
    print(dashboard)
    return dashboard[0][2]

T = int(input())
for _ in range(T) :
    n = int(input())
    runners = list(map(int, input().split()))
    print(get_winner(runners, n))
