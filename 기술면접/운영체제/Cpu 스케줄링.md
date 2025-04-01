## CPU 스케줄링

운영체제는 **CPU scheduling에 따라서 CPU를 배분하고, CPU 스케줄링 알고리즘은 이러한 CPU 스케줄링의 절차이며 CPU 스케줄링 알고리즘을 결정하고 수행하는 OS의 일부를 CPU scheduler라고 한다.
>실행의 문맥이 있다면 모두 스케줄링의 대상(프로세스 + 스레드 ...)

##### Priority = 우선순위
운영체제는 **프로세스 별** priority를 판단해서 **PCB**에 명시, 우선순위가 높은 프로세스에는 CPU의 자원을 더 빨리, 많이 할당한다. 
`ps` 명령어를 통해서 프로세스의 우선순위를 확인 할 수 있음

운영체제가 프로세스의 priority를 결정하는 기준
1. CPU Utilization = CPU 활용률 : 전체 CPU 가동 시간 중 작업을 처리하는 시간의 비율
   - CPU 활용 시간 = CPU burst + I/O burst
   - CPU burst : 프로세스가 CPU를 이용하는 작업
   - I/O burst : 입출력 장치를 기다리는 작업
   - 프로세스마다, cpu burst와 I/O burst 시간의 양에는 차이가 있다.
     - I/O bound process = 입출력 집중 프로제스 : 비디오 재생 디스크 백업 작업 등 I/O burst가 많음
     - CPU bound process = CPU 집중 프로세스 : 복잡한 수학 연산, 그래픽 처리 작업 등은 CPU burst가 많음
    
     - I/O bound process는 입출력을 위한 대기 시간이 매우 많고, CPU bound process는 실행 상태에 많이 머무른다.
     - 그렇기에
     - **IO burst process를 가능한 빨리 실행시켜서 끊임없이 입출력 장치를 작동시킨 후, CPU burst process에 집중적으로 CPU 할당을 한다**
     - 입출력 집중 프로세스는 CPU 집중 프로세스보다 우선순위가 높다.
     - 이는 상황에 맞게 CPU를 배분하는 것이 효과적이기에 이렇다.

##### Scheduling queue
CPU를 이용하고 싶은 프로세스의 PCB와 메모리로 적재되고 싶은 프로세스의 PCB, 특정 입출력 장치를 이용하고 싶은 프로세스의 PCB를 큐에 삽입시켜서 줄을 세우는 것

대표적으로 ready queue(준비 큐)와 waiting queue(대기 큐)가 있음
- ready queue: CPU를 이용하고 싶은 프로세스의 PCB의 줄
- waiting queue : 대기 상태에 접어든 프로세스의 PCB의 줄

주로 입출력 작업을 수행중일 때, 대기 큐에서 대기 상태로 입출력 완료 인터럽트를 기다리게 됩니다.
준비 상태인 프로세스의 PCB는 준비 큐의 마지막에 삽입되어서 CPU 차례를 기다린다. 
운영체제는 큐에 삽입된 순서에 따르되, 우선순위가 높은 프로세스부터 먼저 실행한다. 
실행되는 프로세스가 할당받은 시간을 모두 소모하면 (timer interrupt) 준비 큐로 다시 이동
실행 도중 입출력 작업을 수행하는 등 대기 상태로 접어 들어가야 하는 경우 대기 큐로 이동하게 된다.


