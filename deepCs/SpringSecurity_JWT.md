## Spring Security와 JWT를 활용한 토큰 기반 인증 흐름

Access Token과 Refresh Token은 Spring Security 환경에서 JWT를 활용해 사용자 인증(Authentication) 및 **인가(Authorization)**를 구현할 때 사용하는 핵심 수단이다.

1. 초기 인증 및 토큰 발급
사용자가 로그인을 시도하면, 정보는 Spring Security의 인증 필터로 전달되어 검증 과정을 거친다. 인증에 성공하면 사용자의 정보를 담은 **인증 객체(Authentication)**가 생성되어 Security Context에 저장된다. 서버는 이 인증 객체의 정보를 기반으로 Access Token과 Refresh Token을 생성하고, 이미 수립된 HTTPS 암호화 터널을 통해 안전하게 클라이언트에게 전달한다.

2. 요청 및 인가 과정
이후 사용자는 API 요청을 보낼 때마다 HTTP 헤더(Header)에 Access Token을 담아 보낸다. 요청을 받은 Spring Security는 Filter Chain 앞단에서 토큰을 가로채 유효성을 검증하고, 토큰 내의 정보를 바탕으로 다시 임시 인증 객체를 만들어 Security Context에 주입함으로써 해당 요청에 대한 **권한(인가)**을 확인한다.

3. 토큰 만료와 재발급 (Refresh Flow)
Access Token의 유효 기간(TTL)이 만료된 상태로 요청이 들어오면, 서버는 401 Unauthorized 에러와 함께 토큰 재발급이 필요하다는 응답을 보낸다. 이때 클라이언트가 가지고 있던 Refresh Token을 서버로 보내면, 서버는 다음 단계로 검증을 수행한다.

DB(또는 Redis)에 저장된 해당 사용자의 Refresh Token과 클라이언트가 보낸 토큰이 일치하는지 확인한다.

유효하다면 사용자의 정보를 기반으로 새로운 Access Token을 생성하여 발급한다.

4. 클라이언트 최적화 (Silent Refresh)
사용자 경험(UX)을 저해하지 않기 위해, 클라이언트(브라우저) 측에서는 이 과정을 자동화한다. 보통 Axios Interceptor 등을 활용해 401 응답을 감지하거나, 쿠키/로컬 스토리지에 저장된 만료 시간(TTL)을 미리 체크한다. 이를 통해 사용자가 로그아웃되거나 멈추는 느낌 없이, 백그라운드에서 자동으로 Refresh Token을 전송하고 새로운 Access Token을 받아오는 'Silent Refresh' 전략을 구현한다.
