from collections import deque

def solution(begin, target, words):
    def check(word1, word2) :
        tmp = 0 
        for idx in range(len(word1)) :
            if word1[idx] != word2[idx] and tmp == 0:
                tmp += 1
            elif word1[idx] != word2[idx] and tmp != 0 :
                return False
        return True
    
    
    q = deque()
    q.append([begin, 0, []])
    while q :
        current, count, used = q.popleft()
        print(current, count)
        if current == target :
            return count
        for idx, word in enumerate(words ) :
            if idx not in used and check(current, word) :
                print("__")
                q.append([word, count + 1, used + [idx]])
            
    return 0


from collections import deque


def get_adjacent(current, words):
    for word in words:
        if len(current) != len(word):
            continue

        count = 0
        for c, w in zip(current, word):
            if c != w:
                count += 1

        if count == 1:
            yield word


def solution(begin, target, words):
    dist = {begin: 0}
    queue = deque([begin])

    while queue:
        current = queue.popleft()

        for next_word in get_adjacent(current, words):
            if next_word not in dist:
                dist[next_word] = dist[current] + 1
                queue.append(next_word)

    return dist.get(target, 0)

'''
1. 두개의 iterable이 주어졌을 때, 같은 인덱스 끼리 묶는 역할의 `zip`( ) 함수

'''
