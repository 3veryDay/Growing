def solution(n, words) :
    sets=set()
    for i, word in enumerate(words) :
        if i== 0 :
            sets.add(word)
            continue
        if words[i-1][-1] != word[0] :
            return ([(i%n)+1, i//n + 1])
        if word in sets :
            return ([(i%n)+1, i//n+ 1 ])
        else :
            sets.add(word)
    
    return ([0,0])

n = 2
words =["hello", "one", "even", "never", "now", "world", "draw"]
print(solution(n,words))