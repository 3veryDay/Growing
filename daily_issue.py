import requests
import random
import os

GITHUB_REPO = "3veryday/Growing"
GITHUB_TOKEN = os.environ["IMPLEMENTATION_GH_TOKEN"]

# level 9~10 (실버2,1), level 15~16 (골드5,4) 따로
API_URLS = [
    "https://solved.ac/api/v3/search/problem?query=tag:구현%20level:9..10&sort=random",
    "https://solved.ac/api/v3/search/problem?query=tag:구현%20level:15..16&sort=random"
]

def get_random_problem():
    problems = []

    for url in API_URLS:
        res = requests.get(url)
        data = res.json()
        items = data.get("items", [])
        problems.extend(items)

    if not problems:
        raise ValueError("문제 리스트가 비어 있습니다.")

    problem = random.choice(problems)
    return {
        "title": f"{problem['problemId']} - {problem['titleKo']}",
        "url": f"https://www.acmicpc.net/problem/{problem['problemId']}"
    }

def create_github_issue(title, url):
    api_url = f"https://api.github.com/repos/{GITHUB_REPO}/issues"
    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }
    data = {
        "title": f"[백준 구현] {title}",
        "body": f"문제 링크: {url}"
    }
    response = requests.post(api_url, headers=headers, json=data)
    print("📌 Issue Created:", response.status_code)

if __name__ == "__main__":
    problem = get_random_problem()
    create_github_issue(problem["title"], problem["url"])
