## 🎯 오늘의 공부 주제
# **WebFlux**

---

## 💡 핵심 개념 (Definition)
> 한 줄 요약: Spring WebFlux는 적은 수의 스레드로 동시성을 처리할 수 있는 비동기-논블로킹 방식의 리액티브 웹 프레임워크입니다.

- 비동기-논블로킹 I/O: 요청을 보낸 후 응답을 기다리지 않고 다른 작업을 수행하여 자원을 효율적으로 사용합니다.

- 리액티브 스트림: Project Reactor 라이브러리를 기반으로 하며, 데이터 흐름을 Flux(0~N개)와 Mono(0~1개)로 관리합니다.

- 높은 확장성: 적은 하드웨어 리소스로 대규모 동시 접속을 처리하는 데 최적화되어 있습니다.

## ⚙️ 동작 원리 / 구조 (Mechanism)
WebFlux는 서블릿 컨테이너 대신 Netty와 같은 비동기 서버 위에서 이벤트 루프(Event Loop) 모델로 동작합니다. 요청이 들어오면 이벤트 루프가 이를 수락하고, 실제 작업은 논블로킹으로 처리한 뒤 결과가 준비되면 콜백이나 리액티브 체인을 통해 반환합니다.
```java
@RestController
@RequestMapping("/api")
public class WebFluxController {

    @GetMapping("/items")
    public Flux<String> getItems() {
        // 여러 데이터를 비동기 스트림으로 반환
        return Flux.just("Item 1", "Item 2", "Item 3")
                   .delayElements(Duration.ofMillis(100));
    }

    @GetMapping("/item/{id}")
    public Mono<String> getItem(@PathVariable String id) {
        // 단일 데이터를 비동기로 반환
        return Mono.just("Item details for " + id);
    }
}
```

## 🆚 장단점 / 비교 (Pros & Cons)
- 장점: 대규모 트래픽 처리 시 메모리 사용량이 적고 성능이 뛰어남, 스트리밍 데이터 처리에 적합함.

- 단점: 프로그래밍 모델이 복잡하여 학습 곡선이 높음, 디버깅 및 에러 추적이 어려움, 모든 라이브러리(DB 드라이버 등)가 논블로킹이어야 시너지가 남.

- 비교 대상: Spring MVC (Thread-per-request 모델, Blocking I/O 기반으로 구조가 단순하고 이해하기 쉬움)

---

## 🔗 참고 자료 (References)
- [ ] 공식 문서 확인
- [ ] 블로그 정리 완료
