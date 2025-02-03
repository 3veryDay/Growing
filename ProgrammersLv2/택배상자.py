'''
굉장히 간단한 문제이지만, 시간 복잡도를 최적화해야지만 풀 수 있는 문제.
이러한 간단한 배열 문제에서 시간 복잡도를 줄일 수 있는 방법
1. [i for i in range(1, 29) ] 이러한 간단한 배열을 만들 거면, 차라리 그냥 I, I += 1 이런 식으로 숫자만 사용하는 것도 좋다.
2. 배열을 슬라이싱하거나, popleft 하는 것보다, index를 줄이거나 늘리는 식으로 하는 게 더 효율적이다.

if 어떠한 요소 in 배열 : -> 이거는 시간 복잡도 O(N)이다. 그렇기에 하나씩 썪여 있으면 시간 복잡도가 확 늘어난다.
그렇기 때문에, 특징이 있는 애들의 경우에는 바로 잡는 게 좋다. 
여기 같은 경우에는 순차적으로 box가 증가하기 때문에, order에 올 수 있는 애랑, 다른 벨트 위에 있는 친구들... 다 생각하면 굳이 in을 쓰지 않고, 간단하게 풀어 쓸 수 있었다.

'''


def solution(order) :
    
    sub = []
    l, o = 1, 0
    cnt = 0
    while o < len(order) and l <= len(order) + 1 :
        
        if l == order[o] :
            cnt += 1
            l += 1
            o += 1
        else :
            if not sub :
                sub.append(l)
                l += 1
                
            else :
                if sub[-1] == order[o] :
                    while sub and sub[-1] == order[o] and o < len(order) :
                        sub.pop()
                        o += 1
                        cnt += 1
                    sub.append(l)
                    l += 1
                else :
                    if sub[-1] > order[0] and order[o] < l :##if () in [] 이거 쓰면 확실히 확 늘어나서, 안 쓰는 게 좋다. 
                        return cnt
                    else :
                        sub.append(l)
                        l += 1

    return cnt
