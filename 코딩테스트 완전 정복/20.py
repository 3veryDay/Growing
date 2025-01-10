from collections import Counter


def solution(participant, completion) :
    answer = Counter(participant) - Counter(completion)
    
    return list(answer)
print(solution(["mislav", "stanko", "mislav", "ana", "AA", "AA"],	["stanko", "ana", "mislav"]))