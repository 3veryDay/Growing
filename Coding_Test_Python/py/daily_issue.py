import json
import random
import os
import requests
from datetime import date

GITHUB_REPO = "3veryday/Growing"
GITHUB_TOKEN = os.environ["IMPLEMENTATION_GH_TOKEN"]

def get_random_problem():
    with open("problem_list.json", "r", encoding="utf-8") as f:
        problems = json.load(f)
    selected = random.choice(problems)
    return {
        "id": selected['id'],
        "title": selected['title'],
        "url": f"https://www.acmicpc.net/problem/{selected['id']}"
    }

def create_github_issue(problem):
    api_url = f"https://api.github.com/repos/{GITHUB_REPO}/issues"
    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }

    today = date.today().strftime("%Y-%m-%d")

    body = f"""### 🔢 문제 링크
[{problem['id']}. {problem['title']}]({problem['url']})

---

### 📝 할 일
- [ ] 문제 이해하기  
- [ ] 예제 입력/출력 확인  
- [ ] 코드 작성 및 제출  
- [ ] 리팩토링 & 주석 추가  

---

### 💡 풀이 아이디어
> 여기에 핵심 아이디어를 적어주세요.

---

📅 **생성일:** {today}
"""

    data = {
        "title": f"[백준] {problem['id']}. {problem['title']}",
        "body": body,
        "labels": ["백준", "구현"],
        "assignees": ["3veryday"]  # 👉 본인 GitHub ID로 변경 가능
    }

    response = requests.post(api_url, headers=headers, json=data)
    if response.status_code == 201:
        print(f"✅ Issue Created: {problem['id']} - {problem['title']}")
    else:
        print(f"❌ Error: {response.status_code}, {response.text}")

if __name__ == "__main__":
    problem = get_random_problem()
    create_github_issue(problem)
