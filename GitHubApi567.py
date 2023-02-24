import requests
import json

def get_user_repos_commits():
    user_id = input('Enter the user id')
    url = f"https://api.github.com/users/{user_id}/repos"
    response = requests.get(url)
    data = json.loads(response.text)
    
    # iterate over the repositories and get the number of commits for each
    no_of_commits = []
    for repo in data:
        repo_name = repo["name"]
        commits_url = repo["commits_url"].replace("{/sha}", "")
        commits_response = requests.get(commits_url)
        commits = json.loads(commits_response.text)
        num_commits = len(commits)
        no_of_commits.append((repo_name, num_commits))

    for i in no_of_commits:
        print(f'Repos : {i[0]} Number of commits : {i[1]}')

get_user_repos_commits()