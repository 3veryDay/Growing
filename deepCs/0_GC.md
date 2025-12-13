# Java GC 핵심 요약 및 알고리즘 총정리

## 1. Java GC(Garbage Collection) 개요

### 핵심 개념
- **정의:** JVM의 Heap 영역에서 동적으로 할당된 메모리 중, 더 이상 사용되지 않는 객체(Garbage)를 찾아내어 메모리를 회수하는 자동 메모리 관리 기법이다.
- **대상 판별 (Reachability):**
  - **Reachable:** 유효한 참조가 있는 객체.
  - **Unreachable:** 참조가 끊겨 더 이상 접근 불가능한 객체 (GC 대상).
- **GC Root Space:** 참조의 시작점이다. 여기서부터 탐색을 시작해 닿지 않는 객체를 찾아낸다.
  - **Stack:** 메서드 내 지역 변수, 파라미터.
  - **Method Area:** static 변수.
  - **Native Method Stack:** JNI(자바 외 언어) 참조.

### 동작 과정 (Mark-Sweep-Compact)
1. **Mark:** Root Space로부터 그래프 순회를 통해 Reachable한 객체를 식별한다.
2. **Sweep:** Unreachable한 객체(Mark 되지 않은 객체)를 메모리에서 해제한다.
3. **Compact:** (선택적) 메모리 파편화를 방지하기 위해 살아남은 객체들을 한곳으로 모아 압축한다.

---

## 2. JVM Heap 메모리 구조와 가설

GC는 **'약한 세대 가설(Weak Generational Hypothesis)'**을 전제로 설계되었다.
1. 대부분의 객체는 금방 접근 불가능(Unreachable) 상태가 된다.
2. 오래된 객체에서 젊은 객체로의 참조는 아주 적다.

### 물리적 구조 (JDK 8 이하 및 G1 이전)
- **Young Generation (Eden + Survivor 0, 1):**
  - 새로 생성된 객체가 위치한다.
  - 객체의 수명이 짧아 **Minor GC**가 빈번하게 발생한다.
  - Eden이 꽉 차면 살아남은 객체는 Survivor로 이동하고, 일정 Age가 되면 Old로 승격(Promotion)된다.
- **Old Generation:**
  - Young 영역에서 살아남은(오래된) 객체가 위치한다.
  - 메모리가 크지만 GC 발생 빈도는 적다.
  - 꽉 차면 **Major GC (Full GC)**가 발생하며, 이때 멈춤 현상(Stop-The-World)이 길게 발생한다.

---

## 3. GC 알고리즘의 발전 (종류)

### 1) Serial GC
- **특징:** 가장 단순한 방식. **싱글 스레드**로 동작한다.
- **단점:** GC가 진행되는 동안 모든 애플리케이션 스레드가 멈추는 **Stop-The-World(STW) 시간이 매우 길다.**
- **용도:** 메모리와 코어가 매우 적은 환경 외에는 **실무에서 사용하지 않는다.**

### 2) Parallel GC (Java 8 Default)
- **특징:** Serial GC의 STW 문제를 개선하기 위해 탄생했다.
- **동작:** **Young 영역의 GC(Minor GC)를 멀티 스레드**로 수행한다. (단, Old 영역은 여전히 싱글 스레드)
- **장점:** Serial GC에 비해 STW 시간이 단축되었다.

### 3) Parallel Old GC
- **특징:** Parallel GC를 개선한 버전이다.
- **동작:** Young 영역뿐만 아니라 **Old 영역의 GC(Major GC)도 멀티 스레드**로 수행한다.
- **결과:** 전체적인 처리량(Throughput)이 향상되었다.

### 4) CMS GC (Concurrent Mark Sweep)
- **특징:** STW 시간을 최소화하기 위해 고안되었다.
- **동작:** 애플리케이션 스레드와 GC 스레드를 **동시에(Concurrent)** 실행한다.
- **단점:** 메모리 파편화가 심하고, CPU 사용량이 높아 구현이 복잡하다. 결국 **Java 9에서 Deprecated(JEP 291), Java 14에서 완전히 제거(JEP 363)** 되었다.

### 5) G1 GC (Garbage First) (Java 9+ Default)
- **구조:** 물리적으로 고정된 Young/Old 영역을 없애고, 전체 힙을 **Region(작은 블록)** 단위로 나눴다. (체스판 구조)
- **동작 (동적 할당):**
  - 각 Region에게 Eden, Survivor, Old라는 역할을 **동적으로 부여**한다.
  - 상황에 따라 효율적인 위치로 객체를 재배치(Evacuation)한다.
  - **Garbage First:** 이름처럼 쓰레기(Garbage)가 가득 찬 Region을 먼저 파악해 우선적으로 청소한다.
- **장점:** 전체 힙을 뒤지지 않고 부분적으로 GC를 수행해 STW 시간을 획기적으로 줄이고 예측 가능하다. 대용량 메모리에 적합하다.

### 6) ZGC
- **목표:** TB 단위의 **초대용량 메모리**를 처리하면서도 **STW 시간을 10ms 이하**로 보장하는 Low Latency GC이다.
- **기술:** **ZPage**라는 동적 영역을 사용하며, 객체의 주소 비트를 활용한 **Colored Pointers**와 **Load Barriers** 기술을 사용한다.
- **단점:** 동작 방식이 매우 복잡하고 메타데이터 저장을 위한 메모리 오버헤드가 크다.
- **결론:** 작은 힙 사이즈에서는 오히려 비효율적이며, 대규모 트래픽과 메모리를 다루는 시스템에 적합하다.

---

### 마무리 요약
- **Java 8:** Parallel GC가 기본이다. (Young만 멀티, Old는 싱글/멀티 선택)
- **Java 9 이후:** G1 GC가 기본이다. (Region 단위, 유연한 메모리 관리)
- **대규모/초저지연:** ZGC를 고려한다. (엄청난 대용량, 짧은 멈춤 시간)
