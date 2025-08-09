N = int(input())
k = int(input())

def solve(kk) :
    y = (kk - 1) // N
    x = (kk - 1) - (N * y)
    
    return (y+1) * (x + 1)


print(solve(k-1))
