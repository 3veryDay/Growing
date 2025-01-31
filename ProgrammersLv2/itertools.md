## Itertools

this module standardies a core of fast, memory efficient tools that are useful by themselves or in combination.

#### Infinite Iterators

|Iterator|Arguments|Result|Example|
|--|-------|----|-----|
|count()|[start,(,step)]| start, start+step, start+2*step ...| count(10) -> 10 11 12 13 14 ...|
|cycle()| p| p0, 01, ...p_last, p0, p1 ...| cycle('ABCD') -> A B C D A B C D ...|
|repeat()|elem [,n]| elem, elem, elem, ... up to n times or endlessly| repeat(10,3) -> 10 10 10|


#### Combinatoric Iterators

|Iterator|Arguments|Results|
|---|---|--------|
|product()|p,q,...(repeat=1)|모든 경우의 수 조합. 중첩 for문과 동일한 효과|
|permutations()|p(,r)|r길이의 튜플로, 순서가 중요한 모든 조합. 같은 요소는 중복되지 않음|
|combinations|p,r|r길이의 튜플로, **순서가 중요하지 않은 조합**을 구함. 같은 요소는 중복되지 않음|
|combinations_with_replacement()|p,r|r길이의 튜플로, 순서가 중요하지 않은 조합을 구함. 같은 요소가 반복될 수도 있음|


#####Examples

product('ABCD', 2) => AA AB AC AD BA BB BC BD ...
permutations('ABCD', 2) => AB AC AD BA BC BD CA CB CD DA DB DC **(nP2)**
combinations('ABCD',2 ) => AB AC AD BC BD CD **(nC2)**
combinations_with_replacement('ABCD', 2) => AA AB AC AD BB BC BD CD CC CD DD


