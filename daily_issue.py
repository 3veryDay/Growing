import requests
import random
import os

GITHUB_REPO = "3veryday/Growing"
GITHUB_TOKEN = os.environ["IMPLEMENTATION_GH_TOKEN"]

# ✅ 수정된 URL (level 쿼리 수정됨)
API_URL = "https://solved.ac/api/v3/search/problem?query=tag:구현%20level:9..10%20level:15..16&sort=random"

def get_random_problem():
    res = requests.get(API_URL)
    data = res.json()
    items = data.get("items", [])
    
    if not items:
        raise ValueError("문제 리스트가 비어 있습니다.")

    problem = items[0]
    return {
        "title": f"{problem['problemId']} - {problem['titleKo']}",
        "url": f"https://www.acmicpc.net/problem/{problem['problemId']}"
    }

def create_github_issue(title, ur
