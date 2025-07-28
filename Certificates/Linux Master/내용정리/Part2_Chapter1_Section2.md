# 주변 장치 관리

### 디스크 확장

> 하드 디스크 시스템 부착 -> 확장 파티션 생성-> 논리 파티션 생성 -> 파티션 포맷 -> 마운트- -> 확인 -> `/etc/fstab` 등록

1. 하드 디스크 시스템에 부착
  - 시스템 끄고 장착 후 킴
  - `fdisk -l` 로 장착되었는지 확인
  - `/dev/sdb`가 추가되었을 것임
2. 확장 파티션 생성
   ```bash
   sudo fdisk /dev/sdb
   # 명령어 입력:
   n   # 새 파티션 생성
   e   # 확장 파티션 선택
   (파티션 번호, 시작·끝 섹터 설정)
   w   # 저장 후 종료
   ```
3. 논리적 파티션 생성
   ```bash
   sudo fdisk /dev/sdb
   n   # 새 파티션 생성
   l   # 논리 파티션 선택
   w   # 저장 후 종료
   ```
   - 일반적으로 `/dev/sdb5`부터 시작됨
4. 파티션 포맷
  - ext4파일 시스템으로 방금 생성한 논리 파티션 포맷함.(디스크 초기화)
  - sudo mkfs.ext4 /dev/sdb5
5. 마운트
  - <mark> 대상이 되는 디렉터리는 미리 생성되어 있어야 함</mark>
  - sudo mount -t ext4 /dev/sdb5 /home/francis/tmp
6. 확인
  - `df` 명령어 통해서 하드디스크 확인(크기, 용량 등)
7. /etc/fstab에 등록
   ```bash
   sudo vi /etc/fstab

   # 아래 내용 추가:
   /dev/sdb5   /home/francis/tmp   ext4   defaults   0 0
   ```

### 프린터

- **CUPS (Common Unix Printing System)**
  - 유닉스 계열 프린팅 시스템
  - HTTP 기반, IPP/SMB 프로토콜 지원
  - BSD, System V 명령 체계 모두 지원

|BSD 명령어 | System V| 설명 |
|---|---|--|
|lpr|lp | 문서를 프린터로 출력 | 
|lprm|cancel | 대기열에 있는 작업 번호를 통해 작업 취소 (지정 X ,  현재 취소) |
|lpc |lpq|lpc는 대기열 제어, 상태 . lpq는 대기열 상태 출력 |
| | lpstat| 현재 설정된 프린터, 클래스, 인쇄 작업에 대한 정보 출력 |


### 사운드 카드

##### OSS (Open Sound System)
- 유닉스 계열 시스템용 사운드 드라이버
- `read`, `write`, `ioctl` 기반 시스템 콜 지원
- 기본 출력 장치: `/dev/dsp`

##### ALSA (Advanced Linux Sound Architecture)
- 리눅스 전용 사운드 시스템
- OSS보다 성능 우수, 다채널 지원


### 스캐너

##### SANE(Scanner Access Now Easy)
- 오픈소스 스캐너 API (GPL 라이선스)
- 리눅스에서 스캐너 장치 접근을 표준화
##### XSANE(X based interface for the SANE)
- GTK+ 기반 그래픽 프론트엔드
- 독립 실행 또는 GIMP 플러그인으로 사용 가능
- 이미지 저장, 팩스 전송, 프린터 출력 지원
- 설치: `sudo yum install xsane`

##### 명령어

| 명령어             | 설명                       |
|--------------------|----------------------------|
| `sane-find-scanner`| 연결된 스캐너 장치 검색     |
| `scanimage`        | 커맨드라인 스캔 수행        |
| `scanadf`          | 자동 문서 공급기 스캔       |
| `xscanimage`       | GUI 기반 스캔 유틸리티      |
