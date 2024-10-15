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

class Event:
    """
    Represents a GitHub event.
    """
    def __init__(self, event_data: dict) -> None:
        self._event_data = event_data or {}


    @property
    def id(self) -> str:
        return self._event_data.get("id")


    @property
    def type(self) -> str:
        return self._event_data.get("type")


    @property
    def actor(self) -> dict:
        return self._event_data.get("actor")


    @property
    def repo(self) -> dict:
        return self._event_data.get("repo")


    @property
    def created_at(self) -> str:
        return self._event_data.get("created_at")


    def __repr__(self) -> str:
        return f"Event(id={self.id})"