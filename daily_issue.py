import requests
from bs4 import BeautifulSoup
import random
import os

GITHUB_REPO = "3veryday/Growing"  # ⚠️ 본인 리포 경로로 수정
GITHUB_TOKEN = os.environ["Implementation_GH_TOKEN"]

SEARCH_URL = "https://solved.ac/search?query=tag:구현+level:9..10+level:15..16"

def get_random_problem():
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(SEARCH_URL, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    
    links = soup.select("a.css-1ewt4k2")  # 문제 링크가 걸린 <a> 태그
    problems = [
        {
            "title": link.text.strip(),
            "url": "https://www.acmicpc.net" + link.get("href")
        }
        for link in links if "/problem/" in link.get("href")
    ]
    return random.choice(problems)

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
