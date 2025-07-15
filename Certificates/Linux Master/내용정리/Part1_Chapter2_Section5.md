# 프로세스
- 디스크의 프로그램을 **메모리에 적재하고 실행**한 상태
- 한 프로그램 -> 중복된 여러개의 프로세스 생성 가능 (프로그램의 인스턴스라고 함)
- 생성, 실행, 대기, 중지, 좀비, 종료의 라이프 사이클 (상태인 R, D, S, Z, T 랑 또 다름)

### 프로세스 유형
1. 최상위 프로세스
  - <mark>PID가 1</mark>
  - 부트 로더에 의해 리눅스의 초기화를 위해서 가장 먼저 실행되는 프로세스
  - init 프로세스 (centOS6) systemd(centOs7) -> on-demand, 병령
2. 부모 & 자식
  - PID, PPID
3. 고아 & 좀비
  - 고아 : 자식이 부모를 잃으면 고아(부모가 강제 종료)
  -  좀비 : 자식이 종료 했는데, 부모가 자식 종료 코드 회수 X -> 프로세스 테이블 상에만 남아있고, 자원은 모두 회수된 상태
      - 부모의 wait()으로 정상적 종료 가능
4. 데몬
  - 시스템 부팅 시 자동으로 백그라운드 실행
  - 사용자 제어 X
  - 주기적, 지속적인 서비스 요청 처리
  - cron, ftpd, lpd, rlogind, rshd, telnetd 등

### 프로세스 동작 원리
1. exec() : 새로운 프로세스의 이미지로 교체
2. fork() : 부모, 자식 관계. 자식이 부모 복제(메모리 락, 세마포터, 비동기 IO는 상속 X)

부모 -> fork() -> 자식 -> exec() -> 실행 -> exit() -> 자원 회수 -> wait() -> 부모 

1. Foreground Process : 프로세스 실행될 때 셸은 블록이 되도록 하는 프로세스
  - 사용자 입력 받을 수 있음
  - 터미널, 그래픽 확인 가능
2. Background Process  : 오래 걸리면 전환
  - `&` 붙여서 실행
  - `[` `]` 사이 숫자는 **작업 번호**, 그 뒤는 PID
    ```
    $ ls ch*.ppt &
    [1] 12131
    # 작업 번호 1, PID 12131
    ```
3. FG <-> BG 전환
   - FG -> BG : 프로세스 suspend 후 , BG 명령어 사용
   - BG -> FG : fg
   - <mark>현재 실행중인 작업의 정보를 보기 위해서 `jobs` 명령어 사용
     ```bash
     $ jobs
     [1] Running bash ....
     [2]- Running evolution &
     [3]+ Done ...
     ```
4. 우선순위
  - PR : 리눅스 커널이 관리
    - 0 ~ 139
    - 0 ~ 99 실시간 테스크
    - 100 ~ 139 사용자 할당
  - NI : 사용자가 정하는 우선순위
    - nice : 프로세스 시작 시 설정
    - renice : 실행중인 프로세스 설정
    - -20 ~ 19
    - 음수인 -20 ~ -1 은 root 사용자만이 할당 가능
   

### 프로세스 중지
1. `kill`
  - PID 지정 -> 종료
  - 직접 생성한 거 kill
  - root 사용자는 시스템 프로세스 kill
  - 남의 프로세스 root만 kill

|시그널 번호| 이름| 설명 | 
|--|--|----|
|1|SIGHUP| 터미널 접속 끊길 때|
|2|SIGINT| CTRL + C 인터럽트 발생|
|3|SIGQUIT| CTRL + / 입력 시|
|9|SIGKILL|강제 종료|
|15|SIGTERM| 정상 종료|
|18|SIGCONT|STOP->재개|
|19|SIGSTOP|중지|
|20|SIGSTP|프로세스 대기|

2. 프로세스 상태 : `PS` 나 `TOP` 명령어로 프로세스 상태 확인
  - R : 실행
  - D : DEEPSLEEP -> IO로 방해 금지
  - S : SLEEP : 기다리는 중, 인터럽트 가능
  - Z
  - T

3. 프로세스 구조
   - PCB : 프로세스 정보 관리
   - PT : PID + PCB -> **모든 프로세스 관리**

### 데몬 
1. standalone 
  - 사용자 요청 X, 자동으로 백그라운드 대기
  - 즉각적인 반응
  - 비효율적, 요청 빈번해야 사용
  - /etc/systemd/system에서 `.service`로 끝나는 위치
    - [Install] 섹션을 통해서 바로 시작하도록 설정 가능
2. xinetd 방식(eXtended interNET)
  - 필요할 때 로드
  - 요청 빈번하지 않을 때 로드
  - inetd -> xinetd가 처리
3. systemd의 on-demand
  - `.socket` 와 `.service` 로 데몬 실행

### systemd
CentOS 7에서 데몬 시작하는 명령어
```bash
systemctl stop/start/restart/reload httpd.service

# 부팅시 자동 실행되도록 하기 위해서
sudo systemctl enable httpd.service
# root만이 할 수 있기에
```

### 데몬 설정 도구
1. ntsysv : 터미널에서 부팅 중 실행할 데몬 설정 유틸리티 (centOS 6)
2. chkconfig : 데몬 실행 설정 목록, 실행 데몬 추가, 삭제 등 (centOS 6)
3. systemctl : 기본 systemd 관련 데몬 설정 명령어
  - systemctl -H .... (원격지에 있는 거 관리)
  - systemctl set-property (서비스 CPU, 메모리 사용량 제한)
  - systemctl list-sockets (연결 대기 중인 소켓 목록 확인)
4. systemd-cgtop : control group에 속합 <mark>데몬에 대한 CPU, 메모리, IO 등 실시간 정보</mark>
5. systemd-cgls : cgroup에 대한 정보 계층적 출력
6. systemd-analyze : 부팅시 걸린 시간 확인, `blame`을 통해서 서비스 시작 시간 출력
