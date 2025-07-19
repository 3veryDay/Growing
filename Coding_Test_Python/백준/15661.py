from itertools import combinations

N = int(input())
S = []
for _ in range(N) :
    S.append(list(map(int, input().split())))
for i in range(N) :
    for j in range(i+1, N) :
        S[i][j] += S[j][i]
        S[j][i] = 0


for line in S :
    print(line)



def calculate_difference( members1) :
    members = set(i for i in range(N))
    members2 = members - members1
    sum1 = 0
    members1 = list(members1)
    members1.sort()
    for idx, person1 in enumerate(members1) :
        for person2 in members1[idx:] :
            sum1 += S[person1][person2]
    sum2 = 0
    members2 = list(members2)
    members2.sort()
    for idx, person1 in enumerate(members2) :
        for person2 in members2[idx:] :
            sum2 += S[person1][person2]
    print(f'members1 : {members1} sum1 : {sum1} sum 2 :{sum2}')
    return abs(sum1-sum2)


# 인원수가 적은 팀의 인원수를 입력 -> 그때의 최소 리턴
def calculate(start_team_member) :
    answer = float('inf')
    members = set(i for i in range(N))
    small_team_member = list(combinations(members, start_team_member))
    print(small_team_member)
    for team_member in small_team_member :
        answer = min(answer, calculate_difference(set(team_member)))
    return answer    


result = float('inf')
for start_team_member in range(2, N//2 + 1) :
    result = min(result, calculate(start_team_member))
print(result)
