import requests
from config import GITLAB_BASE_URL, PRIVATE_TOKEN, PROJECT_ID

headers = {
    "PRIVATE-TOKEN": PRIVATE_TOKEN
}

def get_commits(since=None, until=None, per_page=20):
    url = f"{GITLAB_BASE_URL}/projects/{PROJECT_ID}/repository/commits"
    params = {
        "per_page": per_page
    }
    if since:
        params["since"] = since
    if until:
        params["until"] = until

    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def get_commit_diff(commit_sha):
    url = f"{GITLAB_BASE_URL}/projects/{PROJECT_ID}/repository/commits/{commit_sha}/diff"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()
