
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
\



좋아! 차근차근 네가 말한 **4가지 개선 포인트**를 하나씩 해결해보자. 그에 맞게 **개선된 코드도 함께 제공**할게.

---

## ✅ 1. hover 안 되는 문제 (리스트)

> 🔍 문제 원인: Tailwind `hover:` 스타일은 `li`에서도 **정상 작동**함. 다만 다음을 확인해야 함:

### ✅ 해결 방법
- `li` 자체에 `hover:`가 들어갔는지 확인
- 리스트 항목에 **배경색 변화** 같은 효과를 줘야 눈에 띔

### ✅ 개선 코드

```jsx
<li
  key={track.id}
  onClick={() => setTrackUri(uri)}
  className={`cursor-pointer px-2 py-1 rounded transition-colors duration-150
    hover:bg-gray-200 ${uri === trackUri ? 'bg-green-100 font-semibold' : ''}`}
>
  🎵 {track.name} - {track.artists.map(a => a.name).join(', ')}
</li>
```

- `transition-colors duration-150` → 부드럽게 hover 효과
- `hover:bg-gray-200` → 좀 더 명확한 색으로 변경

---

## ✅ 2. 앨범 커버 크기 조절 (너무 큼)

> 🔍 `w-40`은 10rem (약 160px)이라 클 수 있음

### ✅ 개선 코드 (너가 말한 1/5 사이즈로)

```jsx
<img
  src={trackInfo.album.images[0].url}
  alt="앨범 커버"
  className="mt-2 w-20 rounded shadow" // ✅ w-20 = 5rem = 약 80px
/>
```

> 필요 시 `w-16`(64px), `w-12`(48px) 등으로 더 줄일 수 있어

---

## ✅ 3. 재생이 안 되는 이유

재생이 안 되는 경우는 대표적으로 아래 중 하나야:

### 🔍 체크리스트
- [ ] **프리미엄 계정**인가? (Web Playback SDK는 프리미엄만 가능)
- [ ] `deviceId`가 **정상 설정**되었는가?
- [ ] `trackUri`가 바뀐 후 재생 요청이 제대로 전송되었는가?

### ✅ 개선 팁
`controlPlayback('play')` 시점에 console.log로 `trackUri`와 `deviceId`를 출력해봐:

```js
if (action === 'play') {
  console.log("🎯 재생 시도 - URI:", trackUri, "Device ID:", deviceId); // ✅ 로그 추가
  body = JSON.stringify({
    track_uri: trackUri,
    device_id: deviceId,
  });
}
```

### ✅ 보너스: 재생 API 예시 (백엔드 없이도 사용 가능)
```ts
PUT https://api.spotify.com/v1/me/player/play?device_id={deviceId}
Body: {
  uris: ["spotify:track:xxx"]
}
```

---

## ✅ 4. 후렴구(chorus) 시작을 알 수 있는 방법?

> 🧠 Spotify 자체 API에는 후렴구(chorus) 타임 정보는 제공되지 않아.  
다만 다음과 같은 **대체 방법**이 있어:

### 🔧 방법 1: [Spotify Audio Analysis API](https://developer.spotify.com/documentation/web-api/reference/get-audio-analysis)
- `/audio-analysis/{id}` 엔드포인트 사용
- `"sections"` 배열을 분석해서 가장 에너지 높은 section을 "후렴"으로 추정 가능

```js
fetch(`https://api.spotify.com/v1/audio-analysis/${trackId}`, {
  headers: {
    Authorization: `Bearer ${token}`
  }
})
  .then(res => res.json())
  .then(data => {
    const sections = data.sections;
    const chorusCandidate = sections.reduce((prev, curr) =>
      curr.loudness_max > prev.loudness_max ? curr : prev
    );
    console.log("🎶 예상 후렴 시작 시점:", chorusCandidate.start);
  });
```

### 💡 왜 이게 되냐면?
- `"sections"`에 구간별 정보가 들어 있음 (`start`, `duration`, `loudness_max`, `tempo` 등)
- 일반적으로 후렴은 가장 **크고** 눈에 띄는 구간임 → `loudness_max` 기준으로 추정 가능

---

## ✅ 정리

| 문제 | 해결 방법 |
|------|------------|
| hover 안 됨 | Tailwind `hover:bg-gray-200` + `transition-colors` |
| 앨범 커버 큼 | `w-20` 또는 `w-16`으로 줄이기 |
| 재생 안 됨 | 프리미엄 여부 + `deviceId` 확인 + 로그 추가 |
| 후렴 시작 | `audio-analysis` API의 `sections` 분석으로 추정 가능 |

---

필요하면 내가 후렴 추정까지 통합한 코드도 만들어줄게 😉  
어떤 거 먼저 진행할까?
