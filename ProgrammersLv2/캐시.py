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
