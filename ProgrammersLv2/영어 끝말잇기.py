"""
  20분 걸렸지만, 새로 알아낸 사실! 
for문에서 슬라이싱을 하면, slicing된 배열이 새로 들어가는 것이기에 인덱스가 다 새로 고쳐진다.
[a
이 문제에서도 for idx, word in enumerate(words[1:]) :

words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
words[1:] = [ "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
이기에, 인덱스 계산을 슬라이싱 된 kick이 0이 되도록 계산해야 한다.
 쉬운 문제인데, 너무 많은 시간을 지체했다.
  """


def solution(n, words) :
    said_words = set()
    said_words.add(words[0])
    prev = words[0][-1]
    
    for idx, word in enumerate(words[1:]) : 
        idx += 1
        num = idx % n + 1
        spin = idx // n + 1
        
        if len(word) < 2 or word in said_words or prev != word[0] :
            print(idx, word, num, spin)
            return [num, spin]
        
        else :
            print(prev)
            said_words.add(word)
            prev = word[-1]
    return [0,0]


"""
 다른 사람의 풀이를 보던 중에, 짧고 직관적으로 풀이한 파이써닉한 코드를 보게 되었다.
 여기서 set을 쓰지 않고, words[i] in words[:i]이게 인상 깊었다.
 어차피 시간 복잡도는 비슷하니, 이렇게 하면 set을 따로 만들지 않기 때문에 공간 복잡도가 줄어들 것이니
 """
 def solution(n, words) :
    for i in range(1, len(words)) :
        if len(words[i]) < 2 or words[i][0] != words[i-1][-1] or words[i] in words[:i] :
            return [i%n + 1, i//n + 1]
    else :
        return [0,0]
