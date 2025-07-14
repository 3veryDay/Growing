#1차 풀이, 80
from collections import deque

def solution(cacheSize, cities):
    cache = deque()
    time = 0
    
    
    for i in range(cacheSize) :
        cache.append(cities[i].lower())
        time += 5
    for city in cities[cacheSize :] :
        city = city.lower()
        if city in cache :
            time += 1
            cache.remove(city)
            cache.append(city)
            
        else :
            time += 5
            cache.append(city)
            cache.popleft()
    return time

#2차 풀이, 90점
from collections import deque

def solution(cacheSize, cities) :
    
    cache = deque()
    cache.append(cities[0].lower())
    idx = 1
    time = 5
    
    while idx < len(cities) :
        city = cities[idx].lower()
        if city in cache :
            time += 1
            cache.remove(city)
            cache.append(city)
            idx += 1
            
        if city not in cache :
            if len(cache) < cacheSize :
                time += 5
                cache.append(city)
                idx += 1
            else :
                time += 5
                cache.append(city)
                cache.popleft()
                idx += 1
            
    return time

# 3차 시도 , 100

"""
cacheSize 가 0부터 ~~ 일 때는 0인 경우도 무조건 확인 같이 해야함.
보통 return 문으로 일찍 처리하면 될 것.

여기서도 두개의 testcase만 계속 실패가 떴는데, 이는 cacheSize가 0인 경우에도 cache에 넣고 시작했기 때문에 문제 발생.
0인 경우도 꼭 생각하자. 

"""
from collections import deque

def solution(cacheSize, cities) :
    if cacheSize == 0 :
        return len(cities) * 5
    cache = deque()
    cache.append(cities[0].lower())
    idx = 1
    time = 5
    
    while idx < len(cities) :
        city = cities[idx].lower()
        if city in cache :
            time += 1
            cache.remove(city)
            cache.append(city)
            idx += 1
            
        if city not in cache :
            if len(cache) < cacheSize :
                time += 5
                cache.append(city)
                idx += 1
            else :
                time += 5
                cache.append(city)
                cache.popleft()
                idx += 1
            
    return time


#다른 사람 풀이
#deque(maxlen = 정수) 
def solution(cacheSize, cities):
    import collections
    cache = collections.deque(maxlen=cacheSize)
    #deque(maxlen = cacheSize) 이런 기능이 있습니다~ 
    time = 0
    for i in cities:
        s = i.lower()
        if s in cache:
            cache.remove(s)
            cache.append(s)
            time += 1
        else:
            cache.append(s)
            time += 5
    return time
