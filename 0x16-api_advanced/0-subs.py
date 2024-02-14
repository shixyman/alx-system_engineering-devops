#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0
"""
import requests


def number_of_subscribers(subreddit):
    """Returns subscriber count of subreddit or 0"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "my-app/0.0.1"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()
        data = response.json()
        subscribers = data["data"].get("subscribers")
        return subscribers if subscribers is not None else 0
    except (requests.RequestException, ValueError):
        return 0