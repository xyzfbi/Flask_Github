import os
from src import github_api

RESUME_FILE_PATH = os.path.join('data', 'resume.txt')




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

    save_resume(data)
    return data

def save_resume(data):
    with open(RESUME_FILE_PATH, 'w') as file:
        for key, value in data.items():
            file.write(f"{key.capitalize()}: {value}\n")