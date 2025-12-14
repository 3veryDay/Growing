import math
import sys

input = sys.stdin.readline
# 초기 체력은 안 주어짐 (1과 max가 안 주어짐)
# 방의 개수 N, 초기 공격력 ATK
N, ATK = map(int, input().split())
# 방정보 : t = 1 : 공격력, 생명력인 몬스터
# 방정보 : t = 2 : 포션 ATK += a, 생명령 += h
rooms = []
for i in range(N) :
    rooms.append(list(map(int, input().split())))
    
def fight_monster(hp, atk, a, h ) :
    '''공격력이 a인, 체력이 h인 몬스터'''
    '''나는 hp, 공격력은 atk'''
    t = math.ceil(h / atk)
    hp -= ((t-1)*a)
    
    return hp

def drink_potion(hp, atk, a, h, MAX_HP) :
    '''포션 마시기, 단 hp는 제한 있음'''
    return min(MAX_HP, hp + h) , atk + a

def fight_with_given_HP(MAX_HP) :
    hp = MAX_HP
    atk = ATK
    for room in rooms :
        print(f'hp : {hp}')
        # 몬스터가 있는 방
        if room[0] == 1 :
            hp = fight_monster(hp, atk, room[1], room[2])
            # 용사 사망 -1 반환
            if hp <= 0 : return hp
        # 포션 있는 방
        else :
            hp, atk = drink_potion(hp, atk, room[1], room[2], MAX_HP)
    return hp

# 이제 이진 탐색
l, r = 1, sys.maxsize

while l < r :
    m = (l+r) // 2
    if fight_with_given_HP(m) > 0 :
        r = m
    else :
        l = m + 1
print(l)
