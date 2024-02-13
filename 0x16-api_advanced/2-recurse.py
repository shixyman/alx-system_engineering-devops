#!/usr/bin/python3
"""Module for task 2"""

import requests

def recurse(subreddit, hot_list=[]):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "My Reddit API Client"}  # Set a custom User-Agent
    
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json()
        children = data["data"]["children"]
        
        for child in children:
            title = child["data"]["title"]
            hot_list.append(title)
        
        after = data["data"]["after"]
        
        if after:
            return recurse(subreddit, hot_list=hot_list)
        else:
            return hot_list
    else:
        return None
