import requests

base_url = "https://api.github.com"

def create_repo(access_token, repo_name, repo_descr=None):
    url = f"{base_url}/user/repos"
   
    headers = {
        "Authorization": f"token {access_token}",
    }

    # create json data to send using the post request
    data = {
        "name": repo_name,
        "description": repo_descr,
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 201:
        repo_data = response.json()
        return repo_data
    else:
        return None


access_token = "YOUR ACCESS TOKEN"
repo_name = "apify_testing"
repo_descr = "New repo created using the Python GitHub API."

new_repo = create_repo(access_token, repo_name, repo_descr)

if new_repo:
    print(f"New public repo created successfully!")
else:
    print("Failed to create a new repo.")