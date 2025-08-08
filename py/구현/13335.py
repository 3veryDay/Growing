import sys

input = sys.stdin.readline
from collections import deque

n, w, L = map(int, input().split())
trucks = deque(map(int, input().split()))

def solve() :
    time = 0
    crossed= 0
    bridge = deque([0]*w)
    weight = 0

    while crossed != n :
        time += 1
        print(f'bridge : {bridge} trucks : {trucks}')
        fin  = bridge.popleft()
        # 차가 실제로 다리를 건넌 경우
        if fin != 0 :
            crossed += 1
            weight -= fin
        
        if trucks : 
            truck = trucks[0]
            if weight + truck <= L :
                trucks.popleft()
                weight += truck
                bridge.append(truck)
            else :
                bridge.append(0)
        else :
            bridge.append(0)
    print(time)
solve()
