import heapq

heap = []

N = int(input())
s = []
for _ in range(N) :
    s.append(list(map(int, input().split())))
    
s.sort()
answer = 0
for start, end in s :
    if not heap :
        answer += 1
        heapq.heappush(heap, end)
    else :
        closest_end = heapq.heappop(heap)
        if start >= closest_end :
            heapq.heappush(heap, end)
        else :
            heapq.heappush(heap, end)
            heapq.heappush(heap, closest_end)
            answer += 1
            
print(answer)
