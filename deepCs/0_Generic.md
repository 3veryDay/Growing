## 🎯 오늘의 공부 주제
# **Generic**

---

## 💡 핵심 개념 (Definition)
> 한 줄 요약: 타입을 파라미터화하여 런타임이 아닌 컴파일 타임에 타입 체크를 수행하는 것

제네릭이 없었을 때는 모든 것의 상위 클래스인 `object`를 사용해서 모든 객체를 담을 수 있도록 했습니다. 하지만 이런 경우 크게 두가지 문제점이 발생합니다.

1. 컴파일 타임 타입 체크 불가 : 잘못된 타입의 객체가 들어가도 런타임 중에 `ClassCastException`이 발생함.
2. 불필요한 casting : 코드 지저분해짐

그래서 <T> 의 제네릭을 사용해서 타입 안정성도 챙기고, 형반환도 컴파일러가 알아서 처리해주는 가독성 높은 코드 작성 가능!


## ⚙️ 동작 원리 / 구조 (Mechanism)
```java
public class Box<T> {
    private T item;

    public void setItem(T item) {
        this.item = item;
    }

    public T getItem() {
        return item;
    }
}

// 사용 예시
Box<String> stringBox = new Box<>();
stringBox.setItem("Hello");
String s = stringBox.getItem(); // 별도의 형변환이 필요 없음```

//같은 상황에서 이렇게도 쓸 수 있음
Box<Int> intBox = new Box<>();
intBox.setItem(1);
int i = intBox.getItme();
```

보통 <T>는 Type, <E>는 Element, <K> 는 key, <V> 는 Value, <N> 은 <Number>로 사용

## 알아야 하는 추가적인 내용 - 1 : wildcard
제네릭의 유연성을 높이는 특수 기호로
1. `<?>` (Unbounded Wildcard): 모든 타입이 가능합니다. <? extends Object>와 동일합니다.

2. `<? extends T>` (Upper Bounded Wildcard): T와 그 자손 타입만 가능합니다. (데이터 읽기 전용으로 자주 사용)

3. `<? super T>` (Lower Bounded Wildcard): T와 그 조상 타입만 가능합니다. (데이터 쓰기 전용으로 자주 사용)

## 알아야 하는 추가적인 내용 - 2 : 제네릭 소거(Type Erasure)

- 컴파일 시점: 타입 체크를 수행하고 필요한 곳에 형변환 코드를 삽입합니다.

- 런타임 시점: <T>와 같은 정보는 사라지고, 제한이 없는 경우 Object로, 제한이 있는 경우(extends T) T로 치환됩니다.

- 참고: 이로 인해 new T()와 같이 제네릭 타입으로 직접 객체를 생성하거나, static 변수에 제네릭 타입을 사용할 수는 없습니다.

## 🆚 장단점 / 비교 (Pros & Cons)
- 장점: 
- 단점: 
- 비교 대상: 

---

## 🔗 참고 자료 (References)
- [ ] 공식 문서 확인
- [ ] 블로그 정리 완료
