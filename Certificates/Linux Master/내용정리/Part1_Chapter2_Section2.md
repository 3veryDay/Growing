# 리눅스 구조

## Boot Manager = Boot Loader

(보조 기억 장치에 위치한) OS를 주기억장치로 로드 하기 위한 프로그램
Linux에서는 대표적으로 **GRUB** 하고 **LILO**가 있음. 

1. LILO
   - 표준, 가장 오래됨
   - 개선되고 있음
   - `/etc/lilo.conf`에서 설정하고 MBR로 다시 쓰기 위해서 `lilo` 명령어 사용
  
2. GRUB
   - GNU 개발
   - 대화형 명령어 인터페이스
   - 네트워크 부팅
   - `/boot/grub/grub.conf`에서 설정, 바로 적용됨

3. GRUB2
   - GRUB에서 완전히 새로 작성
   - 다양한 아키텍쳐, 다양한 펌웨어 지원
   - 정식 GPT 지원
   - RAID, LVM 지원
   - 파일 시스템 지원
   - 다른 OS 지원
   - `/boot/grub/grub.cfg`에서 설정
  

##### 동작 순서
1. **BIOS** 가 Boot Sector에 있는 `MBR`(Master Boot Record) 읽음
2. `IPL`이 먼저 실행되며, 파티션 테이블 검사 -> 나머지 코드 위치 알아냄

##### GRUB 사용

초기 화면에서 
- e : 설정 변경
- a : 커널에게 인자 수정 (GRUB2에서는 없음)
- c : 명령줄 모드
- `grub2-mkconfig` 명령어를 통해서 `/boot/grub2/grub2.cfg` 환경설정 파일 수정

###### /boot/grub2/grub2.cfg
- set timeout = 10 : 사용자에게 시간 줌
- set default = 0 : 사용자가 안 정하면 0, 1은 `grub.cfg`상에서 설정한 운영체제
- set root=(hd1,2) : 루트 디바이스 설정
- linux16 : 커널 이미지 경로 (GRUB에서의 kernel)
- initrd16 : 램디스크 이미지에 대한 경로 (GRUB에서 initrd)

##### /etc/default/grub
- 여기서 `grub.cfg`가 생성됨.
- 이 파일 수정하기 위해서는 `grub2-mkconfig` 명령어 사용
- GRUB_TIMEOUT " 사용자 시간 줌
- GRUB_DISTRIBUTOR : 메뉴 항목 제목
- GRUB_DEFAULT : 부팅할 때 기본. "saved"는 `grub2-set-default`이랑 `grub2-reboot` 설정된 값을 사용
- GRUB_DISABLE_SUBMENU : 메뉴 아래 서브 메뉴 표시
- GRUB_CMDLINE_LINUX : 커널 부트 파라미터
- GRUB_DISABLE_RECOVERY : true이면 복구를 위한 메뉴 항목이 보여짐



# 주요 디렉터리
리눅스는 FHS를 따름
|디렉터리| 설명 | 
|--|----|
|/|최상위|
|/bin/ | 모든 사용자의 명령어-ls, cp ...|
|/boot/|부팅 관련|
|/dev/|디바이스 파일|
|/etc/|Extended Tool Chest : 시스템 환경 설정 파일, 스크립트 파일, init 의 환경설정 파일 |
|/home/|로그인한 사용자 파일, 등 사용자 전용 홈 디렉터리. 사용자 계정별로 폴더 생성|
|/lib/|각종 라이브러리 저장, /lib/modules에는 설치된 커널의 모듈이 위치|
|/media/|CD-ROM 이나 이동식 디스크가 시스템에 마운트 시 사용|
|/mnt/|다양한 디바이스가 마운트할 때 사용하는 임시 dir|
|/opt/|추가 app sw package|
|/proc/|메모리에 있는 모든 프로세스들이 파일 형태로 매핑. **가상 파일 시스템**으로 구현, 프로세스 상태 정보, 하드웨어 정보 등 시스템 정보 확인 |
|/root/| 루트 사용자 홈 dir |
|/sbin/|**root가 사용하는 시스템 관리 명령어**, <mark>shutdown, ifconfig 등 </mark>|
|/tmp/| 각종 프로그램들이 임시 파일 생성하는 dir , /var/tmp로 퍼미션은 1777, sticky bit 있음 |
|/usr/|<mark>사용자들이 사용하기 위해 설치한 주요 명령어</mark> |
|/usr/bin/| 대부분 사용자 명령어|
|/usr/include/|프로그래밍 언어 사용하는 헤더 파일|
|/usr/lib/| `usr/bin` 와 `usr/sbin`에 있는 바이너리에 링크하기 위한 라이브러리|
|/usr/sbin/|상대적으로 중요하지 않은 명령어 위치|
|/var/| 로그, 스풀 파일 등 임시로 생성, 상황에 따라 생성, 삭제|
|/run/| 부팅 이후 시스템의 실행 중 프로세스, 로그인한 사용자와 같은 런타임 데이터 포함|
|/sys/| 핫플러그 장치를 위한 sysfs 가상 파일 시스템을 통해 장치 정보 제공  == /proc와 유사 |

# GRUB
관련해서는 많이 안 나옴

# systemd

기존 SysV init 대체하기 위한 시스템 및 서비스를 위한 Manager 역할
- LGPL 라이선스
- 기존 sysV init 와 호환
- 병렬 서비스 시작
- 시작 순서 제어
- UNIT 단위로 관리

### systemd 구조

##### UNIT
systemd는 시스템 관리하기 위해서 다양한 유닛 제공
|UNIT|확장자|설명|
|--|--|-----------|
|Service Unit|.service| 서비스/데몬|
|Target Unit|.target|다수를 하나의 그룹으로 관리|
|Device Unit|.device|커널이 인식 가능한 장치 관리|
|Mount Unit |.mount|파일 시스템 마운트 포인트|
|Path Unit|.path|파일 시스템의 파일과 디렉터리|
|Socket Unit|.socket|IPC, 프로세스 통신|
|Timer Unit|.timer|systemd 타이머|

|경로| 설명 |
|--- |--------|
|/usr/lib/systemd/system/| RPM으로 설치된 유닛이 여기있음|
|/run/systemd/system|실행 시 생성된 유닛, 위의 경로보다 이 경로가 더 우선시됨|
|/etc/systemd/system/|systemctl enable 명령을 통해 생성된 유닛, 위보다 이게 더 우선시 됨|

유닛 파일의 구조는 [Unit] [Unit type] [Install]로 구성된다.
- [UNIT] : 공통 사항
  - Description : 유닛 설명
  - Documentation : 유닛 설명 있는 URIs
  - After : 유닛이 시작할 순사
  - Requires : 의존 관계
  - Wants : REquires보다 약한 의존성
- [Unit Type] :특성
  - Service 유닛은 [Service]
    - ExecStart : 실행 시 실행할 명령어, 스크립트
    - ExecStop : 유닛 중지 시 실행할 명령어, 스크립트
- [Install] : systemctl enable/disable 로 유닛을 제어할 때 필요한 정보
  - RequireBy : 의존 유닛 지정
  - WantedBy : 약한 의존 목록

 ##### Systemd의 주요 명령어
 ```bash
# service start
systemctl start name.service

# service stop
systemctl stop name.service

# service restart
systemctl restart name.service

#서비스 실행 중인 경우만 재시작
systemctl try-restart name.service

# 서비스 설정 갱신
systemctl reload name.service

# 서비스 상태 확인
systemctl status name.service

# 서비스 목록 확인
systemctl list-units--type service --all
```
타켓 유닛
```bash
# default target 확인
systemctl get-default

# loaded target check
systemctl list-units --type target

# change default target
systemctl set-default name.target
#########################################################################
# current target change                                                 #
systemctl isolate name.target                                           #
#########################################################################

# 복구 모드 변경
systemctl rescue

# 응급 모드 변경
systemctl emergency
```

전원 관리
```bash
# halt
systemctl halt

systemctl poweroff

systemctl reboot

systemctl suspend

systemctl hibernate

# 하이버네이드 및 서스팬드
systemctl hyrid-sleep
```

<mark> systemctl -H root@linuxserver.example.com status httpd.service</mark>
--host 또는 -H 옵션을 사용해서 <mark> 원격지 sshd 서비스 연결 </mark>

### 파일 시스템

