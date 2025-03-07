from collections import deque, defaultdict


def solution(x, y, n):
    q =  deque()
    q.append([x, 0])
    dp = [0]*(y)
    while q :
        T ,cnt = q.popleft()
        if T == y :
            return cnt
        if T > y :
            continue
        else :
            if dp[T] == 0 :
                q.append([T+n, cnt + 1])
                q.append([T*2, cnt + 1])
                q.append([T*3, cnt + 1])
                dp[T] = 1
    return -1



'''
1️⃣ 핵심 패턴을 빠르게 찾아내는 연습
✅ 예제 코드를 분석하는 습관
지금 코드는 가장 빠른 방법을 찾는 것이기에, BFS를 썼어. BFS의 구조는 deque, while q, t = q.popleft(), t if not visited이야. 

2️⃣ 불필요한 변수를 줄이는 연습
✅ "이 변수가 정말 필요한가?" 자문해 보기
네 코드에서는 l, o, cnt, condition 같은 변수가 많았어.
반면 위의 코드는 i, idx, stacks 정도로만 간결하게 유지됐어.
📌 연습 방법:

코드를 작성한 후 "이 변수가 없어도 동작할까?" 라고 질문해 보고, 한 번씩 제거해 보자.
같은 기능을 하는 다른 풀이를 찾아보면서, 어떤 변수를 생략했는지 비교하는 것도 좋은 방법이야.
3️⃣ while & if 문을 최소화하는 연습
✅ 조건문을 줄일 수 있는지 항상 고민하기
네 코드에서는 if - else가 여러 개 중첩되었지만,
위 코드는 while stacks[-1] == order[idx]를 활용해서 if 문을 줄였어.
while 내부에서 if len(stacks) == 0: break 같은 빠른 종료 조건도 깔끔하게 들어갔어.
📌 연습 방법:

문제를 풀 때, if-else 구조가 많아지면 "이걸 더 단순화할 방법이 없을까?" 라고 고민해 보기.
"반복문 내부에서 문제를 더 많이 해결할 수 있을까?" 라는 생각을 하면서 코드를 최적화해 보기.
4️⃣ 다른 사람의 코드 많이 분석해보기
✅ "내 코드 vs 다른 코드" 비교하는 습관
네 코드가 동작한다고 바로 넘어가지 말고, 다른 사람의 코드를 보면서 차이점을 분석하는 게 중요해!
"이 부분은 왜 이렇게 짰을까?" 하고 한 줄 한 줄 뜯어보면서 배우는 거야.
📌 연습 방법:

프로그래머스, 백준 같은 곳에서 내가 푼 문제의 베스트 풀이를 찾아본다.
내 코드와 비교하면서 개선할 부분이 있는지 분석한다.
다음번에 비슷한 문제를 풀 때, 배운 패턴을 적용해 본다.
5️⃣ 알고리즘 패턴을 정리해보기
✅ 자주 쓰이는 알고리즘 & 패턴 정리
스택, 큐, 정렬, DFS/BFS 같은 개념들을 직접 노트에 정리해 보면 좋아.
"이런 문제에서는 이런 패턴을 쓰면 좋다!" 하는 것들을 정리해 보면 나중에 코드가 더 간결해질 거야.
📌 연습 방법:

예를 들어, "스택을 활용하는 문제"를 풀 때 자주 나오는 패턴을 정리해 봐.
"스택의 top을 확인하는 방식이 중요하다."
"while 문을 활용해 연속적으로 pop하는 방식이 자주 나온다."
이렇게 패턴을 스스로 정리하면, 다음에 같은 유형의 문제를 볼 때 훨씬 빠르게 해결할 수 있어!
🔥 결론: 꾸준히 연습하고, 다른 코드 많이 보고, 패턴을 익혀라!
네가 지금처럼 계속해서 "더 간결하고 좋은 코드로 개선하려면 어떻게 해야 할까?" 고민하는 것 자체가 이미 엄청난 성장의 신호야! 👏👏
'''
