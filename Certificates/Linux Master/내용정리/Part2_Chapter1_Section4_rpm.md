# 패키지를 통한 소프트웨어 설치
- 사용자의 환경설정에 맞게 **미리 컴파일된 프로그램**을 **PACKAGE**라는 형태로 제작, 배포함.
- |배포판|저수준 패키지 도구|고수준 패키지 도구|
  |--|--|--|
  |레드햇, centOS 계열 | rpm | yum |
  |데비안 계열 |dpkg|apt, apt-get, aptitude|
  |openSUSE|rpm|zipper/YasT|

# 저수준 패키지 사용하기
```bash
# install
rpm -i file.rpm
dpkg -i file.deb

# upgrade
rpm -U file.rpm
dpkg -U file.deb

# 설치된 패키지 확인(모든)
rpm -qa
dpkg -l

# 특정 패키지 확인 or use grep
rpm -q file.rpm
dpkg --status file.deb

# 특정 파일이 어떤 패키지를 통해 설치되었는지
rpm -qf file_name
dpkg --search file_name
```

# 고수준 패키지 사용하기
```bash
# 검색하기
yum search package_name
#패키지에 대한 모든 정보에서 검색을 시도
yum search all package_name
#특정 파일이 포함된 패키지를 찾음
yum whatprovides"/package_name"


#데비안 계열 -search
# apt-cache, 패키지명, 패키지의 설명 등의 키워드 검색
apt-cache search [검색어]

# apt 와 aptitude는 패키지명만 검색
apt search [검색어]
aptitude search [검색어]

# 설치하기
# update 통해서 패키지 정보 갱신 -> install 사용해서 다운로드 받아 설치
yum update && yum install package_name
apt-get update && apt-get install package name

#제거하기
yum erase package_name
apt-get remove package name
apt-get purge package name  # 환경 설정 파일도 삭제

# 패키지 정보 출력
yum info package name
apt-cache show package name
apt show package name
aptitute show package_name

```

| 분류               | rpm                                | yum                                 | dpkg                              | apt / apt-get                                |
|--------------------|-------------------------------------|--------------------------------------|------------------------------------|----------------------------------------------|
| 📌 설치             | rpm -ivh pkg.rpm                    | yum install pkg                      | dpkg -i pkg.deb                    | apt install pkg / apt-get install pkg        |
| ▶ 설치 (강제)       | rpm -ivh --force pkg.rpm            | –                                    | dpkg -i --force-all pkg.deb        | apt install -o Dpkg::Options::="--force-all" |
| ▶ 설치 시 test     | rpm --test -ivh pkg.rpm             | –                                    | –                                  | –                                            |
| ▶ 의존성 무시      | rpm -ivh --nodeps pkg.rpm           | yum install pkg --skip-broken        | dpkg -i --force-depends            | apt-get -f install (의존성 해결 전용)        |
| ▶ 자동 의존성 해결 | ❌                                   | ✅ 기본 지원                          | ❌                                  | ✅ 기본 지원                                 |
| ▶ -y 자동 Yes      | –                                   | yum install -y pkg                   | –                                  | apt install -y pkg                           |
| 📌 업데이트         | –                                   | yum update pkg                       | –                                  | apt install --only-upgrade pkg               |
| ▶ 전체 업데이트     | –                                   | yum update                           | –                                  | apt update && apt upgrade                    |
| ▶ 전체 업그레이드   | –                                   | yum upgrade                          | –                                  | apt full-upgrade                             |
| ▶ 설치 + 없으면 설치| –                                   | yum install pkg                      | –                                  | apt install pkg                              |
| 📌 삭제             | rpm -e pkg                          | yum remove pkg                       | dpkg -r pkg                        | apt remove pkg / apt-get remove pkg          |
| ▶ 강제 삭제         | rpm -e --nodeps pkg                 | yum remove --setopt=clean_requirements_on_remove=1 pkg | dpkg --purge pkg      | apt purge pkg                               |
| 📌 질의             | rpm -q pkg                          | yum list installed | grep pkg        | dpkg -s pkg                        | apt show pkg                                 |
| ▶ 설치 여부         | rpm -q pkg                          | yum list installed | grep pkg        | dpkg -l | grep pkg                | apt list --installed | grep pkg           |
| ▶ 파일 목록         | rpm -ql pkg                         | –                                    | dpkg -L pkg                        | –                                            |
| ▶ 파일 소속 패키지  | rpm -qf /경로/파일명                | –                                    | dpkg -S /경로/파일명               | apt-file search /경로/파일명 (apt-file 필요) |
| ▶ 의존성 확인       | rpm -qpR pkg.rpm                    | yum deplist pkg                      | –                                  | apt depends pkg                              |
| ▶ 제공하는 패키지   | –                                   | repoquery --whatprovides /파일명     | –                                  | apt-file search /파일명                      |
| 📌 검증             | rpm -V pkg                          | –                                    | –                                  | –                                            |
| ▶ 무결성 검사       | rpm -K pkg.rpm                      | –                                    | –                                  | –                                            |
| 📌 검색             | rpm -qa | grep pkg                  | yum search 키워드                    | dpkg -l | grep 키워드              | apt search 키워드                            |
| 📌 캐시/청소        | –                                   | yum clean all                        | –                                  | apt clean                                    |
| 📌 기록(history)    | –                                   | yum history                          | –                                  | –                                            |

#### 📌 rpm 관련
- rpm -K pkg.rpm : 패키지 무결성 검사
- rpm2cpio pkg.rpm | cpio -idmv : rpm 파일 압축 해제

#### 📌 yum 관련
- yum history : 설치/삭제 이력 조회
- yum repolist : 활성화된 저장소 목록 보기
- yum-config-manager --enable repo : 저장소 활성화
- yum-config-manager --disable repo : 저장소 비활성화

#### 📌 dpkg 관련
- dpkg-reconfigure pkg : 설정 재실행 (ex. locale 설정 등)
- dpkg --get-selections : 모든 설치된 패키지 목록 출력

#### 📌 apt 관련 (apt vs apt-get)
- apt는 apt-get + apt-cache 통합 명령어로, 사용자 친화적 출력 제공 (Debian 8+/Ubuntu 16.04+)
- apt edit-sources : /etc/apt/sources.list 편집
- apt policy pkg : 패키지의 설치 후보 우선순위 확인



























