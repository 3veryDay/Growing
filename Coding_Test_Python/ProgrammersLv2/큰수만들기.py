'''
ValueError: max() arg is an empty sequence
max에 빈 배열 전달
'''

def solution(number, k) :
    num = list(map(int, number))
    
    if k == len(num) - 1  :
        return str(max(num))
    if k == 1 :
        m = min(num)
        m_ = num.index(m)
        num.pop(m_)
        return ''.join(map(str, num))
    
    n = len(number)
    a = n-k
    answer = []
    start_idx = 0
    end_idx = k+1
    while len(answer) < a :
        # print(start_idx, "~ " , end_idx)

        # val, idx = max((val, idx) for idx, val in enumerate(num[start_idx : end_idx]))
        #가장 마지막을 반환한다.
        
        val = max(num[start_idx:end_idx])    #매번 max을 호출할 때, 슬라이싱을 사용해서 리스트를 새로 생성하기 때문에 , 공간 복잡도 높고, 시간 복잡도는 최대 O(N)
        idx = num[start_idx:end_idx].index(val)
        #이것도 시간 복잡도가 매우 높은 것 같음
        
        
        # idx = 0
        # val= 0 
        # for midx, mval in enumerate(num[start_idx : end_idx]) :
        #     if mval > val :
        #         idx = midx
        #         val = mval
        # print(f'val : {val} idx : {idx}')
        end_idx += 1
        start_idx += idx + 1
        answer.append(val)
        
        
#         print(val)
#         print(answer)
    return ''.join(map(str, answer))


'''
최적화 원리 :
스택의 top과 비교하여 더 작은 값을 제거하는 방식
'''



### 정답

def solution(number, k):
    stack = []
    
    for num in number:
        while stack and k > 0 and stack[-1] < num:
            stack.pop()  # 스택에서 숫자 제거 (k번까지 가능)
            k -= 1
        stack.append(num)  # 현재 숫자를 추가
    
    return ''.join(stack[:len(number) - k])  # 최종 결과 반환


'''
1️⃣ 작은 문제부터 해결해보기 (손으로 풀기)
작은 입력값에 대해 직접 최적의 선택을 찾아보는 연습을 하면 패턴을 쉽게 이해할 수 있어.
예를 들어, "4177252841"에서 4개를 제거하여 가장 큰 수를 만들 때 어떤 숫자를 제거하면 되는지 손으로 적어보는 거야.
예제
plaintext
복사
편집
입력: "4177252841", k=4
1. 4는 유지, 1 제거 → "477252841"
2. 7은 유지, 2 제거 → "47752841"
3. 5는 유지, 2 제거 → "4775841"
4. 8은 유지, 4 제거 → "477581"
결과: "775841"
이 과정을 직접 따라 해 보면 큰 숫자를 유지하면서 작은 숫자를 제거해야 한다는 직관이 생길 거야.

2️⃣ 문제를 "최대값을 찾는 과정"으로 변환하기
기존에는 max()와 슬라이싱을 사용해서 최댓값을 찾고 있었는데,
**"가장 큰 숫자를 유지하고, 필요 없는 숫자를 제거하는 방법"**을 고민하는 연습이 필요해.
슬라이싱 없이 최댓값을 유지하는 방법을 생각해 보면 자연스럽게 스택을 떠올릴 수 있어.
3️⃣ 스택을 활용한 문제 연습하기
스택을 활용한 그리디 문제를 여러 개 풀어 보면 패턴이 익숙해질 거야.
예제 문제:

백준 2841 - 외계인의 기타 연주
백준 17298 - 오큰수
프로그래머스 - 큰 수 만들기 (현재 문제!)
이런 문제를 직접 풀어보면서 그리디 + 스택 패턴을 연습하면 직관적으로 떠올리기 쉬워질 거야!

4️⃣ 직접 코드 없이 시뮬레이션 해보기
코드를 바로 짜는 게 아니라, 예제를 보면서 한 단계씩 변화를 추적하는 연습을 하면 좋아.
예제 입력을 스택처럼 종이에 적어놓고, 숫자가 들어오고 빠지는 과정을 눈으로 따라가 보는 거야.
이렇게 하면 점점 문제 해결 방식이 익숙해지고,
"이런 문제는 스택으로 풀면 되겠다!"라는 감각이 생길 거야. 😊
'''
