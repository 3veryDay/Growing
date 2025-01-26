"""
문제 설명
효진이는 총 
𝑛
n개의 계단이 있는 곳을 올라가고 있습니다. 한 번에 1칸 또는 2칸씩 오를 수 있습니다.
효진이가 계단 꼭대기에 도달할 수 있는 방법의 수를 구하세요.

제한사항
𝑛
n은 1 이상, 2000 이하의 자연수입니다.
결과는 
1234567
1234567로 나눈 나머지를 반환합니다.
"""
def solution(n) :
    def dfs(total) :
        
        if total == n :
            return 1
        if total > n :
            return 0
        answer = 0

        for _ in (1,2) :
            if total + _ <= n :
                answer += dfs(total + _ ) % 1234567
                
            
        return answer  % 1234567
    
    return dfs(0)  % 1234567
print(solution(5))


"""
RecursionError: maximum recursion depth exceeded in comparison
이와 같은 에러가 뜬다는 것은 DFS 가 아닌 다른 접근법을 사용해야되고, 일단 내 지식 선에서는 DP가 
적절한 다음 접근 법이다. 
"""

