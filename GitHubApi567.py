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
# test function to mock out service calls
def test_get_user_repos_commits():
    user_id = "example_user"
    repos_url = f"https://api.github.com/users/{user_id}/repos"
    commits_url = "https://api.github.com/repos/example_user/example_repo/commits"

    # create a fake response for requests.get
    fake_response = [{"name": "example_repo", "commits_url": commits_url}]
    fake_commits_response = [{"sha": "123abc"}, {"sha": "456def"}]

    # mock the requests.get method to return the fake responses
    requests_get_mock = Mock(side_effect=[
        Mock(text=json.dumps(fake_response)),
        Mock(text=json.dumps(fake_commits_response)),
    ])
    with patch("requests.get", requests_get_mock):
        # call the function to be tested
        get_user_repos_commits(user_id)
        
        # assert that requests.get was called with the correct URLs
        requests_get_mock.assert_any_call(repos_url)
        requests_get_mock.assert_any_call(commits_url)

# run the test function
test_get_user_repos_commits()