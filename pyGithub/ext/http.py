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


class Http:
    """
    Requests manager for the GitHub API.
    This class handles the API requests and responses for various GitHub functionalities.
    """
    def __init__(self) -> None:
        """
        Initializes the Http instance, setting the base URL for the GitHub API.
        """
        self.base: str = "https://api.github.com"


    def request(
        self,
        method: str,
        endpoint: str,
        token: Optional[str] = None,
        **kwargs: Any
    ) -> json:
        """
        Makes an API request to the GitHub API.

        Args:
            method (str): The HTTP method to use (GET, POST, etc.).
            endpoint (str): The specific API endpoint to call.
            token (Optional[str]): An optional personal access token for authentication.
            **kwargs: Additional parameters to pass to the request.

        Returns:
            json: The response data in JSON format.

        Raises:
            NotFound: If the endpoint does not exist (404).
            Unauthorized: If authentication fails (401).
            Forbidden: If access is denied (403).
            BadRequest: If the request is malformed (400).
        """
        r = requests.request(
            method=method,
            url=f"{self.base}/{endpoint}",
            headers={
                "Accept": "application/vnd.github.v3+json",
                "Authorization": f"token {token}" if token else None
            },
            **kwargs
        )
        if r.status_code == 404:
            raise NotFound(
                f"Endpoint '{endpoint}' not found."
            )
        elif r.status_code == 401:
            raise Unauthorized(
                "Invalid or missing authentication token."
            )
        elif r.status_code == 403:
            raise Forbidden(
                "You do not have permission to access this resource."
            )
        elif r.status_code == 400:
            raise BadRequest(
                "The request was malformed."
            )

        return r.json()


    def fetch_user(
        self, 
        username: str,
        token: str
    ) -> User:
        """
        Fetches user data from GitHub.

        Args:
            username (str): The username of the GitHub user to fetch.
            token (str): The personal access token for authentication.

        Returns:
            User: A User object containing the user's data.
        """
        user_data = self.request(
            method="GET",
            endpoint=f"users/{username}",
            token=token
        )
        return User(user_data)


    def fetch_repo(
        self, 
        owner: str, 
        repo_name: str,
        token: str
    ) -> Repository:
        """
        Fetches repository data from GitHub.

        Args:
            owner (str): The username of the repository owner.
            repo_name (str): The name of the repository.
            token (str): The personal access token for authentication.

        Returns:
            Repository: A Repository object containing the repository's data.
        """
        repository_data = self.request(
            method="GET",
            endpoint=f"repos/{owner}/{repo_name}",
            token=token
        )
        return Repository(repository_data)


    def search_repositories(
        self, 
        query: str,
        token: str
    ) -> dict:
        """
        Searches for repositories based on a query.

        Args:
            query (str): The search query string.
            token (str): The personal access token for authentication.

        Returns:
            dict: A dictionary containing search results.
        """
        return self.request(
            method="GET",
            endpoint=f"search/repositories?q={query}",
            token=token
        )


    def fetch_issues(
        self, 
        owner: str, 
        repo_name: str,
        token: str
    ) -> list[dict]:
        """
        Fetches issues for a repository.

        Args:
            owner (str): The username of the repository owner.
            repo_name (str): The name of the repository.
            token (str): The personal access token for authentication.

        Returns:
            list[dict]: A list of dictionaries representing the issues.
        """
        return self.request(
            method="GET",
            endpoint=f"repos/{owner}/{repo_name}/issues",
            token=token
        )


    def fetch_pull_requests(
        self, 
        owner: str, 
        repo_name: str,
        token: str
    ) -> list[dict]:
        """
        Fetches pull requests for a repository.

        Args:
            owner (str): The username of the repository owner.
            repo_name (str): The name of the repository.
            token (str): The personal access token for authentication.

        Returns:
            list[dict]: A list of dictionaries representing the pull requests.
        """
        return self.request(
            method="GET",
            endpoint=f"repos/{owner}/{repo_name}/pulls",
            token=token
        )


    def fetch_commits(
        self, 
        owner: str, 
        repo_name: str,
        token: str
    ) -> list[dict]:
        """
        Fetches commits for a repository.

        Args:
            owner (str): The username of the repository owner.
            repo_name (str): The name of the repository.
            token (str): The personal access token for authentication.

        Returns:
            list[dict]: A list of dictionaries representing the commits.
        """
        return self.request(
            method="GET",
            endpoint=f"repos/{owner}/{repo_name}/commits",
            token=token
        )


    def fetch_branches(
        self, 
        owner: str, 
        repo_name: str,
        token: str
    ) -> list[dict]:
        """
        Fetches branches for a repository.

        Args:
            owner (str): The username of the repository owner.
            repo_name (str): The name of the repository.
            token (str): The personal access token for authentication.

        Returns:
            list[dict]: A list of dictionaries representing the branches.
        """
        return self.request(
            method="GET",
            endpoint=f"repos/{owner}/{repo_name}/branches",
            token=token
        )


    def fetch_releases(
        self, 
        owner: str, 
        repo_name: str,
        token: str
    ) -> list[dict]:
        """
        Fetches releases for a repository.

        Args:
            owner (str): The username of the repository owner.
            repo_name (str): The name of the repository.
            token (str): The personal access token for authentication.

        Returns:
            list[dict]: A list of dictionaries representing the releases.
        """
        return self.request(
            method="GET",
            endpoint=f"repos/{owner}/{repo_name}/releases",
            token=token
        )


    def fetch_contributors(
        self, 
        owner: str, 
        repo_name: str,
        token: str
    ) -> list[dict]:
        """
        Fetches contributors for a repository.

        Args:
            owner (str): The username of the repository owner.
            repo_name (str): The name of the repository.
            token (str): The personal access token for authentication.

        Returns:
            list[dict]: A list of dictionaries representing the contributors.
        """
        return self.request(
            method="GET",
            endpoint=f"repos/{owner}/{repo_name}/contributors",
            token=token
        )