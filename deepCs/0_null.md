# NULL

null은 데이터 타입 (object)는 존재하나, 참조하는 대상이 없거나 정의되지 않은 상태.
->이를 참조하면 `NullPointerException` = `NPE` 발생함

### NPE 방지

1. Optional 클래스 사용
```
Optional<String> maybeName = Optional.ofNullable(getName());

// null이 아닐 때만 실행
maybeName.ifPresent(n->sout(n.length())) ;
```

2. Objects사용
```
Objects.isNull(obj)
Objects.nonNull(obj)
``` 

3. Annotation 처리

```
//intellij 경고 유도
public void printMessage(@NotNull String Message) {
  sout(messgae)
}

//Lombok 활용
public void updateName(@NonNull String name) {
  //lombok이 컴파일 시점에 자동으로 아래 코드 넣음
  // if (name == null ) throw new NullPointerException(" this name is marked non-nulll" );
  this.name = name;
}

//Spring Validation
public class UserRequest {
  @NotNull(messgae = "이름 필수")
  private String name;
}
```

