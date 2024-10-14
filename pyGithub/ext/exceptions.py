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

class GitHubError(Exception):
    """Base class for all GitHub errors.
    """
    pass


class NotFound(GitHubError):
    """
    Exception raised for 404 errors.
    """
    def __init__(
        self, 
        message: str = "Resource not found."
    ) -> None:
        super().__init__(message)


class Unauthorized(GitHubError):
    """
    Exception raised for 401 errors.
    """
    def __init__(
        self, 
        message: str = "Unauthorized access."
    ) -> None:
        super().__init__(message)


class Forbidden(GitHubError):
    """
    Exception raised for 403 errors.
    """
    def __init__(
        self, 
        message: str = "Forbidden access."
    ) -> None:
        super().__init__(message)


class BadRequest(GitHubError):
    """
    Exception raised for 400 errors.
    """
    def __init__(
        self, 
        message: str = "Bad request."
    ) -> None:
        super().__init__(message)
