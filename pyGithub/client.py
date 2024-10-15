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
from pyGithub.commit import Commit  
from pyGithub.branch import Branch  
from pyGithub.release import Release  
from pyGithub.milestone import Milestone  
from pyGithub.label import Label  
from pyGithub.event import Event  
from pyGithub.traffic import Traffic  


class Client:
    """
    A Client for interacting with the GitHub API.

    This class provides methods to perform various operations related to
    GitHub resources such as users, repositories, issues, pull requests,
    commits, branches, releases, and contributors. The Client utilizes an 
    authentication token to access the API, ensuring that the requests are 
    made securely and can include rate limits where applicable.
    """

    def __init__(self, token: Optional[str] = "") -> None:
        self.token: Optional[str] = token
        self.http: Http = Http()


    def get_user(self, username: str) -> User:
        return self.http.fetch_user(username=username, token=self.token)


    def get_repo(self, owner: str, repo_name: str) -> Repository:
        return self.http.fetch_repo(owner=owner, repo_name=repo_name, token=self.token)


    def search_repos(self, query: str) -> List[Repository]:
        repo_data: Dict[str, Any] = self.http.search_repositories(
            query=query, token=self.token
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


    def get_issues(self, owner: str, repo_name: str) -> List[Issue]:
        issues_data: List[Dict[str, Any]] = self.http.fetch_issues(
            owner=owner, repo_name=repo_name, token=self.token
        )
        return [
            Issue(
                issue
            ) 
            for issue 
            in issues_data
        ]


    def get_pull_requests(self, owner: str, repo_name: str) -> List[Issue]:
        pulls_data: List[Dict[str, Any]] = self.http.fetch_pull_requests(
            owner=owner, repo_name=repo_name, token=self.token
        )
        return [
            Issue(
                pull
            )
            for pull 
            in pulls_data
        ]


    def get_commits(self, owner: str, repo_name: str) -> List[Commit]:
        commits_data: List[Dict[str, Any]] = self.http.fetch_commits(
            owner=owner, repo_name=repo_name, token=self.token
        )
        return [
            Commit(commit)
            for commit in commits_data
        ]


    def get_branches(self, owner: str, repo_name: str) -> List[Branch]:
        branches_data: List[Dict[str, Any]] = self.http.fetch_branches(
            owner=owner, repo_name=repo_name, token=self.token
        )
        return [
            Branch(branch)
            for branch in branches_data
        ]


    def get_releases(self, owner: str, repo_name: str) -> List[Release]:
        releases_data: List[Dict[str, Any]] = self.http.fetch_releases(
            owner=owner, repo_name=repo_name, token=self.token
        )
        return [
            Release(release)
            for release in releases_data
        ]


    def get_contributors(self, owner: str, repo_name: str) -> List[User]:
        contributors_data: List[Dict[str, Any]] = self.http.fetch_contributors(
            owner=owner, repo_name=repo_name, token=self.token
        )
        return [
            User(
                contributor
            ) 
            for contributor
            in contributors_data
        ]


    def get_issue(self, owner: str, repo_name: str, issue_number: int) -> Issue:
        issue_data: Dict[str, Any] = self.http.fetch_issue(
            owner=owner, repo_name=repo_name, issue_number=issue_number, token=self.token
        )
        return Issue(issue_data)


    def create_issue(self, owner: str, repo_name: str, title: str, body: Optional[str] = None) -> Issue:
        issue_data: Dict[str, Any] = self.http.create_issue(
            owner=owner, repo_name=repo_name, title=title, body=body, token=self.token
        )
        return Issue(issue_data)


    def get_milestones(self, owner: str, repo_name: str) -> List[Milestone]:
        milestones_data: List[Dict[str, Any]] = self.http.fetch_milestones(
            owner=owner, repo_name=repo_name, token=self.token
        )
        return [
            Milestone(milestone)
            for milestone in milestones_data
        ]


    def create_milestone(
        self, 
        owner: str,
        repo_name: str, 
        title: str, 
        description: Optional[str] = None, 
        due_on: Optional[str] = None
    ) -> Dict[str, Any]:
        milestone_data: Dict[str, Any] = self.http.create_milestone(
            owner=owner,
            repo_name=repo_name, 
            title=title, 
            description=description, 
            due_on=due_on, 
            token=self.token
        )
        return milestone_data


    def get_labels(self, owner: str, repo_name: str) -> List[Label]:
        labels_data: List[Dict[str, Any]] = self.http.fetch_labels(
            owner=owner, repo_name=repo_name, token=self.token
        )
        return [
            Label(label)
            for label in labels_data
        ]


    def create_label(self, owner: str, repo_name: str, name: str, color: str) -> Dict[str, Any]:
        label_data: Dict[str, Any] = self.http.create_label(
            owner=owner, repo_name=repo_name, name=name, color=color, token=self.token
        )
        return label_data


    def get_events(self, owner: str, repo_name: str) -> List[Event]:
        events_data: List[Dict[str, Any]] = self.http.fetch_events(
            owner=owner, repo_name=repo_name, token=self.token
        )
        return [
            Event(event)
            for event in events_data
        ]


    def get_commit(self, owner: str, repo_name: str, commit_sha: str) -> Commit:
        commit_data: Dict[str, Any] = self.http.fetch_commit(
            owner=owner, repo_name=repo_name, commit_sha=commit_sha, token=self.token
        )
        return Commit(commit_data)


    def get_release(self, owner: str, repo_name: str, release_id: int) -> Release:
        release_data: Dict[str, Any] = self.http.fetch_release(
            owner=owner, repo_name=repo_name, release_id=release_id, token=self.token
        )
        return Release(release_data)


    def create_release(
        self, 
        owner: str, 
        repo_name: str, 
        tag_name: str, 
        name: Optional[str] = None,
        body: Optional[str] = None,
        draft: bool = False, 
        prerelease: bool = False
    ) -> Release:
        release_data: Dict[str, Any] = self.http.create_release(
            owner=owner, 
            repo_name=repo_name,
            tag_name=tag_name,
            name=name,
            body=body, 
            draft=draft, 
            prerelease=prerelease,
            token=self.token
        )
        return Release(release_data)


    def get_forks(self, owner: str, repo_name: str) -> List[Repository]:
        forks_data: List[Dict[str, Any]] = self.http.fetch_forks(
            owner=owner, repo_name=repo_name, token=self.token
        )
        return [
            Repository(fork)
            for fork in forks_data
        ]


    def get_stargazers(self, owner: str, repo_name: str) -> List[User]:
        stargazers_data: List[Dict[str, Any]] = self.http.fetch_stargazers(
            owner=owner, repo_name=repo_name, token=self.token
        )
        return [
            User(stargazer)
            for stargazer in stargazers_data
        ]


    def get_watched_repos(self) -> List[Repository]:
        watched_data: List[Dict[str, Any]] = self.http.fetch_watched_repos(token=self.token)
        return [
            Repository(repo)
            for repo in watched_data
        ]


    def get_repositories_for_user(self, username: str) -> List[Repository]:
        user_repos_data: List[Dict[str, Any]] = self.http.fetch_repositories_for_user(username=username, token=self.token)
        return [
            Repository(repo)
            for repo in user_repos_data
        ]


    def get_notifications(self) -> List[Dict[str, Any]]:
        notifications_data: List[Dict[str, Any]] = self.http.fetch_notifications(token=self.token)
        return notifications_data


    def mark_notifications_as_read(self) -> Dict[str, Any]:
        return self.http.mark_notifications_as_read(token=self.token)


    def get_repo_topics(self, owner: str, repo_name: str) -> Dict[str, Any]:
        topics_data: Dict[str, Any] = self.http.fetch_repo_topics(
            owner=owner, repo_name=repo_name, token=self.token
        )
        return topics_data


    def replace_repo_topics(self, owner: str, repo_name: str, names: List[str]) -> Dict[str, Any]:
        return self.http.replace_repo_topics(
            owner=owner, repo_name=repo_name, names=names, token=self.token
        )


    def get_traffic_views(self, owner: str, repo_name: str) -> Dict[str, Any]:
        traffic_views_data: Dict[str, Any] = self.http.fetch_traffic_views(
            owner=owner, repo_name=repo_name, token=self.token
        )
        return traffic_views_data


    def get_traffic_clones(self, owner: str, repo_name: str) -> Dict[str, Any]:
        traffic_clones_data: Dict[str, Any] = self.http.fetch_traffic_clones(
            owner=owner, repo_name=repo_name, token=self.token
        )
        return traffic_clones_data


    def get_traffic(self, owner: str, repo_name: str) -> Traffic:
        traffic_data: Dict[str, Any] = self.http.fetch_traffic(
            owner=owner, repo_name=repo_name, token=self.token
        )
        return Traffic(traffic_data)