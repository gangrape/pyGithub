# pyGithub

A Python client for interacting with the GitHub API, providing features like fetching user information, searching repositories, and managing issues and pull requests.

## Features

- Fetch user data
- Search for repositories
- Retrieve issues and pull requests
- List branches
- Custom error handling

## Installation

To get started with this project, clone the repository and install the required dependencies:

```bash
git clone https://github.com/gangrape/pyGithub.git
cd pyGithub
pip install -r requirements.txt
```

## Example

```python
from pyGithub import Client

token = "YOUR_GITHUB_TOKEN" # Completely optional
client = Client(token)

user = client.get_user("octocat")
print(user)
```