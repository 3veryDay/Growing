from collections import deque


def backtracking(num) :
    count = 0
    def bfs( n ) :
        count = 0
        q = deque()
        q.append([n,0])
        while q :
            curr, count = q.popleft()
            if curr == 1 :
                return count
            for idx in (1,2,3) :
                if idx == 1 and curr % 3 == 0 :
                    q.append([curr//3, count + 1])
                if idx == 2 and curr % 2 == 0 :
                    q.append([curr//2, count + 1])
                if idx == 3 :
                    q.append([curr - 1, count + 1 ])
        return count
    return bfs(num)
    
    
print(backtracking(2))
"""
bfs backtracking 하니까 시간 너무 오래 걸림. 이럴 때는 dp를 생각해보자


"""
