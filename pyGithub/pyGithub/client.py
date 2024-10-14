"""
client.py
"""
from __future__ import annotations

from .ext.http import Http
from .user import User
from .repository import Repository
from .issue import Issue


class Client:
    def __init__(self, token: str) -> None:
        self.token = token
        self.http_client = Http()


    def get_user(self, username: str) -> User:
        """
        Fetches a user by username.
        """
        return self.http_client.fetch_user(
            username=username,
            token=self.token
        )


    def get_repo(
        self, 
        owner: str, 
        repo_name: str
    ) -> Repository:
        """
        Fetches a repository by owner and name.
        """
        return self.http_client.fetch_repo(
            owner=owner,
             repo_name=repo_name, 
             token=self.token
        )


    def search_repos(self, query: str) -> list[Repository]:
        """
        Searches for repositories by query.
        """
        repo_data = self.http_client.search_repositories(query=query, token=self.token)
        return [
            Repository(
                repo
            )
            for repo 
            in repo_data.get(
                "items",
                []
            )
        ]


    def get_issues(
        self, 
        owner: str, 
        repo_name: str
    ) -> list[Issue]:
        """
        Fetches issues for a repository.
        """
        issues_data = self.http_client.fetch_issues(
            owner=owner,
             repo_name=repo_name, 
             token=self.token
        )
        return [
            Issue(
                issue
            ) 
            for issue 
            in issues_data
        ]


    def get_pull_requests(
        self, 
        owner: str, 
        repo_name: str
    ) -> list[Issue]:
        """
        Fetches pull requests for a repository.
        """
        pulls_data = self.http_client.fetch_pull_requests(
            owner=owner,
             repo_name=repo_name, 
             token=self.token
        )
        return [
            Issue(
                pull
            ) 
            for pull 
            in pulls_data
        ]


    def get_commits(
        self, 
        owner: str, 
        repo_name: str
    ) -> list[dict]:
        """
        Fetches commits for a repository.
        """
        commits_data = self.http_client.fetch_commits(
            owner=owner,
             repo_name=repo_name, 
             token=self.token
        )
        return commits_data


    def get_branches(
        self, 
        owner: str, 
        repo_name: str
    ) -> list[dict]:
        """
        Fetches branches for a repository.
        """
        branches_data = self.http_client.fetch_branches(
            owner=owner,
             repo_name=repo_name, 
             token=self.token
        )
        return branches_data


    def get_releases(
        self, 
        owner: str, 
        repo_name: str
    ) -> list[dict]:
        """
        Fetches releases for a repository.
        """
        releases_data = self.http_client.fetch_releases(
            owner=owner,
             repo_name=repo_name, 
             token=self.token
        )
        return releases_data


    def get_contributors(
        self, 
        owner: str, 
        repo_name: str
    ) -> list[User]:
        """
        Fetches contributors for a repository.
        """
        contributors_data = self.http_client.fetch_contributors(
            owner=owner,
             repo_name=repo_name, 
             token=self.token
        )
        return [
            User(
                contributor
            ) 
            for contributor 
            in contributors_data
        ]