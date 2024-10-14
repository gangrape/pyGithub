"""
ext/http.py
"""
from __future__ import annotations
from typing import Optional, Any

import requests
import json

from ..user import User
from ..repository import Repository
from .exceptions import (
    NotFound, 
    Unauthorized, 
    Forbidden, 
    BadRequest
)


class Http:
    """
    Requests manager for the GitHub API

    """
    def __init__(self) -> None:
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
        """
        return self.request(
            method="GET",
            endpoint=f"repos/{owner}/{repo_name}/contributors",
            token=token
        )