import heapq
def solution(n,k, enemy) :
    left, right = 0, len(enemy)
    while left <= right :
        mid = (left + right) // 2
        heap = []
        goon = n
        skill = k
        
        for i in range(mid) :
            heapq.heappush(heap, -enemy[i])
            goon -= enemy[i]
            
            if goon < 0 :
                if skill > 0 :
                    goon += -heapq.heappop(heap)
                    skill -= 1
                else :
                    right = mid - 1
                    break
        else :
            left = mid + 1
    return right
                



# 이건 합계: 34.4 / 100.0
def solution(n,k, enemy) :
    answer = 0
    def dfs(n,k, idx) :
        nonlocal answer
        if idx >= len(enemy) :
            answer= len(enemy)
            return
        if k == 0 and enemy[idx] > n:
            answer = max(answer, idx )
            return
            
        else :
            if idx < len(enemy) and enemy[idx] <= n :
                dfs(n - enemy[idx], k, idx + 1)
            if k != 0 :
                dfs(n, k-1, idx+ 1)
    dfs(n,k,0)
    return answer


