#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""
import requests

def number_of_subscribers(subreddit):
    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'My Reddit API Client'}

    # Make the API request to retrieve subreddit information
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        try:
            data = response.json()
            return data['data']['subscribers']
        except KeyError:
            # Invalid subreddit
            return 0
    else:
        # Invalid subreddit or other error
        return 0