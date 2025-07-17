# 사용자 관리

### 사용자 분류
루트, 시스템, 사용자 3개로 나뉨
- 시스템 계정은 리눅스 설치 시 기본적으로 생성되는 계정 -> 각 역할 별로 제한적인 권한을 가짐

### 루트 계정 관리
루트 = SuperUser(Sudo) -> 제한 없이 어떤 명령어이든 사용 가능, **UID = 0**

- root 사용자는 로그인 할 수 없다.
```bash
# root로 로그인
su

# root 로그인 + 환경변수 로드
su -

# root로 임시 로그인
sudo [명령어]

```
사용자를 root로 변경시키기 위해서는 `/etc/passwd`에 있는 UID를 0으로 바꾸면 된다.


###### 계정을 관리하기 위해서는 
- 시스템 초기에만 로그인 가능하도록, 그리고는 사용 하면 안되게 설정
- root는 유일해야 함.
- PAM을 통해서 root 로 로그인 못하게
- root을 사용해서 TMOUT 있어야 함
- root 로그인 X , sudo 명령어 사용

##### CentOS root 패스워드 분실 시
1. GRUB2에서 환경 설정 변경을 위해 `e` 입력
2. linux 16 옵션에서 `ro` -> `rw`
3. "init=/sysroot/bin/sh" 추가 입력
4. 단일 사용자 모드로 부팅 시도
```bash
# 5. 시스템 접근
chroot /sysroot

# 6. 루트 패스워드 변경
passwd root

# 7.  selinux 정보 갱신
touch /.autorelabel

# 8. chroot 종료
exit

# 9. 시스템 재부팅
reboot
```

### 시스템 계정 관리
시스템 계정이란 특정 서비스에 대한 권한을 행사할 수 있는 계정
- bin, daemon, adm, lp, sync, shutdown, halt, mail 같은 계정
- /etc/passwd에서 UID가 0 ~ 499(RedHat) 0 ~ 999 (Debian) 이다.
- 0~ 99는 시스템 install 시 기본으로 설치되는 시스템 계정
- 그 외는 시스템 운영 시 추가되는 시스템 계정

### 사용자 계정 관리
- UID 범위는 `/etc/login.defs` 에 명시 -> UID_MIN, UID_MAX

##### 사용자 생성
`useradd` & `adduser`
|옵션|설명|
|---|-------------------|
|-d</br>--home|디렉터리 지정</br>기본 값은 기본 경로 + 사용자 이름 |
|-D</br>--defaults|사용자 생성시 사용하는 기본값, 어느 그룹에 속할지, 언제 expire...|
|-e</br>--expiredate|계정 만기일 설정</br>지나면 계정 비활성화</br>`/etc/default/useradd`의 EXPIRE 필드 따름|
|-f</br>--inactive|패스워드 만료일 이후 유효기간</br>n >= 1 : n일만큼 유효,0이면 바로 잠김, -1이면 사용 안함</br>`/etc/default/useradd`의 INACTIVE 필드 따름|
|-g</br>--gid GROUP|사용자 그룹 설정(이미 존재해야 함)|
|-G</br>--groups| 기본 그룹 외 추가로 그룹 설정, `,` 로 여러 그룹 지정|
|-k</br>--skel SKEL_DIR| -m 옵션을 통해 홈 디렉터리 생성할 때 복사할 기본 파일 지정|
|-m</br>--create-home| 홈 지정, 없으면 새 dir 생성</br> 이 옵션 사용 X-> `/etc/login.defs`에 CREATE_HOME` 변수 x-> 홈 DIR 생성 X|
|-M|홈 디렉터리 무조건 설정 안함|
|-N</br>--no-user-group| 사용자와 같은 이름의 그룹 생성 x |
|-p</br>--password PASSWORD| 암호화 된 패스워드 생성|
|-r</br>--system| 시스템 계정 생성|
|-s</br>--shell SHELL| 사용자 셸 지정</br>`/etc/default/useradd`의 SHELL 변수가 디폴트|
|-u</br>--uid UID| UID 설정|


###### 사용자 패스워드 설정
`passwd`는 꼭 `sudo`와 함께 써야 함.
passwd [options] [username]
|옵션|설명|
|--|----------|
|-d</br>--delete| 삭제, 비번 없이 로그인|
|-e</br>--expire|만료 시켜서 다음 로그인때 pw 변경|
|-i</br>--inactive| 비활성까지 유예기간|
|-l</br>--lock| 패스워드에 LOCK 검|
|-n</br>--mindays|최소 비번 유지 기간|
|-q</br>--quiet| 출력 없이 명령|
|-S</br>--status|로그인명, pw 상태, pw 설정?, 마지막 변경 여부, pw 변경까지 남은 기간 정보 제공|
|-u</br>--unlock|락 해제|
|-w</br>--warndays|패스워드 만료 전 경고 날짜 지정|
|-x</br>--maxdays| 패스워드 최대 사용 기간|

##### su, 사용자 전환
su [options] username
|옵션|설명|
|--|--------|
|-c</br>--command|일시적으로 지정한 명령을 실행|
|-</br>-l</br>--login| 직접 로그인했을 떄와 동일하게 환경변수 설정, home dir 이동|
|-s</br>--shell|명시된 셸 사용|

###### usermod
`usermod`

|옵션|설명|
|--|---------|
|-a</br>--append|사용자를 그룹에 추가|
|-c</br>--comment|사용자 코멘트 추가|
|<mark>-d</br>--home</mark>|홈 dir 변경|
|-e</br>--expiredate|사용자 비활성 yyyy-mm-dd|
|-f</br>--inactive|며칠동안 유효(비활성되고)|
|<mark>-l</br>--login|<mark>로그인 이름 변경</mark>|
|-L</br>--lock|락 검|
|-m</br>--move-home|홈-> 새로운 홈|
|-p</br>--password|암호화된 패스워드 설정|
|-s</br>--shell|셸 지정|
|-u</br>--uid UID|UID 지정|
|-U</br>--unlock|LOCK 해제|


##### userdel & chage
`userdel`
- -r : 모두 삭제
- -f :강제 삭제(로그인 된 것도)

`chage`:패스워드 만료 정보
- -d : 변경 날짜 수
- -E : 만료되는 날
- -I : 유예 기간
- -l : 패스워드 만료 정보
- -m : 패스워드 변경까지 min days
- -M : 패스워드 변경까지 max datys
- -W : 만료 경고 메시지 보여줄 날짜 지정


### 그룹 계정 관리

##### groupadd
`groupadd [op] groupname`
- -f, --force : 그룹 생성(이미 있어도 ㄱㅊ)
- -r, --system : 시스템 그룹 생성
- -g, --gid GID :그룹의 양수 GID 지정, -o옵션 선택 안하면 유일한 값 설정
- -o, --non-unique : 중복 GID 허용

##### groupmod
`groupmod [op] groupname`
- -g, --gid : GID 변경
- -n, --new-name : 이름 변경

##### groupdel
- 주 그룹에 존재하는 사용자 없어야 함
- 있으면 사용자를 삭제한 후 그룹 삭제 가능
- 파일 중 그룹에 설정된 파일 없어야 함.

##### gpasswd
- -a, --add user
- -d, --deleteuser
- -r, --remove-password group : `newgrp`으로 참가
- -R, --restrict group
- -A, --administrators user ... : 관리자 지정
- -M, --members user : 그룹 맴버 설정

##### newgrp: 그룹 참여
- 현재 로그인되어있는 세션의 GID 변경
