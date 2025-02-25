def solution(n, k, enemy):
    answer = 0

    #DFS를 재귀적으로 구현할 때는 보통 방문을 먼저 처리한 후 재귀 호출을 진행하는 것이 일반적이야.
    def dfs(byeong, moo, idx, cnt) :
        nonlocal answer
        
        if idx >= len(enemy) :
            if cnt > answer :
                answer = cnt
        if moo == 0 :
            if idx == len(enemy) or enemy[idx] > byeong :
                if cnt > answer :
                    answer = cnt
        
        
        #지금 idx와 연결된 노드를 재귀적으로 방문
        if moo != 0 :
            dfs(byeong, moo-1, idx+1, cnt+1)
        if idx < len(enemy) and enemy[idx] <= byeong :
            dfs(byeong - enemy[idx], moo, idx+1, cnt + 1)
    (dfs(n,k,0,0))
    return answer
