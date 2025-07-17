| 명령어       | 설명                                 | 자주 나오는 옵션 및 의미                                                                  |
|--------------|--------------------------------------|--------------------------------------------------------------------------------------------|
| ifconfig     | 인터페이스 설정/조회 (구식)           | `-a`: 모든 인터페이스 표시<br>`인터페이스 down`: 비활성화<br>`up`: 활성화                 |
| ip           | 네트워크 인터페이스 설정              | `ip a`(addr): 주소 보기<br>`ip link`: 링크 상태<br>`ip route`: 라우팅<br>`ip neigh`: ARP |
| nmcli        | NetworkManager CLI 도구              | `nmcli device status`: 장치 상태<br>`nmcli con up/down`: 연결 설정/해제                   |
| route        | 라우팅 테이블 확인/설정              | `route -n`: 숫자 주소 출력<br>`add default gw`: 기본 게이트웨이 추가                      |
| arp          | ARP 캐시 조회/삭제                   | `-a`: 전체 목록<br>`-d IP`: 특정 항목 삭제                                                |
| ethtool      | NIC 정보 확인/설정                   | `ethtool eth0`: 기본 정보<br>`-i`: 드라이버 정보<br>`-s`: 속도/듀플렉스 설정              |
| mii-tool     | 링크 상태 점검 (구식)                | `mii-tool`: 기본 출력<br>`-v`: 상세 정보                                                  |
| ping         | ICMP 테스트                          | `-c`: 패킷 수 지정<br>`-i`: 간격<br>`-t`: TTL 설정                                        |
| netstat      | 네트워크 상태 확인 (구식)            | `-tuln`: 열려있는 포트<br>`-r`: 라우팅<br>`-a`: 모든 연결<br>`-p`: PID/프로그램 이름      |
| ss           | 소켓 상태 확인                       | `-tuln`: 열려있는 포트<br>`-a`: 전체<br>`-p`: 프로세스 보기                               |
| traceroute   | 경로 추적                            | `-n`: 호스트 이름 생략<br>`-m`: 최대 홉 지정                                              |
| nslookup     | DNS 조회 도구                        | `nslookup 도메인`                                                                          |
| dig          | DNS 조회 (상세 정보)                 | `dig 도메인`, `+short`, `+trace`                                                           |
| host         | 간단한 DNS 조회                      | `host 도메인`                                                                              |
| hostname     | 현재 호스트 이름 확인                | `-i`: IP 확인<br>`-d`: DNS 도메인명<br>`-f`: 전체 FQDN                                     |
| hostnamectl  | 호스트 이름 설정/관리                | `set-hostname`: 이름 설정                                                                  |
| telnet       | 원격 접속 테스트                     | `telnet IP 포트`: 포트 열림 여부 확인용                                                    |
| ftp          | 파일 전송 프로토콜                   | `ftp IP`, `put`, `get`, `bye` 등 기본 명령어                                               |
