# X 윈도우
- 서버 클라이언트 구조를 기반으로 **X 프로토콜**을 통해 -> 윈도우 그려줌, 상호작용
- **X프로토콜**이라는 네트워크 프로토콜 사용
- 네트워크 연결 -> 사용 가능
- X 클라이언트는 X 서버에서 동작하는 응용 프로그램 실행 가능 -> 직접 설치 X
- 사용자 인터페이스에 독립적(KDE, GNOME, XFCE등은 클라이언트 임)
- 쉽게 X윈도우 이식 가능

### X 윈도우 구조
1. X서버
  - 키보드, 마우스 화면과 같은 디바이스와 통신, 관리
  - 디스플레이 서비스 제공
  - `/tmp/.X11-unix/X0` 사용해서 X 클라이언트와 통신
  - TCP 6000 사용해서 통신
  - 다수의 X 클라이언트와 연결
  - 대표적 오픈 소스 프로젝트 : XFree86, X.org
2. X 클라이언트
  - Xlib 사용하여 작성된 응용 프로그램
  - 디스플레이관련 서비스 서버에게 요청
  - X 서버에서 발생한 이벤트 처리
3. X 프로토콜
  - X서버<-> 클라이언트 사이 통신 규약
  - 기본 메시지는 `Request`, `Reply`, `Event`, `Error`로 구성
  - request, event queue를 관리한다.
  - X 프로토콜 -> 높은 이식성
4. Xlib / XCB
  - C언어 작성, X윈도우 시스템 프로토콜 클라이언트 라이브러리
  - API 통해서 X 클라이언트 개발 가능
  - Xlib 대체하기 위해 XCB -> X.org에서 사용
5. XToolKit
  - Xt라고 불림
  - GUI 프로그램 개발을 위해 C/C++ 로 개발된 API 프레임워크
  - 버튼, 메뉴 등 그래픽 요소를 위해 등장
  - XaW, Motif와 같은 다른 라이브러리를 통해 간접적으로 제공
  - <mark>GTK+, Qt, FLTK는 Xlib/XCB 기반</mark> Xtoolkit은 안 사용

### XFree86, X.org
XFree86
- 1992-2004 사용
- 2004 발표된 버전이 GPL 안 따라서, X.org 사용

X.org
- 2004에 시작
- 커뮤니티 주도 프로젝트

### X 윈도우 계층
1. 디스플레이 매니저
  - 윈도우 매니저 전에 뜸
  - 로그인 유저 인터페이스 (login Manager)
  - 원격지의 윈도우 매니저 실행
  - XDM, GDM, KDM
2. X 세션
  - 서버 <-> 클라이언트 연결 -> 생성
  - X 프로토콜을 통해 메시지 왔다리 갔다리
3. 윈도우 매니저
  - 윈도우 그래픽 요소 관리
  - 런처, 데스크톱 아이콘, 바탕화면 등 유틸리티 제공
    |윈도우 매니저 유형|설명|사례|
    |---|------|----|
    |스택형(Stacking)|쌓는 형태로 관리|MVM, WIndowMaker|
    |타일형(Tiling)|서로 안 겹치게 관리|i3, XWEM|
    |복합형(Compositing)|자신의 버퍼를 가진 채 스택, 각 윈도우마다 시각 효과| GNOME Mutter, Unity Compix, KDE Kwin|
    |가상형|자신의 디스플레이보다 더 높은 화상도의 가상 스크린|FVWM, HaZe|
4. 데스크탑 환경
  - 윈도우 매니저가 안 챙기는 다른 애플리케이션
  - GNOME, KDE, XFCE, LXDE

### 데스크탑 환경 구성 사례 (KDE, GNOME)

KDE
- Qt 기반
- 오픈 소스
- 다른 플렛폼도 지원
- 디스플레이 매니저 - KDM
- 파일 관리자 - Konqueror
- 윈도우 매니저 - Kwin(KWM)

GNOME
- GNU 개발
- 공개 데스크탑환경
- LGPL 라이선스의 GTK+ 라이브러리 사용
- 디스플레이 매니저 - GDM
- 파일 관리자 - nautilus
- 윈도우 매니저 - Metacity / Mutter

### X 윈도우 실행(CentOS 7 기준)
```bash
#기본값 변경
systemctl set-default graphical.target

#변경된 내용 확인
systemctl get-default

#터미널 모드에서 X 윈도우 바로 실행
systemctl isolate graphical.target
```

##### 터미널에서 X 윈도우 실행하기
```bash
#userid, pw 입력
#X윈도우 실행하기
startx
```
##### 원격지에서 X윈도우 실행하기
```bash
#xhost을 통해서 클라이언트 지정
#접근 목록 출력
xhost

#모든 클라이언트 접속 허용
xhost +

#모든 클라이언트 접속 차단
xhost -

#특정 IP 허용/차단
xhost +/- <IP>

## Display
# 윈도우를 표시할 서버의 주소를 설정하기 위해서 DISPLAY
export DISPLAY = "<IP>"

## xauth
#.Xauthority 파일의 쿠키 내용 생성, 삭제, 리스트 출력
# MMC 기반 인증 방식
xauth list

xauth add
```
### 추가 응용 프로그램
대표적으로
문서 관리 : evince, LibreOffice

