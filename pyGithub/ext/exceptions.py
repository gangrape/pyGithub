"""
ext/exceptions.py
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
