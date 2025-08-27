from collections import deque


def exclamation(n) :
    if n == 0 :
        return 1
    answer =1
    while n != 1 :
        answer *= n
        n -= 1
    return answer
def solve_1(K) :
    nums = list(i for i in range(1, N + 1))
    k, n = K, N
    answer = []
    while nums :
        e = exclamation(n-1)
        tmp = (k-1) // e
        answer.append(nums.pop(tmp))
        k = k-tmp*(e)
        n -= 1
    return answer
def solve_2(arr) :
    answer = 0
    n = N-1
    nums = list(i for i in range(1, N + 1))
    for a in arr :
        answer +=( nums.index(a) * exclamation(n))
        nums.remove(a)
        print(answer, nums)
        n -= 1
    return answer + 1

N = int(input())
input_ = list(map(int, input().split()))
if input_[0] == 1 :
    print(*solve_1(input_[1]))
else :
    print(input_[1:])
    print(solve_2(input_[1:]))
    
