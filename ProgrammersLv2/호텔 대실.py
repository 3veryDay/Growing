import heapq

def solution(book_time):
    time = []
    cnt = 0 
    book_time.sort()
    for res in book_time :
        start, end = res
        start, end = int(start[:2])*60 + int(start[3:]),int(end[:2])*60 + int(end[3:])
        
        if not time :
            cnt += 1
            heapq.heappush(time,end)
        else :
            if time[0] +10 <= start :
                heapq.heappop(time)
                heapq.heappush(time, end)
            else :
                cnt += 1
                heapq.heappush(time, end)
        
    return cnt
