N = int(input())
M= int(input())

parent = [i for i in range(N)]


def find_parent(x) :
    if parent[x] != x :
        parent[x] =  find_parent(parent[x])
    return parent[x]

def union(a, b) :
    a = find_parent(a)
    b = find_parent(b)
    if a < b :
        parent[b] = a
    else :
        parent[a] = b
        
    

for _ in range(M) :
    a, b = map(int, input().split())
    a-=1
    b-=1
    union(a, b)

answer = 0
for i in range(N) :
    if find_parent(i) == find_parent(0): 
        answer += 1
print(answer -1)
