import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

import math

T = int(input())


def is_sosu(num) :
    if num == 1 :
        return False
    if num== 2 or num == 3 or num == 5 :
        return True
    
    for i in range(2, int(math.sqrt(num) )+ 2 ) :
        if num % i == 0 :
            return False
    return True

def dfs(number, path) :
    if len(path) == 3 :
        print(*sorted(path))
        return True
    for n in range(number, 0, -1) :
        if is_sosu(n) :
            path.append(n)
            if dfs(number - n, path) :
                return True
            path.pop()
    return False
    

def solve(k) :
    ''' 만약 3개의 소수의 합으로 표현될 수 있으면 3 소수를 오름차순
        안되면 0을 반환'''
    if  not dfs(k, []) :
        print("0")
        

for _ in range(T) :
    K = int(input())
    solve(K)
    
