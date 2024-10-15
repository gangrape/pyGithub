"""
MIT License

Copyright (c) 2024 Akami Yen

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

1. The above copyright notice and this permission notice shall be included in all
   copies or substantial portions of the Software.

2. THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
   SOFTWARE.
"""

from __future__ import annotations
from typing import Optional, Any

import requests
import json

from pyGithub.user import User
from pyGithub.repository import Repository
from pyGithub.ext.exceptions import (
    NotFound, 
    Unauthorized, 
    Forbidden, 
    BadRequest
)


class Route:
    """
    Represents an API route with method and path.

    """
    def __init__(self, method: str, path: str, token: Optional[str] = None) -> None:
        self.method = method
        self.path = path
        self.token = token


class Http:
    """
    Requests manager for the GitHub API.

    """
    def __init__(self) -> None:
        self.base: str = "https://api.github.com"


    def request(self, route: Route, **kwargs: Any) -> json:
        response = requests.request(
            method = route.method,
            url=f"{self.base}{route.path}",
            headers={
                "Accept": "application/vnd.github.v3+json",
                "Authorization": f"token {route.token}" if route.token else None
            },
            **kwargs
        )
        return self.handle(response)


    def fetch_user(self, username: str, token: str) -> User:
        user_data = self.request(
            Route(
                'GET', 
                f"/users/{username}", 
                token
            )
        )
        return User(user_data)



    def fetch_repo(self, owner: str, repo_name: str, token: str) -> Repository:
        repository_data = self.request(
            Route(
                method='GET',
                path=f"/repos/{owner}/{repo_name}",
                token=token
            )
        )
        return Repository(repository_data)


    def search_repositories(self, query: str, token: str) -> dict:
        return self.request(
            Route(
                method='GET',
                path=f"/search/repositories?q={query}",
                token=token
            )
        )


    def fetch_issues(self, owner: str, repo_name: str, token: str) -> list[dict]:
        return self.request(
            Route(
                method='GET',
                path=f"/repos/{owner}/{repo_name}/issues",
                token=token
            )
        )


    def fetch_pull_requests(self, owner: str, repo_name: str, token: str) -> list[dict]:
        return self.request(
            Route(
                method='GET',
                path=f"/repos/{owner}/{repo_name}/pulls",
                token=token
            )
        )


    def fetch_commits(self, owner: str, repo_name: str, token: str) -> list[dict]:
        return self.request(
            Route(
                method='GET',
                path=f"/repos/{owner}/{repo_name}/commits",
                token=token
            )
        )


    def fetch_branches(self, owner: str, repo_name: str, token: str) -> list[dict]:
        return self.request(
            Route(
                method='GET',
                path=f"/repos/{owner}/{repo_name}/branches",
                token=token
            )
        )


    def fetch_releases(self, owner: str, repo_name: str, token: str) -> list[dict]:
        return self.request(
            Route(
                method='GET',
                path=f"/repos/{owner}/{repo_name}/releases",
                token=token
            )
        )


    def fetch_contributors(self, owner: str, repo_name: str, token: str) -> list[dict]:
        return self.request(
            Route(
                method='GET',
                path=f"/repos/{owner}/{repo_name}/contributors",
                token=token
            )
        )


    def fetch_issue(self, owner: str, repo_name: str, issue_number: int, token: str) -> dict:
        return self.request(
            Route(
                method='GET',
                path=f"/repos/{owner}/{repo_name}/issues/{issue_number}",
                token=token
            )
        )


    def create_issue(
        self,
        token: str, 
        owner: str, 
        repo_name: str, 
        title: str, 
        body: Optional[str] = None
    ) -> dict:
        return self.request(
            Route(
                method='POST',
                path=f"/repos/{owner}/{repo_name}/issues",
                token=token
            ),
            json={"title": title, "body": body}
        )


    def fetch_milestones(self, owner: str, repo_name: str, token: str) -> list[dict]:
        return self.request(
            Route(
                method='GET',
                path=f"/repos/{owner}/{repo_name}/milestones",
                token=token
            )
        )


    def create_milestone(
        self,
        token: str,
        owner: str, 
        repo_name: str,
        title: str,
        description: Optional[str] = None, 
        due_on: Optional[str] = None
    ) -> dict:
        return self.request(
            Route(
                method='POST',
                path=f"/repos/{owner}/{repo_name}/milestones",
                token=token
            ),
            json={"title": title, "description": description, "due_on": due_on}
        )


    def fetch_labels(self, owner: str, repo_name: str, token: str) -> list[dict]:
        return self.request(
            Route(
                method='GET',
                path=f"/repos/{owner}/{repo_name}/labels",
                token=token
            )
        )


    def create_label(self, owner: str, repo_name: str, name: str, color: str, token: str) -> dict:
        return self.request(
            Route(
                method='POST',
                path=f"/repos/{owner}/{repo_name}/labels",
                token=token
            ),
            json={"name": name, "color": color}
        )


    def fetch_events(self, owner: str, repo_name: str, token: str) -> list[dict]:
        return self.request(
            Route(
                method='GET',
                path=f"/repos/{owner}/{repo_name}/events",
                token=token
            )
        )


    def fetch_commit(self, owner: str, repo_name: str, commit_sha: str, token: str) -> dict:
        return self.request(
            Route(
                method='GET',
                path=f"/repos/{owner}/{repo_name}/commits/{commit_sha}",
                token=token
            )
        )


    def fetch_release(self, owner: str, repo_name: str, release_id: int, token: str) -> dict:
        return self.request(
            Route(
                method='GET',
                path=f"/repos/{owner}/{repo_name}/releases/{release_id}",
                token=token
            )
        )


    def create_release(
        self,
        token: str, 
        owner: str, 
        repo_name: str, 
        tag_name: str, 
        name: Optional[str] = None,
        body: Optional[str] = None,
        draft: bool = False,
        prerelease: bool = False
    ) -> dict:
        return self.request(
            Route(
                method='POST',
                path=f"/repos/{owner}/{repo_name}/releases",
                token=token
            ),
            json={
                "tag_name": tag_name, 
                "name": name, 
                "body": body,
                "draft": draft,
                "prerelease": prerelease
            }
        )


    def fetch_forks(self, owner: str, repo_name: str, token: str) -> list[dict]:
        return self.request(
            Route(
                method='GET',
                path=f"/repos/{owner}/{repo_name}/forks",
                token=token
            )
        )


    def fetch_stargazers(self, owner: str, repo_name: str, token: str) -> list[dict]:
        return self.request(
            Route(
                method='GET',
                path=f"/repos/{owner}/{repo_name}/stargazers",
                token=token
            )
        )


    def fetch_watched_repos(self, token: str) -> list[dict]:
        return self.request(
            Route(
                method='GET',
                path="/user/subscriptions",
                token=token
            )
        )


    def fetch_repositories_for_user(self, username: str, token: str) -> list[dict]:
        return self.request(
            Route(
                method='GET',
                path=f"/users/{username}/repos",
                token=token
            )
        )


    def fetch_notifications(self, token: str) -> list[dict]:
        return self.request(
            Route(
                method='GET',
                path="/notifications",
                token=token
            )
        )


    def mark_notifications_as_read(self, token: str) -> dict:
        return self.request(
            Route(
                method='PUT',
                path="/notifications",
                token=token
            )
        )


    def fetch_repo_topics(self, owner: str, repo_name: str, token: str) -> dict:
        return self.request(
            Route(
                method='GET',
                path=f"/repos/{owner}/{repo_name}/topics",
                token=token
            )
        )


    def replace_repo_topics(self, owner: str, repo_name: str, names: list[str], token: str) -> dict:
        return self.request(
            Route(
                method='PUT',
                path=f"/repos/{owner}/{repo_name}/topics",
                token=token
            ),
            json={"names": names}
        )


    def fetch_traffic_views(self, owner: str, repo_name: str, token: str) -> dict:
        return self.request(
            Route(
                method='GET',
                path=f"/repos/{owner}/{repo_name}/traffic/views",
                token=token
            )
        )


    def fetch_traffic_clones(self, owner: str, repo_name: str, token: str) -> dict:
        return self.request(
            Route(
                method='GET',
                path=f"/repos/{owner}/{repo_name}/traffic/clones",
                token=token
            )
        )


    def handle(self, response: requests.Response) -> json:
        if response.status_code == 404:
            raise NotFound(
                f"Endpoint '{response.url}' not found."
            )
        elif response.status_code == 401:
            raise Unauthorized(
                "Invalid or missing authentication token."
            )
        elif response.status_code == 403:
            raise Forbidden(
                "You do not have permission to access this resource."
            )
        elif response.status_code == 400:
            raise BadRequest(
                "The request was malformed."
            )
        return response.json()