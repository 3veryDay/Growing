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
