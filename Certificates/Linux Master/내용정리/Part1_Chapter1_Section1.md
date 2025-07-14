# OS 개요

## 정의, 목적, 역할

- OS는 사용자와 하드웨어 사이의 interface 제공하는 `시스템 소프트웨어`이다.
- CPU, 메모리, 주변 장치 등 HW 관리
- 응용 프로그램이 동작 할 수 있는 환경, 즉 `Programming Interface`제공

- Througput : 일정 시간 처리하는 양(up)
- Turnaround Time : 작업하는데 걸리는 시간
- Reliability : 신뢰도
- Availability : 사용 가능도로 이용할 수 있는 시스템 자원의 향상 
-> **TART*** 로 기억.

- HW 제어 입력 출력 관리
- <mark>한정된 하드웨어를 다수의 이용자가 공유할 수 있도록 함.</mark>
- 자원 스케줄링
- **system call** 지원
- 오류 복구 기능
- DB, FILE 제공
- 사용자 편리 인터페이스 제공

## OS 운용 기법

1. 일괄 처리 (Batch Processing System) -> 1세대
2. 다중 프로그래밍 (Multi Programming System) -> 2세대
3. 다중 처리 시스템 (Multi Processing System) -> 2세대
- 여러 CPU 사용 
4. 시분할 시스템 (Time Sharing System) -> 3세대
- time Slice, 또는 Time Quantum 별로 큐에서 실행
5. 실시간 처리 시스템 (Real Time Processing System)
6. 다중 모드 시스템 (Multi Mode System) -> 4세대
- 모두 혼용 
7. 분산 처리 시스템 -> 5세대
- 가상화 기술 기본적으로 내장
- 강결합, 약결합 

## OS 종류
| 구분             | OS 종류              | 설명                                                       |
| -------------- | ------------------ | -------------------------------------------------------- |
| **UNIX 계열**    | System V           | AT\&T 개발. 표준 유닉스. 상용 유닉스의 기반                             |
|                | BSD                | 버클리대 개발. TCP/IP 탑재. FreeBSD, NetBSD 등 파생                 |
|                | AIX                | IBM 개발한 UNIX                                             |
|                | Solaris            | Sun Microsystems UNIX (현재 Oracle 소유)                     |
|                | SCO UNIX           | SCO사 UNIX (상용)                                           |
|                | IRIX               | Silicon Graphics 개발한 UNIX                                |
| **Linux 계열**   | Red Hat Enterprise | RHEL. 기업용 상용 리눅스. 유료 서포트                                 |
|                | CentOS             | RHEL 클론. 지금은 AlmaLinux, RockyLinux로 대체 추세                |
|                | Fedora             | RHEL 테스트베드. 최신 기술 실험용                                    |
|                | Debian             | 안정성 중시. 우분투 기반 OS                                        |
|                | Ubuntu             | 데스크탑/서버 인기 OS. Debian 기반                                 |
|                | Slackware          | 초기 리눅스 배포판 중 하나. 매우 전통적                                  |
|                | SUSE Linux         | 독일 계열 리눅스 배포판. 기업용 SUSE Linux Enterprise Server(SLES) 존재 |
|                | Arch Linux         | 롤링 릴리즈. 최신 패키지 제공                                        |
|                | Kali Linux         | 보안/해킹 용도 배포판. Debian 기반                                  |
| **Windows 계열** | Windows NT         | NT 계열 커널. 서버/워크스테이션용 기반                                  |
|                | Windows Server     | 서버용 OS. Active Directory, IIS 등 포함                       |
|                | Windows 10/11      | 데스크탑 OS                                                  |
| **Mac 계열**     | macOS              | BSD 계열 기반. Apple의 데스크탑 OS                                |
| **모바일 OS**     | Android            | Linux 커널 기반. 구글 모바일 OS                                   |
|                | iOS                | Apple 모바일 OS. macOS 커널과 연관                               |
|                |타이젠                | 인텔 & 삼성. Meego와 함께. 스마트 티비에 탑재 많이 함.           |
| **기타**         | DOS                | Disk Operating System. 초기 PC용 OS                         |
|                | FreeDOS            | DOS 호환 무료 OS                                             |
|                | RTOS               | 실시간 운영체제. 임베디드 시스템에서 사용                                  |
| **임베디드** | 라즈비안              |영국, 데비안 기반                                  |
| **IOT** | Linux          |Android Things, Ubuntu Core                               |
| **IOT** | Windows IOT         |-                              |
| **IOT** | RTOS        |FreeRTOS, VxWorks, QNX                     |
| **IOT** | lightWeight        |Cibtujum TubyISm RIOT                              |




