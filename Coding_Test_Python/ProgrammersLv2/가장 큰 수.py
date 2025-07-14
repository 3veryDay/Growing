from functools import cmp_to_key 
def solution(numbers) :
    def compare(a : int, b : int) -> bool:   # True면 순서 유지, 아니면 바꾸기
        a, b = str(a), str(b)
        return  1 if int(a+b) > int(b+a) else -1
    
    tmp = sorted(numbers, key = cmp_to_key(compare), reverse = True)
#     for i in range(len(numbers)) :
#         for j in range(i+1, len(numbers)) :
#             if not compare(numbers[i], numbers[j]) :
#                 numbers[i], numbers[j] = numbers[j], numbers[i]#이건 시간 초과

    answer = ''
    for n in tmp :
        answer += str(n)
        
    return str(int(answer))
        
##다른 풀이
def solution(nums) :
    nums = list(map(str, nums))
    nums = sorted(nums, key = lambda x : x*3, reverse = True)
    return str(int(''.join(nums)))

## 다른 풀이
numbers = sorted(numbers, key=cmp_to_key(lambda a, b: -1 if a+b >= b+a else 1))
cmp_to_key 안에 함수를 lambda로 만들어도 됨
