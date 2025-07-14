
import re
from itertools import permutations

def calculate(num1, exp, num2) :
    if exp =="-" :
        return str(int(num1) - int(num2))
    if exp =="+" :
        return str(int(num1) + int(num2))
    if exp =="*" :
        return str(int(num1) * int(num2))
    
    
def solution(expression) :
    
    exp = re.split(r'(\D)', expression)
    e = [l for l in expression if l=='-' or l =='+' or l == '*']
    perm = permutations(set(e))
    answer = 0
    for order in perm :
        express = exp[:]
        for o in order :
            # while o in exp :
            while o in express:
                idx = express.index(o)
                express = (express[:idx-1] + [calculate(express[idx-1], express[idx], express[idx+1])] + express[idx+2:])
        answer = max(answer, abs(int(express[0])))     
        
    return answer
    
