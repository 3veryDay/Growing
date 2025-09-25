import sys
sys.setrecursionlimit(10**3)

n, m = map(int, input().split())

parent = [i for i in range(n+1)]

def find_parent(x):
    while x != parent[x]:
        parent[x] = parent[parent[x]]  # 경로 압축
        x = parent[x]
    return x
def union(a, b) :
    a = find_parent(a)
    b = find_parent(b)
    if a < b :
        parent[b] = a
    else :
        parent[a] = b
        
def check_if_same_par(a, b) :
    A = find_parent(a)
    B = find_parent(b)
    if A == B :
        return True
    else :
        return False
for _ in range(m) :
    op, a, b = map(int, input().split())
    if op == 0 :
        union(a, b)
    if op == 1 :
        if check_if_same_par(a, b) :
            print("yes")
        else :
            print("no")
