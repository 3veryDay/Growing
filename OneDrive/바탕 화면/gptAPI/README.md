# gdsc-open-tech-seminar
GDSC Ewha 5th open tech seminar web : Creating Your Own ChatGPT

# presentation 

[이 링크](https://gdsc-open-tech-seminar.vercel.app/1)를 통해 발표 자료를 보실 수 있습니다!

# example
실습코드 실행시키는 방법

## 1. 아래 커맨드를 통해 실습코드를 클론 받고 패키지를 설치해줍니다.
```
git clone https://github.com/Nahee-Park/gdsc-open-tech-seminar
cd my-chatgpt && npm install 
```

## 2. Chat GPT API Key와 Organization Id를 받고 .env 파일을 생성해줍니다. 
> 꼭 my-chapgpt 프로젝트 최상단에 생성해주어야 합니다
- [API Key 발급받기](https://platform.openai.com/api-keys)
- [Organization Id 확인하기](https://platform.openai.com/account/organization)

- `my-chatgpt/.env`
```
VITE_OPENAI_API_KEY=
VITE_OPENAI_ORGANIZATION=
```

## 3. 실행시켜 줍니다. 
> 꼭 my-chatgpt 프로젝트 내부에서 해당 명령어를 실행시켜야 합니다
```
npm run dev 
```
