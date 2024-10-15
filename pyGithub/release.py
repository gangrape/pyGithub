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

class Release:
    """
    Represents a GitHub release.
    """
    def __init__(self, release_data: dict) -> None:
        self._release_data = release_data or {}


    @property
    def id(self) -> int:
        return self._release_data.get("id")


    @property
    def tag_name(self) -> str:
        return self._release_data.get("tag_name")


    @property
    def name(self) -> str:
        return self._release_data.get("name")


    @property
    def body(self) -> str:
        return self._release_data.get("body")


    @property
    def published_at(self) -> str:
        return self._release_data.get("published_at")


    def __repr__(self) -> str:
        return f"Release(tag_name={self.tag_name})"