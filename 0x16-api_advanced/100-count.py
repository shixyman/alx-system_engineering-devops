#!/usr/bin/python3

""" Recursive function that queries the Reddit API, parses the title of all
hot articles, and prints a sorted count of given keywords (case-insensitive,
delimited by spaces. Javascript should count as javascript,
but java should not)
"""
import requests
from collections import Counter

def count_words(subreddit, word_list, after=None, counts=Counter()):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "My Reddit API Client"}  # Set a custom User-Agent
    
    params = {
        "limit": 100,
        "after": after
    }
    
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json()
        children = data["data"]["children"]
        
        for child in children:
            title = child["data"]["title"].lower()
            for word in word_list:
                if word.lower() in title.split():
                    counts[word.lower()] += 1
        
        after = data["data"]["after"]
        
        if after:
            return count_words(subreddit, word_list, after=after, counts=counts)
        else:
            print_results(counts)
    else:
        print(f"Invalid subreddit: {subreddit}")
    
def print_results(counts):
    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_counts:
        print(f"{word}: {count}")