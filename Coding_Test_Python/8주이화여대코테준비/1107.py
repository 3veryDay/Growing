from itertools import product
# 수빈이가 이동하려는 채널 N (목적지)
N = int(input())
n = [i for i in str(N)]

# 고장난 버튼 수
M = int(input())
if M == 0 :
    print(min(len(n), abs(N-100)))
    exit()
broken_buttons = set(map(int, input().split()))
working_buttons = [str(i) for i in range(10) if i not in broken_buttons]

# 목적지 채널 번호가 한 자리수씩 str으로 구성된 배열 
n = [i for i in str(N)]

ans = abs(N - 100)  # 초기값 설정

# 길이가 len(n)-1 인 수 생성
if len(n)-1 > 0:
    per = list(product(working_buttons, repeat=len(n)-1))
    for num in per:
        number = int(''.join(num))
        ans = min(ans, abs(N - number) + len(n) - 1)

# 길이가 len(n) 인 수 생성
per2 = list(product(working_buttons, repeat=len(n)))
for num in per2:
    number = int(''.join(num))
    ans = min(ans, abs(N - number) + len(n))

# 길이가 len(n)+1 인 수 생성
per3 = list(product(working_buttons, repeat=len(n)+1))
for num in per3:
    number = int(''.join(num))
    ans = min(ans, abs(N - number) + len(n) + 1)
    
print(ans)
