---
layout: image
theme: apple-basic
colorSchema: 'auto'
highlighter: shiki
image: '/intro.png'
title: 나만의 챗지피티 만들기

---

---
layout: intro-image-right
image: '/profile.jpg'
---
# Speaker

박나희 (devstone) <br>
이화여자대학교 컴퓨터공학과 19학번

- AWS Cloud Club Ewha 1기 Captin
- GDSC 5기 웹파트 코어멤버
- AUSG(AWSKRUG University Student Group) 6기 member
- [dsrvlabs :](https://www.dsrvlabs.com/) [WELLDONE Studio](https://welldonestudio.io/) Remix ide, plugin software engineer internship
- SOPT 28기 웹파트, 29기 서버파트, 30기 웹파트 && 운영팀 수료
- [Goorm :](https://goorm.co/) [Goorm DEVTH](https://devth.goorm.io/) 프론트엔드 개발 인턴십

---

# 우리가 오늘 해볼 것들

#### 1. 우리가 오늘 무엇을 할 것인지 이해하기 (feat. 웹개발이 뭐야 ?)
<br>

#### 2. React 프로젝트 초기 세팅하기

<br>

#### 3. React Component 만들어보기

<br>

#### 4. ChapGPT API 연결해보기

---
---
# 웹 프론트엔드 개발을 한다는 것은 ?


<div class="container">
        <div class="images">
            <div>
                <h2>전통적인 방식 (서버 사이드 렌더링 SSR)</h2>
                <p>php, jsp 등</p>
                <img src="/1-1.png" alt="traditional web">
            </div>
            <div>
                <h2>최근의 방식 (클라이언트 사이드 렌더링 CSR)</h2>
                <p>React, Vue 등</p>
                <img src="/1-2.png" alt="SPA">
            </div>
        </div>
</div>

<style>
.container {
    text-align: center; 
}

.images {
    margin-top: 50px;
    display: flex; 
    justify-content: center; 
    gap: 20px; 
}

.images img {
    height: 300px;
}
p {
    color: #514F4F;
    font-size: 1rem;
}
</style>
---
---
# 웹 프론트엔드 개발을 한다는 것은 ?

<img src="/1-3.jpg" alt="compare traditional and spa">
<p>MPA : MPA(Multiple Page Application)의 경우, 새로운 페이지로 갈 때마다, 서버에서 리소스(html, css, js 등)를 로드하고 실행 ➡️ 규모가 커지고 사용자와의 상호작용이 많아짐에 따라, 매번 서버에서 리소스를 로드하는 것은 과부하로 인한 속도 저하</p>
<p>SPA : SPA(Single Page Application)는 이를 해결하기 위한 방법으로, 첫 페이지에서 필요한 리소스 파일을 모두 로드하고, 페이지가 이동함에 따라 리소스를 실행하며 보여줌 !</p>

<style>
img {
    max-width: 60%;
}
</style>
---
---
# 오늘 해볼 것.

<img src="/2-1.png" alt="web, gpt architecture">
<p>React를 이용해 클라이언트 사이드를 구축하고, ChatGPT API 로 추가적으로 필요한 리소스를 가져온다 !</p>

<style>
img {
    max-width: 70%;
}
</style>
---
layout: image-right
image: '/4-1.png'
---
# Why React ?
- React는 사용자 인터페이스를 구축하기 위한 자바스크립트 UI 라이브러리

- React의 핵심은 컴포넌트 기반 개발 
- 기본적으로 Single Page Application 지원
    - webpack의 설정을 통해 서버사이드 렌더링 부분 지원 가능 
    - React 기반의 Next js 프레임워크를 통해 서버사이드 렌더링 구현 가능
- 효율적인 리렌더링 방식 (변화한 부분만 감지하여 렌더링 한다)
- 가장 많이 쓰여요 . . 



<style>
img {
    max-width: 70%;
}
</style>
---
layout: statement
---

# 다들 사전 세팅 해오셨나요 ? 

<br>

아래 명령어로 node가 제대로 설치되었는지 확인해주세요. <br>
코드를 호버하면 우측 상단의 버튼을 통해 코드를 복사할 수 있어요.

```shell
node —v
```
---

# React 초기 세팅 하기 

#### 1. vite를 통해 React 보일러 플레이트 받기
```shell
npm create vite
```
<img src='/5-1.png' alt="npm create vite">

<style>
img {
    max-width: 70%;
}
</style>
---
layout: image-right
image: '/6-2.png'
---
#### 2. 아래 명령어로 필요한 패키지를 다운로드 받고 실행시키기 
```shell
cd my-chatgpt && npm install && npm run dev
```
<img src='/6-1.png' alt="npm create vite">

<style>
img {
    max-width: 100%;
}
</style>
---

# React 파일의 구조 파악
<br>

`src > main.jsx`

![src > main.jsx 코드](/7-1.png)
<br>

* id값으로 root 를 가진 tag 안에 <App /> 컴포넌트를 넣을게
---

`public > index.html`

![public > index.htm 코드](/7-2.png)

* id="root"는 index.html 파일 하나에 들어가있어. 
* React는 SPA이기 때문에, html 파일이 index.html 하나 밖에 없고, 코드를 실행할 때 모든 코드가 이곳에 들어가서 실행될 것이야.
---

`src > App.jsx`
* App.jsx 코드가 모두 root에 들어가있으므로 컴포넌트들을 만들어서 App.jsx에 넣어야겠군 !
![src > App.jsx 코드](/7-3.png)

<style>
img {
    max-width: 37%;
}
</style>
---

# React Component 설계하기

![컴포넌트 설계](/8-1.png)

<style>
img {
    max-width: 80%;
}
</style>
---

# React Component 짜기 위해 필요한 라이브러리 추가 설치하기
<br>
```shell
npm install openai styled-components react-icons
```
<br>

- openai : openai api를 감싸고 있는 라이브러리와
- styled-components: 컴포넌트 내부에서 스타일링을 지원해주는 css-in-js 라이브러리
- react-icons : 우리는 디자이너가 없기 때문에 . 아이콘을 제공해주는 라이브러리도 함께 설치 ㅎ.ㅎ

[참고]  필요한 라이브러리는 https://www.npmjs.com/ 이곳에서 검색해서 찾아볼 수 있어요 

---

# 우리가 어떤 식으로 뷰와 로직을 가져갈 지 정리해보기 
<br>

![폴더구조](/8-3.png)

<style>
img {
    max-width: 70%;
}
</style>

---

# 우리가 어떤 식으로 뷰와 로직을 가져갈 지 정리해보기 
<br>

![폴더구조](/8-2.png)

<style>
img {
    max-width: 100%;
}
</style>

---

# 1. ChatBar.jsx 컴포넌트 만들어보기 

- `src/hooks/useInput.js` 
<br>

```js {all} {maxHeight:'350px'}
import { useState } from "react";

// useInput 훅 정의
function useInput(initialValue) {
  // 입력 값 상태 관리
  const [value, setValue] = useState(initialValue);

  // 입력 값 변경 이벤트 처리
  const handleChange = (e) => {
    setValue(e.target.value);
  };

  // 입력 필드 초기화
  const reset = () => {
    setValue(initialValue);
  };

  // 훅 사용 시 반환할 객체
  return {
    value,
    onChange: handleChange,
    reset,
  };
}

export default useInput;

```
---

- `src/components/ChatBar.jsx` 

<br>

```js {all} {maxHeight:'400px'}
import styled from "styled-components";
import useInput from "../hooks/useInput";
import { FaArrowUp } from "react-icons/fa";

// 이 컴포넌트는 최종적으로 입력된 값을 send해야 하므로 부모로부터 onSend 함수를 받게될 것
function ChatingBar({ onSend }) {
  // input으로 들어오는 값과, 값을 추적하는 onChage 프로퍼티와, 값을 초기화하는 reset 함수를 useInput 훅으로부터 받음
  const { value, onChange, reset } = useInput("");

  // 전송 버튼을 눌렀을 때, onSend 함수를 실행하고, reset 함수를 실행하여 인풋창을 초기화함
  const handleSubmit = (e) => {
    e.preventDefault();
    onSend(value);
    reset();
  };

  return (
    <StChatingBar onSubmit={handleSubmit}>
      {/* 채팅을 입력받을 창, useInput에서 받은 프로퍼티를 이용해 인풋값을 관리함 */}
      <StTextArea
        type="text"
        value={value}
        onChange={onChange}
        placeholder="Type a message..."
      />
      {/* 채팅 전송 버튼 */}
      <StButton type="submit">
        <FaArrowUp />
      </StButton>
    </StChatingBar>
  );
}

const StChatingBar = styled.form`
  width: 80%;
  height: 69px;
  border: 8px solid rgba(105, 105, 105, 0.5);
  box-shadow: 0px 10px 15px rgba(0, 0, 0, 0.25);
  border-radius: 40px;
  background: #414141;
  display: flex;
  align-items: center;
  margin-bottom: 20px;
`;

const StTextArea = styled.textarea`
  margin-left: 24px;
  width: 90%;
  height: 30px;
  background-color: transparent;
  border: none;
  outline: none;
  font-family: Noto Sans;
  font-style: normal;
  font-weight: normal;
  font-size: 1.25rem;
  line-height: 132.5%;

  display: flex;
  align-items: center;
  color: #f9f9f9;
  text-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  resize: none;

  &::placeholder {
    color: #f9f9f9;
  }
  :focus {
    outline: none;
  }
`;

const StButton = styled.button`
  background-color: #333;
  color: white;
  border: none;
  padding: 10px;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
  outline: none;

  display: flex;
  justify-content: center;
  align-items: center;

  &:hover {
    background-color: #555;
  }

  &:focus {
    outline: none;
  }

  &:active {
    background-color: #222;
  }
`;

export default ChatingBar;
```

---

- 만들어진 ChatBar.jsx를 App.jsx로 불러와서 한 번 동작을 확인해보자 !

- `src/App.jsx` 
```js {all} {maxHeight:'350px'}
import ChatBar from "./component/ChatBar";
import styled from "styled-components";
function App() {
  const onSend = (message) => {
    console.log(message);
  };

  return (
    <StMain>
      <ChatBar onSend={onSend} />
    </StMain>
  );
}

export default App;

const StMain = styled.main`
  width: 100vw;
  height: 100vh;

  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
`;

```

---

- 로컬에 `npm run dev` 실행시켜서 다시 접속해보자 ! 
- 아래와 같은 채팅 입력창이 뜨고, 입력 후 엔터를 치면 콘솔에 입력 값이 나온다 !

![실행화면](/9-1.png)

<style>
img {
    max-width: 80%;
}
</style>
---
layout: image-right
image: '/10-1.png'
---

# 2. chat gpt api 연결하기 (테스트)


- 다들 api키를 사전에 받아오셨나요 ? [키 발급 링크](https://platform.openai.com/account/api-keys)

- 그럼 아래 Docs를 보며 api 키가 잘 동작하는지 테스트 해보아요. ➡️ [독스 링크](https://platform.openai.com/docs/api-reference/authentication?lang=node.js)

- 먼저 터미널에서 api 키가 잘 동작하는지 테스트해보기 !

```shell
curl https://api.openai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
     "model": "gpt-3.5-turbo",
     "messages": [{"role": "user", "content": "Say this is a test!"}],
     "temperature": 0.7
   }'
```
---
layout: image-right
image: '/11-1.png'
---

# 2. chat gpt api 연결하기 (코드로)
<br>

- 먼저 여러분의 소중한 키를 .env파일에 넣어줘야 합니다
- pacakage.json이 있는 층위에 `.env` 파일을 만들어주세요. (추후 깃허브에 올리시는 경우 .gitignore에 .env파일을 넣어주셔야 합니다)
- 오가니제이션 ID 확인 링크 : https://platform.openai.com/account/organization

<br>

```
VITE_OPENAI_API_KEY=여러분의 키
VITE_OPENAI_ORGANIZATION=여러분의 오가니제이션 ID
```

---

# 2. chat gpt api 연결하기 (코드로)
<br>

- [DOCS](https://platform.openai.com/docs/api-reference/authentication?lang=node.js)를 바탕으로 연결 코드를 작성해줍니다 
- `src/lib/gpt.js`

```js {all} {maxHeight:'300px'}

import OpenAI from "openai";

export const configuration = {
  apiKey: import.meta.env.VITE_OPENAI_API_KEY,
  organization: import.meta.env.VITE_OPENAI_ORGANIZATION,
  dangerouslyAllowBrowser: true, // Browser에서 호출하기 위해선 이 옵션이 필요함
};

export const getGptResponse = async (text) => {
  const openai = new OpenAI(configuration);

  // 요청을 비동기적으로 받아오므로 async/await 문법을 사용
  const completion = await openai.chat.completions.create({
    messages: [{ role: "user", content: text }],
    model: "gpt-3.5-turbo",
  });
  console.log(completion); // ompletion.choices[0]?.message.content 내부에 답변이 들어있음

  return completion.choices[0]?.message.content;
};

```

---

- 한 번 해당 유틸 함수가 제대로 동작하는지 App.jsx로 가져와서 테스트 해보아요.

- `src/App.jsx`

```js {all} {maxHeight:'350px'}
import ChatBar from "./component/ChatBar";
import { getGptResponse } from "./lib/gpt";

import styled from "styled-components";
function App() {
  const onSend = async (message) => {
    console.log(message);

    // 입력받은 값으로 아까 생성한 getGptResponse 유틸함수를 호츌 후 결과 값을 찍어보기
    const result = await getGptResponse(message);
    console.log(result);
  };

  return (
    <StMain>
      <ChatBar onSend={onSend} />
    </StMain>
  );
}

export default App;

const StMain = styled.main`
  width: 100vw;
  height: 100vh;

  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
`;
```
---

- 실행화면
![실행화면](/12-1.png)
<style>
img {
    max-width: 100%;
}
</style>

---

# 3. 결과 화면 만들기

- 사실 이런 테스트 앱에선 결과를 그냥 컴포넌트로 바로 그려낼 수도 있지만, 주로 데이터를 받아올 때엔 로딩 중과 에러 처리를 해줘야 해요 
- 그래서 위 데이터 받아오는 로직을 useGptResponse 커스텀 훅으로 loading, success, error 상태를 반환하는 상태 관리 로직으로 연결해보려고 해요

---

- `src/hooks/useGptResponse.js` 
```js {all} {maxHeight:'400px'}
import { useReducer } from "react";
import { getGptResponse } from "../lib/gpt";

// 상태를 업데이트하는 리듀서 함수
const gptReducer = (state, action) => {
  switch (action.type) {
    case "REQUEST_START":
      return { ...state, loading: true, error: null, data: null };
    case "REQUEST_SUCCESS":
      return { ...state, loading: false, data: action.payload, error: null };
    case "REQUEST_FAILURE":
      return { ...state, loading: false, error: action.payload };
    default:
      return state;
  }
};

const initialState = {
  loading: false,
  error: null,
  data: null,
};

const useGptResponse = () => {
  const [state, dispatch] = useReducer(gptReducer, initialState);

  const getResponse = async (text) => {
    dispatch({ type: "REQUEST_START" });

    try {
      // API 요청
      const response = await getGptResponse(text);
      dispatch({ type: "REQUEST_SUCCESS", payload: response });
    } catch (error) {
      dispatch({ type: "REQUEST_FAILURE", payload: error });
    }
  };

  return { ...state, getResponse };
};

export default useGptResponse;
```
---

- 위 커스텀 훅을 이용해서 데이터를 가져오도록 `App.jsx` 를 수정할 거예요

- `src/App.jsx` 
```js {all} {maxHeight:'350px'}
import ChatBar from "./component/ChatBar";
import Result from "./component/Result";
import useGptResponse from "./hooks/useGptResponse";
import styled from "styled-components";
function App() {
  const { getResponse, ...result } = useGptResponse();
  const onSend = async (message) => {
    // getResponse를 통해 함수를 트리거
    getResponse(message);
  };

  return (
    <StMain>
      {/* 데이터 처리 상태를 담고 있는 result를 Result 컴포넌트에 넘길 것임 */}
      <Result result={result} />
      <ChatBar onSend={onSend} />
    </StMain>
  );
}

export default App;

const StMain = styled.main`
  width: 100vw;
  height: 100vh;

  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
`;

```

---

- 싱테 별로 결과를 그려는 Result.jsx를 짜봐요.
- `src/component/Result.jsx`
```js {all} {maxHeight:'350px'}
import styled from "styled-components";

const Result = ({ result }) => {
  const getContent = () => {
    if (result.loading) {
      return "loading ...";
    }
    if (result.error) {
      return result.error.message;
    }
    if (result.data) {
      return result.data;
    }
    return null;
  };

  return (
    <StResultSection>
      {getContent() && <StBubble>{getContent()}</StBubble>}
    </StResultSection>
  );
};
const StResultSection = styled.section`
  width: 80%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
`;

const StBubble = styled.div`
  background-color: #444;
  color: #fff;
  padding: 10px 15px;
  border-radius: 20px;
  max-width: 100%;
  word-wrap: break-word;
  margin: 30px 0;
  font-family: "Comic Sans MS", "Comic Neue", cursive;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);
  position: relative;
  &:after {
    content: "";
    position: absolute;
    border-width: 10px;
    border-style: solid;
    border-color: #444 transparent transparent transparent;
    bottom: -20px;
    left: 20px;
  }
`;

export default Result;

```
---

# 결과물!


![결과물](/13-1.gif)

<style>
img {
    max-width: 60%;
}
</style>

---
layout: image-right
image: '/14-1.png'
---

# 정말로 "나만의 챗지"를 만들고 싶다면

- chatGpt를 호출할 때 프롬프트를 본인의 입맛대로 바꾸어 보세요 . 

```js
export const getGptResponse = async (text) => {
  const openai = new OpenAI(configuration);
  const completion = await openai.chat.completions.create({
    messages: [
      {
        role: "system",
        content:
          "모든 대답은 yes or no로만 답해줘. 그 외에는 아무 말도 하지 마.",
      },
      { role: "user", content: text },
    ],
    model: "gpt-3.5-turbo",
  });

  return completion.choices[0]?.message.content;
};

```
---

# Contact 

- Linkedin : https://www.linkedin.com/in/park-nahee-100890218/
- Github : https://github.com/Nahee-Park
- Instagram : https://www.instagram.com/_devstone
---
layout: image
image: '/end.png'
---
