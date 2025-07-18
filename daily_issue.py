import json
import random
import os
import requests

GITHUB_REPO = "3veryday/Growing"
GITHUB_TOKEN = os.environ["IMPLEMENTATION_GH_TOKEN"]

def get_random_problem():
    with open("problem_list.json", "r", encoding="utf-8") as f:
        problems = json.load(f)
    selected = random.choice(problems)
    return {
        "title": f"{selected['id']} - {selected['title']}",
        "url": f"https://www.acmicpc.net/problem/{selected['id']}"
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
