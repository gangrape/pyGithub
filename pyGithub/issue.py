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