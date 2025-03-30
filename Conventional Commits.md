좋은 질문이야! ✨  
**Conventional Commits**는 커밋 메시지를 일정한 형식으로 작성하자는 규칙이야. 이 규칙을 따르면 협업, 자동 릴리즈, 변경 로그 관리 등에 정말 유용해. GitHub, GitLab, CI/CD 도구들이 이걸 인식해서 자동화 작업에 써먹기도 해!

---

### 📌 기본 구조

```
<타입>(선택적 범위): <변경 요약>
```

예:
```
feat(login): add remember me checkbox
fix(auth): handle null token on logout
```

---

### 🔧 주요 타입(type) 정리 + 예시

| 타입 | 의미 | 예시 |
|------|------|------|
| `feat` | 새로운 기능 추가 | `feat(chat): implement message reactions` |
| `fix` | 버그 수정 | `fix(user): prevent crash on empty username` |
| `docs` | 문서 관련 변경 | `docs(readme): update installation guide` |
| `style` | 포맷팅, 세미콜론 등 코드 변경 없음 | `style: format with prettier` |
| `refactor` | 리팩토링 (기능 변화 X) | `refactor(api): simplify response parsing` |
| `perf` | 성능 개선 | `perf(image): reduce image loading time` |
| `test` | 테스트 추가/수정 | `test(api): add test for error handler` |
| `chore` | 빌드 설정, 패키지 관리 등 기타 잡일 | `chore: bump version to 1.2.0` |
| `ci` | CI 관련 설정 변경 | `ci: add GitHub Actions for testing` |
| `build` | 빌드 관련 설정 변경 | `build: update webpack config` |

---

### 🎯 상황별 Pull Request Title 예시

#### ✅ 기능 추가
- `feat(post): implement post editing`
- `feat(search): add debounced search input`

#### 🐛 버그 수정
- `fix(navbar): fix mobile menu toggle bug`
- `fix(form): resolve validation error on submit`

#### 🧼 코드 리팩토링
- `refactor(user): clean up profile data handling`
- `refactor(store): split reducers into modules`

#### 📄 문서 작업
- `docs: add API usage examples`
- `docs(readme): correct typo in setup section`

#### 🎨 스타일 변경
- `style(button): adjust padding and font size`
- `style: apply prettier formatting`

#### 🔍 테스트 추가
- `test(login): add tests for token handling`
- `test(profile): mock API in unit tests`

#### 🛠 기타 작업
- `chore: update dependencies`
- `chore: remove unused files`

---

필요하다면 너의 프로젝트 상황에 맞게 예시를 더 구체적으로 맞춰줄 수도 있어!  
혹시 지금 작업 중인 브랜치가 어떤 내용인지 알려줄래? PR 제목도 함께 맞춰줄게. 😎
