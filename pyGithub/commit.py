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

class Commit:
    """
    Represents a GitHub commit.
    """
    def __init__(self, commit_data: dict) -> None:
        self._commit_data = commit_data or {}


    @property
    def sha(self) -> str:
        return self._commit_data.get("sha")


    @property
    def commit(self) -> dict:
        return self._commit_data.get("commit")


    @property
    def author(self) -> dict:
        return self._commit_data.get("author")


    @property
    def committer(self) -> dict:
        return self._commit_data.get("committer")


    @property
    def url(self) -> str:
        return self._commit_data.get("url")


    def __repr__(self) -> str:
        return f"Commit(sha={self.sha})"