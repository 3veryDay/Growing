from functools import cmp_to_key


def compare(num1, num2) :
    if int(str(num1) + str(num2)) > int(str(num2) + str(num1)) :
        return -1
    else :
        return 1
    
    
def solution(numbers) :
    
    sorted_numbers = sorted(numbers, key = cmp_to_key(compare))
    answer = ''.join(str(x) for x in sorted_numbers)
    
    return "0" if int(answer) == 0 else answer