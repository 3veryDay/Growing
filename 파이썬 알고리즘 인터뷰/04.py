import re
from collections import Counter


def solution(paragraph, banned ) :
    
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph )
             .lower().split()
             if  word not in banned]
    
    return Counter(words).most_common()
    
a = " 1,2,3,3,3,3,4,4,4,4,4,4,4,4,4,4,6,6"
b = [4]

print(solution(a,b))