"""
issue.py
"""
class Issue:
    """
    Represents a GitHub issue or pull request.
    """
    def __init__(self, issue_data: dict) -> None:
        self._issue_data = issue_data or {}


    @property
    def id(self) -> int:
        return self._issue_data.get("id")


    @property
    def number(self) -> int:
        return self._issue_data.get("number")


    @property
    def title(self) -> str:
        return self._issue_data.get("title")


    @property
    def body(self) -> str:
        return self._issue_data.get("body")


    @property
    def state(self) -> str:
        return self._issue_data.get("state")


    @property
    def created_at(self) -> str:
        return self._issue_data.get("created_at")


    @property
    def updated_at(self) -> str:
        return self._issue_data.get("updated_at")


    @property
    def user(self) -> dict:
        return self._issue_data.get("user")


    @property
    def html_url(self) -> str:
        return self._issue_data.get("html_url")

    def __repr__(self) -> str:
        return f"Issue(title={self.title}, state={self.state}, user={self.user.get('login') if self.user else None})"