# SHELL
- 커널의 서비스 기능을 수행할 수 있도록 하는 사용자 인터페이스
- CLI / GUI -> linux는 CLI가 더 유명
- 대화형 사용자 인터페이스
- sh : 최초, 기본 (스티븐 본 개발, bournce shell)
- ksh : history, alias, 작업 제어, 콘 개발
- bash : ksh + csh , 가장 많이 사용, GPL lv 3 따름
- csh : C언어 기반, 빌 조이 개발
- tcsh : 티넥스 개발

### SHELL 설정, 확인
```bash
# 현재 로그인 한 사용자 확인
echo $SHELL
/bin/bash

# 시스템이 지원하는 쉘 목록
chsh -l (--list-shells)
/bin/sh
/bin/bash ...

# 시스템이 지원하는 쉘 목록 2
cat /etc/shells

# 쉘 변경은 -c(change)
chsh -c /bin/csh

# 특정 사용자의 쉘 확인은
cat /etc/passwd | grep francis
### 7번째 필드에 사용하는 셸이 있음!!!

# 이외 환경 변수
PATH = '실행 파일이 위치한 디렉터리의 집합'
SHELL = '로그인!! 한 사용자의 셸 보여줌'

# 환경 변수 목록 확인 - 현재 셀의 모든 변수, 환경변수 확인
set

# 환경 변수 값 설정/변경
export MYENV=설정

# 오직 exported 변수만 확인
env
```

### 셸 종류
1. 로그인 유무
   - 비로그인 셸 (셸 안에서 셸 생성, X 윈도우에서 터미널 실행)
   - 로그인 셸
2. 인터렉티브
   - 인터렉티브 셸 : 대화형, 명령 -> 결과 받는 식
   - <mark>비인터렉티브 셸 : Shell Script 에서 셸을 실행하는 경우</mark> -> #!


###### 경우의 수에 따른 리눅스 셸 시작 방법
- Login 셸 -> `/etc/profile` + `/etc/profile.d/*` 실행 -> 각 사용자 별 실행 파일인 `~/.bash_profile` / `~/.bash_login` / `~/profile` 실행
  - 이때 먼저 있는 거 순으로 되면 실행(마지막은 앞이 존재하지 않으면 실행)
- Non-Login + Interactive -> `/etc/bashrc` -> `~/.bashrc` 실행
- Non-Login + Non-Interactive -> $BASH_ENV 에 설정되어있는 스크립트를 `source`을 통해 실행

`logout` `exit 통해서 로그아웃 함.

##### 셸 설정 파일
|구분| 설정 파일 | 설명 | 
|--|----|------|
|**시스템 설정 파일**| /etc/profile| 시스템 전역 설정 파일 |
||/etc/profile.d/*|사용자가 로그인하면 이 모든 파일 실행 |
||/etc/bashrc|시스템 전역, 셸 안에서 셸 실행, 비로그인 셸일 때 로드|
|**사용자 설정 파일**|~/.bash_profile , ~/.bash_login| 사용자가 시스템 로그인 할 때마다 실행, 계속 유지, `source`통해서 변경 사항 반영|
||~/.profile|시스템 로그인 때마다 실행, bash와 관련 없느 사항 기재|
||~/.bashrc| 비로그인 셸에서 실행, 새로운 터미널 열때마다(로그인된 사용자도), alias, 함수 지정|
||~/.bash_logout|로그아웃|

### 셸 기능
- 자동 완성 [TAB]
- history :옵션 없이 쓰면 지정된 명령어 확인
  - `!2` 하면 history에서 2번째 뜨는 명령어 **실행**
  - `-c` 하면 명령어 이력 삭제
  - `!!` 바로 직전 명령어 실행
  - `3` 숫자 입력하면 최근 3개만 출력
- alias
- 명령어 치환
  - ' ' or $ 통해서 명령어 치환
- 표준 입출력 기능
  - 표준 입력 : stdin : 0 : 기본 장치, 보통 키보드
  - 표준 출력 : stdout : 1 : 기본 출력 장치, 보통 모니터
  - 표준 에러 : stderr : 2 : 기본 오류 출력 장치, 보통 모니터
- 리다이렉션
  - >, >>, <, <<
  - `/dev/null` 은 그냥 null 장치(실제 존재하지 ㅇ낳는 논리적 장치
- 파이프 : 명령어 합쳐서 한줄로 구성 or IPC에 사용(프로세스 간 통신)
- 그룹 명령 기능
  - `;` : 나열한 순서대로 명령어 실행
  - `||` : A || B || C  : A 성공하면 바로 A 결과 출력, 실패하면 B로...
  - `&&` : A && B && C : A 성공해야지 B 실행, ... A 실패하면 끝
 
### 셸 프로그래밍
- 셸 스크립팅
- 한번에 일련의 명령어를 실행하도록
- 첫번째 줄에서 `#!` 통해서 해당 스크립트가 사용할 셸 명시

##### 셸 실행 방법
1. ./hello.sh ( chmod 해야함)
2. bash hello.sh // sh hello.sh 등 앞에 존재하는 셸 들어가면 ㄱㅊ
3. . hello.sh
4. source hello.sh

### 매개 변수

##### 위치 매개 변수
cp file1.txt file2.txt
일 때 
$0 -> cp
$1 -> file1.txt
$2 -> file2.txt
$@, $* -> file1.txt or file2.txt

##### 반복문 같은 애들

- if then - elif then - else - fi

- case $변수 in 패턴1) 명령문 - 패턴 2) 명령문 - *) 명령문 - esac

- for do done

- while do done

- until do done

- select do done

- function 이름 { 명령문 }

##### 셸 스크립트의 부분 문자열 제거
- ${string#pattern} : 맨앞부터 패턴과 가장 짧게 매칭된 문자열 삭제
- ${string##pattern} : 맨 앞부터 ... 가장 길게 ...
- ${string%pattern} : 맨 뒤부터 가장 짧게 ...
- ${string%%pattern} : 맨 뒤부터 가장 길게 ... 

