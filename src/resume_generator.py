import os
from src import github_api
from jinja2 import Template
from flask import render_template

RESUME_FILE_PATH = os.path.join('data', 'resume.txt')
INDEX_FILE_PATH = os.path.join('data', 'index.html')
TEMPLATE_FILE_PATH = os.path.join('templates', 'index.html')

def generate_resume(username):
    profile_stats = github_api.get_profile_stats(username)
    stars = github_api.get_user_stars(username)
    commits = github_api.get_user_commits(username)

    data = {
        "name": profile_stats.get("name", "None"),
        "email": profile_stats.get("email", "None"),
        "login": profile_stats.get("login", "None"),
        "location": profile_stats.get("location", "None"),
        "bio": profile_stats.get("bio", "None"),
        "stars": stars,
        "commits": commits,
        "repos": profile_stats.get('public_repos', 0),
        "followers": profile_stats.get('followers', 0),
        "following": profile_stats.get('following', 0)
    }

    rendered_resume = render_template('index.html', data=data)

    with open(INDEX_FILE_PATH, "w", encoding="utf-8") as resume_file:
        resume_file.write(rendered_resume)

    save_resume(data)
    return data

def save_resume(data):
    with open(RESUME_FILE_PATH, 'w') as file:
        for key, value in data.items():
            file.write(f"{key.capitalize()}: {value}\n")