def solution(elements) :
    A = len(elements)
    E = elements * 2
    s = set()
    for length in range(1, A + 1 ) :
        for start in range(A) :
            addition = sum(E[start : start + length])
            
            s.add(addition)
    return len(s)


"""
근데 이건 O(N^2)임.
그냥 생각없이 이중 루프 돌린거.

그러면 어떻게 해야할까?
"""

def solution(elements) :
    ll = len(elements)
    ans = set()
    
    for start in range(ll) :
        total = elements[start]
        ans.add(total)
        for j in range(start+1, ll + start) :
            total += elements[j % ll]
            ans.add(total)
            
    return len(ans)

"""
이 방법은 start을 고정해두고, start와 붙은 애들을 순차적으로 하나씩 element을 더한 후, 그 더한 값을 set에 추가하는 것

내가 한 건 길이 설정한 후에 출발점을 계속 바꾸는 것
위의 풀이는 출발점을 설정한 후, 길이를 하나씩 늘려가면서 하나 늘려갈 때마다 set에 추가하기 떄문에, elements 배열을 연장할 필요가 없었음

배열을 두배로 연장하면 공간복잡도가 배로 증가하면서 효율성이 많이 떨어지게 되는 것 같음.

"""
