# javac

1. 컴파일 타임 (Compile Time) 자바 소스 코드(.java)는 JDK에 포함된 javac 컴파일러를 통해 바이트코드(.class)로 변환됩니다. 이 과정에서 어휘 분석, 구문 분석(AST 생성), 의미 분석을 거쳐 문법 오류를 잡고 최적화된 바이트코드를 생성합니다.

2. 클래스 로딩 (Class Loading) 자바 프로그램이 실행되면 JVM이 OS로부터 메모리를 할당받습니다. 이후 Class Loader가 동적으로 필요한 클래스 파일을 찾아 Loading(적재) → Linking(검증/준비/분석) → Initialization(초기화) 단계를 거쳐 Runtime Data Area에 배치합니다.

3. 런타임 데이터 영역 (Runtime Data Area) 메모리 영역은 크게 두 가지로 나뉩니다.

모든 스레드 공유: 클래스 정보와 static 변수가 저장되는 Method Area, 객체 인스턴스가 생성되는 Heap Area.

스레드별 독립 공간: 메서드 호출 시 프레임이 쌓이는 JVM Stack, 현재 명령 주소를 갖는 PC Register, 네이티브 코드 실행을 위한 Native Method Stack.

4. 실행 엔진 (Execution Engine) 메모리에 올라온 바이트코드는 실행 엔진에 의해 기계어로 변환되어 실행됩니다.

기본적으로 Interpreter가 한 줄씩 해석하여 실행하지만,

자주 실행되는 코드(Hot Spot)는 JIT Compiler가 기계어로 컴파일하여 캐싱함으로써 실행 속도를 획기적으로 높입니다.

추가로 **Garbage Collector(GC)**가 더 이상 참조되지 않는 객체를 정리하고, JNI를 통해 네이티브 라이브러리와 통신합니다.



## 공부 마인드맵
<img width="4738" height="3868" alt="image" src="https://github.com/user-attachments/assets/42a9ab4f-bc47-4909-b15b-72d57050e96f" />


## 추가 
https://inpa.tistory.com/entry/JAVA-%E2%98%95-JDK-JRE-JVM-%EA%B0%9C%EB%85%90-%EA%B5%AC%EC%84%B1-%EC%9B%90%EB%A6%AC-%F0%9F%92%AF-%EC%99%84%EB%B2%BD-%EC%B4%9D%EC%A0%95%EB%A6%AC
