"""
repository.py
"""
class Repository:
    """
    Represents a GitHub repository.
    """
    def __init__(self, repo_data: dict) -> None:
        self._repo_data = repo_data or {}


    @property
    def id(self) -> int:
        return self._repo_data.get("id")


    @property
    def node_id(self) -> str:
        return self._repo_data.get("node_id")


    @property
    def name(self) -> str:
        return self._repo_data.get("name")


    @property
    def full_name(self) -> str:
        return self._repo_data.get("full_name")


    @property
    def owner(self) -> dict:
        return self._repo_data.get("owner")


    @property
    def html_url(self) -> str:
        return self._repo_data.get("html_url")


    @property
    def description(self) -> str:
        return self._repo_data.get("description")


    @property
    def fork(self) -> bool:
        return self._repo_data.get("fork")


    @property
    def url(self) -> str:
        return self._repo_data.get("url")


    @property
    def forks_url(self) -> str:
        return self._repo_data.get("forks_url")


    @property
    def keys_url(self) -> str:
        return self._repo_data.get("keys_url")


    @property
    def collaborators_url(self) -> str:
        return self._repo_data.get("collaborators_url")


    @property
    def teams_url(self) -> str:
        return self._repo_data.get("teams_url")


    @property
    def hooks_url(self) -> str:
        return self._repo_data.get("hooks_url")


    @property
    def issue_events_url(self) -> str:
        return self._repo_data.get("issue_events_url")


    @property
    def events_url(self) -> str:
        return self._repo_data.get("events_url")


    @property
    def assignees_url(self) -> str:
        return self._repo_data.get("assignees_url")


    @property
    def branches_url(self) -> str:
        return self._repo_data.get("branches_url")


    @property
    def tags_url(self) -> str:
        return self._repo_data.get("tags_url")


    @property
    def blobs_url(self) -> str:
        return self._repo_data.get("blobs_url")


    @property
    def git_tags_url(self) -> str:
        return self._repo_data.get("git_tags_url")


    @property
    def git_refs_url(self) -> str:
        return self._repo_data.get("git_refs_url")


    @property
    def trees_url(self) -> str:
        return self._repo_data.get("trees_url")


    @property
    def statuses_url(self) -> str:
        return self._repo_data.get("statuses_url")


    @property
    def languages_url(self) -> str:
        return self._repo_data.get("languages_url")


    @property
    def stargazers_count(self) -> int:
        return self._repo_data.get("stargazers_count")


    @property
    def watchers_count(self) -> int:
        return self._repo_data.get("watchers_count")


    @property
    def size(self) -> int:
        return self._repo_data.get("size")


    @property
    def default_branch(self) -> str:
        return self._repo_data.get("default_branch")


    @property
    def open_issues_count(self) -> int:
        return self._repo_data.get("open_issues_count")


    @property
    def is_template(self) -> bool:
        return self._repo_data.get("is_template")


    @property
    def topics(self) -> list:
        return self._repo_data.get("topics")


    @property
    def has_issues(self) -> bool:
        return self._repo_data.get("has_issues")


    @property
    def has_projects(self) -> bool:
        return self._repo_data.get("has_projects")


    @property
    def has_wiki(self) -> bool:
        return self._repo_data.get("has_wiki")


    @property
    def has_pages(self) -> bool:
        return self._repo_data.get("has_pages")


    @property
    def has_downloads(self) -> bool:
        return self._repo_data.get("has_downloads")


    @property
    def archived(self) -> bool:
        return self._repo_data.get("archived")


    @property
    def disabled(self) -> bool:
        return self._repo_data.get("disabled")


    @property
    def visibility(self) -> str:
        return self._repo_data.get("visibility")


    @property
    def created_at(self) -> str:
        return self._repo_data.get("created_at")


    @property
    def updated_at(self) -> str:
        return self._repo_data.get("updated_at")


    @property
    def pushed_at(self) -> str:
        return self._repo_data.get("pushed_at")


    @property
    def homepage(self) -> str:
        return self._repo_data.get("homepage")

    def __repr__(self) -> str:
        return f"Repository(name={self.name}, owner={self.owner.get('login') if self.owner else None})"
