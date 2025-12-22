# [정리] HTTP 쿠키 (Cookie)와 Spring에서의 활용

## 1. 쿠키의 개요 및 등장 배경
* **HTTP의 Stateless 보완:** HTTP는 기본적으로 상태를 유지하지 않는(Stateless) 프로토콜입니다. 서버는 클라이언트의 이전 요청을 기억하지 못하기 때문에, 클라이언트 측에서 상태 정보를 유지하도록 돕는 쿠키(Cookie)가 등장했습니다.
* **Client-side 관리:** 데이터를 클라이언트에 저장하므로 서버의 부하를 줄이면서 가볍게 상태를 유지할 수 있습니다.

---

## 2. 쿠키의 분류

### ① 세션 쿠키 (Session Cookie)
* **생명 주기:** 메모리에만 저장되며, 브라우저가 종료되면 자동으로 삭제됩니다.
* **특징:** `Max-Age`나 `Expires` 옵션을 명시하지 않았을 때 기본으로 생성됩니다. (과거 RFC 2965의 `Discard` 파라미터와 유사한 동작)
* **용도:** 장바구니, 임시 로그인 상태 유지 등 일시적인 데이터 저장.

### ② 영속 쿠키 (Persistent Cookie)
* **생명 주기:** 파일 시스템(디스크)에 저장되며, 브라우저를 껐다 켜도 지정된 만료 시간까지 유지됩니다.
* **특징:** 브라우저 실행 시 디스크에서 읽어 메모리(RAM)로 로드됩니다.
* **용도:** "아이디 저장", "자동 로그인", 사용자 취향 분석용 "3rd Party 쿠키".

---

## 3. 쿠키의 동작 원리 및 관리 (Cookie Jar)
1.  **발급:** 서버가 응답 헤더에 `Set-Cookie`를 실어 보냅니다.
2.  **저장:** 브라우저는 도메인/경로별로 쿠키를 보관하는 **Cookie Jar(쿠키 저장소)**에 이를 보관합니다.
3.  **전송:** 이후 동일한 도메인/경로로 요청을 보낼 때, 브라우저는 해당되는 쿠키들을 `Cookie` 요청 헤더에 자동으로 담아 보냅니다.

> **설계 주의점:** 모든 요청마다 쿠키가 포함되므로, 쿠키 양이 많아지면 네트워크 오버헤드가 발생합니다. 따라서 `Domain`과 `Path` 설정을 통해 필요한 곳으로만 전송되도록 정밀하게 설계해야 합니다.

---

## 4. 쿠키 버전 및 주요 기능 (v0 vs v1)
* **Version 0 (Netscape):** 가장 널리 쓰이는 기본 사양입니다.
* **Version 1 (RFC 2109/2965):** TTL을 초 단위(`Max-Age`)로 관리하고, 포트(Port) 제한 등 보안이 강화되었습니다. 
* **강제 삭제 기능 (Force Delete):** 서버가 클라이언트의 쿠키를 지우고 싶을 때 사용합니다. 
    * **방법:** 동일한 이름의 쿠키를 만들고 `Max-Age=0` 또는 만료 시간을 과거(예: 1970년)로 설정하여 다시 보냅니다.
    * **용도:** 로그아웃 처리, 기존 유효하지 않은 정보 초기화.

---

## 5. 쿠키 상세 옵션 (Attributes)

### ① 시간 관리 (Lifetime)
* **Expires:** 절대적인 유효 날짜 지정.
* **Max-Age:** 현재 시점부터 생존할 시간을 **초(Seconds)** 단위로 지정. (더 우선순위가 높음)

### ② 보안 관리 (Security)
* **HttpOnly:** 자바스크립트(`document.cookie`)로 쿠키 접근을 차단합니다. **XSS 공격을 방지**하는 핵심 옵션입니다.
* **Secure:** HTTPS 프로토콜을 사용하는 암호화된 통신에서만 쿠키를 전송합니다.

### ③ 접근 범위 (Scope)
* **Domain:** 쿠키를 전송할 도메인 범위를 지정합니다.
* **Path:** 특정 경로 이하의 요청에만 쿠키를 전송합니다.

### ④ CSRF 방지 (SameSite)
* **Strict:** 동일 도메인 요청에서만 쿠키 전송.
* **Lax:** 링크 클릭 등을 통한 외부 사이트 이동 시 GET 요청에 한해 쿠키 전송 (최신 브라우저의 기본값).
* **None:** 모든 교차 사이트 요청에 전송 (반드시 `Secure` 옵션이 동반되어야 함).

---

## 6. Spring에서의 쿠키 관리

### ① 전역 설정 (`application.yml`)
세션 쿠키의 보안 옵션을 프로젝트 전체에 적용할 때 사용합니다.
```yaml
server:
  servlet:
    session:
      cookie:
        http-only: true
        secure: true
        same-site: lax
```
### ② 최신 방식 (ResponseCookie API)
Spring 5부터 제공되는 객체로, SameSite 등 최신 옵션 설정을 지원합니다.

```java
ResponseCookie cookie = ResponseCookie.from("user_id", "toby123")
    .httpOnly(true)
    .secure(true)
    .path("/")
    .maxAge(3600)
    .sameSite("Lax")
    .build();

response.addHeader(HttpHeaders.SET_COOKIE, cookie.toString());
```

### ③ 서블릿 기초 방식 (HttpServletResponse)
토비책에서 servlet공부하면서 보게 될 내용
```java
Cookie cookie = new Cookie("user_id", "toby123");
cookie.setHttpOnly(true);
cookie.setSecure(true);
cookie.setMaxAge(60 * 60); // 1시간
cookie.setPath("/");

response.addCookie(cookie);
```
