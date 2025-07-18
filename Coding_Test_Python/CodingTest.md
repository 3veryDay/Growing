
### Backtrack 틀
```
def backtrack(path, depth):
    if 종료조건(depth):
        정답 처리(path)
        return

    for 후보 in 후보군:
        if 유효한 선택(후보):
            상태 변경(후보 선택)
            backtrack(갱신된 path, depth+1)
            상태 복원(후보 취소)
```

### 이외 이 문제에서 알게 된 것들

> a = [1, 2, 3, 4]를 1 2 3 4로 출력
- print(*a) #unpacking
- print(' '.join(map(str,a))

> set에서 요소 제거
- set.remove(x) # x 제거, x 없으면 keyerror
- set.discard(x) # x 제거, x 없으면 무시
- s - { x } # 새로운 set 반환, 원본은 안 건들임.

> set 추가 정보
- set은 순서가 없음.
- set 처음 초기화 할 때, set(number)는 불가능, {number} 이렇게 넘겨야 
