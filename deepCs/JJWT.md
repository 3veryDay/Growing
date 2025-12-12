# JJWT

정의: 자바(Java) 환경에서 JWT(JSON Web Token)를 생성하고, 파싱(해석)하고, 검증하기 위해 가장 널리 사용되는 오픈소스 라이브러리이다.

특징: 복잡한 암호화(HMAC, RSA) 로직이나 JSON 직렬화/역직렬화 과정을 추상화하여, 개발자가 메서드 체이닝(Method Chaining) 방식으로 쉽게 토큰을 다룰 수 있게 해주는 **도구(Tool)**이다.

독립성: Spring Framework에 종속되지 않은 순수 자바 라이브러리이다.


## 핵심 역할

#### A. 토큰 생성(Builder)

`Jwts.builder()`

역할 :
1. Claims 설정 : 토큰에 담을 정보(subject, expiration, ...)를 JSON형태로 주입
2. 서명 : `signsWith(key, algorithm)`을 통해서 서명 생성
3. 압축 : `.compact()` 통해서 String 형태로 반환

#### B. 토큰 검증기(Parser)

`Jwts.parser()`

역할
1. 키 설정 : `verifyWith(key)` 암호화할 때 썼던 비밀키와 같은 키인지 확인함.
2.파싱(Parse): `parseSignedClaims(token)`을 통해 문자열을 다시 데이터 객체(Claims)로 변환한다.

3. 예외 발생: 만약 토큰이 조작되었거나(SignatureException), 유효기간이 지났다면(ExpiredJwtException) 즉시 예외를 던진다.


## 추가
JJWT 라이브러리는 비대칭키(Asymmetric Key) 방식도 지원한다.

- 알고리즘: RS256 (RSA), ES256 (ECDSA) 등.

특징: 키가 두 개(쌍) 있다.

Private Key (개인키): 나만 가지고 있음. **서명(Sign)**할 때 씀.

Public Key (공개키): 남들에게 뿌림. **검증(Verify)**할 때 씀.

장점: 검증하는 서버(Resource Server)가 여러 대여도 비밀키가 털릴 걱정 없이 공개키만 던져주면 되니까 보안성이 더 높다. (구글 로그인 같은 OAuth2가 이 방식을 쓴다.)