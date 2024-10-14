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
from typing import (
    List, 
    Dict, 
    Any,
    Optional
)

from pyGithub.ext.http import Http
from pyGithub.user import User
from pyGithub.repository import Repository
from pyGithub.issue import Issue


class Client:
    def __init__(
        self, 
        token: Optional[str] = ""
    ) -> None:
        """
        Initializes a Client instance for interacting with the GitHub API.

        Args:
            token (Optional[str]): A personal access token for authenticating API requests.
        """
        self.token: Optional[str] = token
        self.http: Http = Http()


    def get_user(
        self,
        username: str
    ) -> User:
        """
        Fetches a GitHub user by their username.

        Args:
            username (str): The GitHub username to fetch.

        Returns:
            User: A User object representing the fetched GitHub user.
        """
        return self.http.fetch_user(
            username=username,
            token=self.token
        )


    def get_repo(
        self, 
        owner: str, 
        repo_name: str
    ) -> Repository:
        """
        Fetches a repository by its owner's username and the repository's name.

        Args:
            owner (str): The username of the repository owner.
            repo_name (str): The name of the repository.

        Returns:
            Repository: A Repository object representing the fetched repository.
        """
        return self.http.fetch_repo(
            owner=owner, 
            repo_name=repo_name, 
            token=self.token
        )


    def search_repos(
        self, 
        query: str
    ) -> List[Repository]:
        """
        Searches for repositories using a specific query string.

        Args:
            query (str): The search query string for repositories.

        Returns:
            List[Repository]: A list of Repository objects matching the search query.
        """
        repo_data: Dict[
            str, 
            Any
        ] = self.http.search_repositories(
            query=query,
            token=self.token
        )
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
    ) -> List[Issue]:
        """
        Fetches all issues for a specified repository.

        Args:
            owner (str): The username of the repository owner.
            repo_name (str): The name of the repository.

        Returns:
            List[Issue]: A list of Issue objects representing the fetched issues.
        """
        issues_data: List[
            Dict[
                str,
                Any
            ]
        ] = self.http.fetch_issues(
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
    ) -> List[Issue]:
        """
        Fetches all pull requests for a specified repository.

        Args:
            owner (str): The username of the repository owner.
            repo_name (str): The name of the repository.

        Returns:
            List[Issue]: A list of Issue objects representing the fetched pull requests.
        """
        pulls_data: List[
            Dict[
                str, 
                Any
            ]
        ] = self.http.fetch_pull_requests(
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
    ) -> List[Dict[str, Any]]:
        """
        Fetches all commits for a specified repository.

        Args:
            owner (str): The username of the repository owner.
            repo_name (str): The name of the repository.

        Returns:
            List[Dict[str, Any]]: A list of dictionaries representing the fetched commits.
        """
        commits_data: List[
            Dict[
                str,
                Any
            ]
        ] = self.http.fetch_commits(
            owner=owner, 
            repo_name=repo_name,
            token=self.token
        )
        return commits_data


    def get_branches(
        self, 
        owner: str, 
        repo_name: str
    ) -> List[Dict[str, Any]]:
        """
        Fetches all branches for a specified repository.

        Args:
            owner (str): The username of the repository owner.
            repo_name (str): The name of the repository.

        Returns:
            List[Dict[str, Any]]: A list of dictionaries representing the fetched branches.
        """
        branches_data: List[
            Dict[
                str,
                Any
            ]
        ] = self.http.fetch_branches(
            owner=owner, 
            repo_name=repo_name,
             token=self.token
        )
        return branches_data


    def get_releases(
        self, 
        owner: str,
        repo_name: str
    ) -> List[Dict[str, Any]]:
        """
        Fetches all releases for a specified repository.

        Args:
            owner (str): The username of the repository owner.
            repo_name (str): The name of the repository.

        Returns:
            List[Dict[str, Any]]: A list of dictionaries representing the fetched releases.
        """
        releases_data: List[
            Dict[
                str, 
                Any
            ]
        ] = self.http.fetch_releases(
            owner=owner, 
            repo_name=repo_name,
            token=self.token
        )
        return releases_data


    def get_contributors(
        self, 
        owner: str,
        repo_name: str
    ) -> List[User]:
        """
        Fetches contributors for a specified repository.

        Args:
            owner (str): The username of the repository owner.
            repo_name (str): The name of the repository.

        Returns:
            List[User]: A list of User objects representing the fetched contributors.
        """
        contributors_data: List[
            Dict[
                str, 
                Any
            ]
        ] = self.http.fetch_contributors(
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