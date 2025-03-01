import os
import requests
from dotenv import load_dotenv

load_dotenv()  # load values from env file
TOKEN = os.getenv("API_KEY")
HEADERS = {"Authorization": f"Bearer {TOKEN}",
           "Accept": "application/vnd.github+json"}

if not TOKEN:
    raise ValueError("API_KEY environment variable is not set. Check again README.md file for instructions.")

def get_profile_stats(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url, headers=HEADERS, timeout=5)
    if response.status_code != 200:
        raise ValueError(f"{response.status_code}: {response.text}")
    return response.json()

def get_user_stars(username):
    stars_url = f"https://api.github.com/users/{username}/starred"
    response_stars = requests.get(stars_url, headers=HEADERS, timeout=5)
    if response_stars.status_code != 200:
        raise ValueError(f"{response_stars.status_code}: {response_stars.text}")
    return len(response_stars.json())

def get_user_commits(username):
    commits_url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(commits_url, timeout=5)

    total_commits = 0
    for commit in response.json():
        repo_name = commit["name"]
        commits_url = f"https://api.github.com/repos/{username}/{repo_name}/commits"  # COUNT COMMITS
        commits_response = requests.get(commits_url, headers=HEADERS, timeout=5)
        if commits_response.status_code != 200:
            raise ValueError(f"{response.status_code}: {commits_response.text}")
        total_commits += len(commits_response.json())
    if response.status_code != 200:
        raise ValueError(f"{response.status_code}: {response.text}")
    return total_commits