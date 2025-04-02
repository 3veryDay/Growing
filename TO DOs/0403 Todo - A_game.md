
# 🧭 통합 타임라인 (인터벌 + 음악 연동 중심)

## 0단계: 기획 및 구조 설계

| 항목 | 내용 |
|------|------|
| 🎯 목표 | 인터벌 구간마다 음악이 자동으로 전환되도록 구성 |
| 📦 구조 설계 |  
- 인터벌 상태 (`currentSegmentIndex`, `segmentList`, `timeLeft`, `isRunning`)  
- 음악 상태 (`currentTrack`, `trackList`, `playerReady`, `isPremium`)  
- 두 상태를 **공통 Context (또는 전역 상태)** 로 공유하여 연동 처리 |
| 🎧 트랙 할당 로직 |  
- `segmentList.length === trackList.length` 가 보장되도록  
- 각 인터벌 구간에 맞는 음악 리스트를 먼저 구성해놓음 |

---

## 1단계: 음악 선택 및 설정 페이지 (MusicSetupPage)

### 💻 프론트 작업

- [ ] 음악 선택 유형: `Random`, `Recommended`, `Artist`, `Keyword`  
- [ ] 선택 유형에 따라 입력 필드 동적 렌더링
- [ ] "음악 리스트 만들기" 버튼 누르면 → 음악 리스트 생성 요청

### 🔌 백엔드 작업

- [ ] Spotify Access Token 확인 및 저장
- [ ] Spotify API로 음악 리스트 생성 (길이 = 인터벌 세그먼트 수)
- [ ] 응답: `{ tracks: [track1, track2, ...] }`

---

## 2단계: 음악 리스트 미리보기 및 선택 확인

- [ ] 생성된 트랙 목록을 UI에 표시 (썸네일 + 제목 + 아티스트)
- [ ] “확인” 누르면 `trackList` 상태에 저장

> ✅ 이 시점에서 `segmentList.length === trackList.length` 가 보장됨

---

## 3단계: 인터벌 실행 페이지 (IntervalRunningPage)

### 📦 상태 연동 구조

- `intervalContext` → 현재 구간 인덱스 (`currentIndex`), 타이머 상태
- `musicContext` → 현재 트랙 인덱스, 재생 컨트롤 함수

### ⏱️ 타이머 흐름과 음악 제어 연동

| 인터벌 타이머 이벤트 | 음악 동작 |
|---------------------|-----------|
| 구간 시작 시 | `playTrack(trackList[currentIndex])` 호출 |
| 구간 전환 시 | 다음 트랙으로 `skipToTrack(index + 1)` |
| 일시정지 | 음악도 일시정지 (`pause()`) |
| 재개 | 음악 재개 (`resume()`) |
| 인터벌 종료 | 음악 정지 or 마지막 트랙 반복 |

> 🎧 `playTrack(track)` 함수는 Spotify Web Playback SDK 사용

---

## 4단계: Spotify Web Playback SDK 연동

- [ ] 사용자 프리미엄 여부 확인
- [ ] SDK 초기화 → 디바이스 등록
- [ ] 음악 제어 함수 구현  
  - `playTrack(trackUri: string)`
  - `pause()`
  - `resume()`
  - `skipToTrack(index: number)`

---

## 5단계: UI 상태 연동

- [ ] 재생 중인 음악 정보 표시 (앨범 커버, 트랙명, 아티스트)
- [ ] 진행 시간 표시 (interval timer + music progress bar)
- [ ] 일시정지, 다시시작 버튼 연동
- [ ] 비프리미엄 사용자 예외 처리

---

# 💡 주요 상태 구조 예시 (React + Context)

```ts
// musicContext.tsx
{
  trackList: Track[],
  currentTrackIndex: number,
  playTrack: (index: number) => void,
  pause: () => void,
  resume: () => void,
  isPremium: boolean,
}
```

```ts
// intervalContext.tsx
{
  segmentList: Segment[],
  currentSegmentIndex: number,
  isRunning: boolean,
  timeLeft: number,
  nextSegment: () => void,
  pause: () => void,
}
```

→ `IntervalRunningPage`에서 useEffect로 감지하여 `currentSegmentIndex`가 바뀔 때마다 `musicContext.playTrack(currentIndex)` 호출.

---

## ⏳ 예상 작업 기간

| 단계 | 기간 | 난이도 |
|------|------|--------|
| 구조 설계 + 상태 정의 | 0.5일 | 중 |
| 음악 선택 UI + 트랙 생성 | 1일 | 중 |
| 트랙 리스트 연동 + 미리보기 | 0.5일 | 중하 |
| 인터벌 타이머 ↔ 음악 연동 | 1.5일 | 중상 |
| Spotify SDK 연동 및 디버깅 | 1.5일 | 상 |
| UI/UX 마무리 + 예외처리 | 0.5일 | 중 |
