from itertools import permutations
def solution(numbers):
    
    # num이 소수면 True 리턴, 소수가 아니면 False 리턴하는 함수
    def sosu(num) :
        if num == 1 :
            return False        # False : 소수가 아니다
        if num == 2 or num == 3 :
            return True         # True : 소수다.
        if num % 2 == 0 or num % 3 == 0 :
            return False
        
        for i in range(5, num//2 + 1, 2) :
            if num % i == 0 :
                return False
            
        return True
    answer = set()
    for length in range(1, len(numbers) + 1 ) :
        lst = list(permutations(numbers, length))
        for l in lst :
            string = int(''.join(l))
            if sosu(string) :
                answer.add(string)
    return len(answer)

#다른 풀이

from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)

'''
집합 | 집합 => 합집합
그러니까, 여기서는 중복 없는 모든 조합들을 만들기 위해서 a |= set(map(**int**, map("".join, permutations(list(n), i + 1))

'''
