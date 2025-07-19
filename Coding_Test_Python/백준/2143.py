from collections import defaultdict

T = int(input())
A = int(input())
a = list(map(int, input().split()))

B = int(input())
b = list(map(int, input().split()))
answer = 0
A_dict = defaultdict(int)
for start in range(A) :
    for end in range(start, A) :
        if start == end :
            A_dict[a[end]] += 1
        else :
            A_dict[sum(a[start:end+1])] += 1


for start in range(B) :
    for end in range(start, B) :
        B_partial_sum = sum(b[start:end+1])
        answer += A_dict[T-B_partial_sum]
print(answer)
