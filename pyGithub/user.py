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

class User:
    """
    Represents a GitHub user.
    """
    def __init__(self, user_data: dict) -> None:
        self._user_data = user_data or {}


    @property
    def login(self) -> str:
        return self._user_data.get("login")


    @property
    def id(self) -> int:
        return self._user_data.get("id")


    @property
    def node_id(self) -> str:
        return self._user_data.get("node_id")


    @property
    def avatar_url(self) -> str:
        return self._user_data.get("avatar_url")


    @property
    def gravatar_id(self) -> str:
        return self._user_data.get("gravatar_id")


    @property
    def url(self) -> str:
        return self._user_data.get("url")


    @property
    def html_url(self) -> str:
        return self._user_data.get("html_url")


    @property
    def followers_url(self) -> str:
        return self._user_data.get("followers_url")


    @property
    def following_url(self) -> str:
        return self._user_data.get("following_url")


    @property
    def gists_url(self) -> str:
        return self._user_data.get("gists_url")


    @property
    def starred_url(self) -> str:
        return self._user_data.get("starred_url")


    @property
    def subscriptions_url(self) -> str:
        return self._user_data.get("subscriptions_url")


    @property
    def organizations_url(self) -> str:
        return self._user_data.get("organizations_url")


    @property
    def repos_url(self) -> str:
        return self._user_data.get("repos_url")


    @property
    def events_url(self) -> str:
        return self._user_data.get("events_url")


    @property
    def received_events_url(self) -> str:
        return self._user_data.get("received_events_url")


    @property
    def type(self) -> str:
        return self._user_data.get("type")


    @property
    def site_admin(self) -> bool:
        return self._user_data.get("site_admin")


    @property
    def name(self) -> str:
        return self._user_data.get("name")


    @property
    def company(self) -> str:
        return self._user_data.get("company")


    @property
    def blog(self) -> str:
        return self._user_data.get("blog")


    @property
    def location(self) -> str:
        return self._user_data.get("location")


    @property
    def email(self) -> str:
        return self._user_data.get("email")


    @property
    def hireable(self) -> bool:
        return self._user_data.get("hireable")


    @property
    def bio(self) -> str:
        return self._user_data.get("bio")


    @property
    def twitter_username(self) -> str:
        return self._user_data.get("twitter_username")


    @property
    def public_repos(self) -> int:
        return self._user_data.get("public_repos")


    @property
    def public_gists(self) -> int:
        return self._user_data.get("public_gists")


    @property
    def followers(self) -> int:
        return self._user_data.get("followers")


    @property
    def following(self) -> int:
        return self._user_data.get("following")


    @property
    def created_at(self) -> str:
        return self._user_data.get("created_at")


    @property
    def updated_at(self) -> str:
        return self._user_data.get("updated_at")

    def __repr__(self) -> str:
        return f"User(login={self.login}, id={self.id})"
