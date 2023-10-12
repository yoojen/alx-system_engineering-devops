#!/usr/bin/python3
"""fetch api with not more thatn 10"""
import requests


def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of
    the first 10 hot posts listed for a given subreddit.
    """

    response = requests.get('https://api.reddit.com/r/{}/hot/.json'
                            .format(subreddit),  params={"limit": 10}, allow_redirects=False)
     
    if response.status_code != 200:
        print(None)
    else:
        subreddit_info = response.json().get("data")
        for sub in subreddit_indo.get("children"):
            print(sub.get("data").get("title"))
