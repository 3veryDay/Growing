import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
from collections import defaultdict, deque

N = int(input())
parent = list(map(int, input().split()))
d = int(input())

def delete_dfs(v) :
    parent[v] = -2
    for n in range(N) :
        if parent[n] == v :
            parent[n] = -2
            delete_dfs(n)
delete_dfs(d)

def find_leaf_node() :
    leaf = [0] * N
    for n in range(N)  :
        if parent[n] == -1 or parent[n] == -2 : continue
        leaf[parent[n]] = 1
    cnt = 0
    for n in range(N) :
        if leaf[n] == 0 and parent[n] != -2:
            cnt += 1
    return cnt
    
print(find_leaf_node())
