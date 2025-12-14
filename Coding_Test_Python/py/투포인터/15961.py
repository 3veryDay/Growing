import sys

input = sys.stdin.readline
from collections import defaultdict

N, d, k, c = map(int, input().split())

buffet = []
for _ in range(N) :
    buffet.append(int(input()))
    
dic = defaultdict(int)
s = set()
for i in range(k) :
    dic[buffet[i]] += 1
    s.add(buffet[i])
    
answer = 0
for i in range(N):
    if c in s :
        answer = max(answer,len(s) )
    else :
        answer = max(answer, len(s) + 1)
    if answer == k + 1 :
        print(k + 1)
        sys.exit()
    
    
    dic[buffet[i]] -= 1
    if dic[buffet[i]] == 0 :
        s.remove(buffet[i])
    nxt = (i+k) % N
    dic[buffet[nxt]] += 1
    s.add(buffet[nxt])
print(answer)
