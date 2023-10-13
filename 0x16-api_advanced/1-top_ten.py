#!/usr/bin/python3
"""Function to print hot posts for a subreddit."""
import requests


def top_ten(subreddit):
    """Returns top ten post

    Keyword arguments:
    subreddit -- topic to be searched on the reddit
    Return: return title of post
    """
    url = "https://api.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url, params={"limit": 10}, allow_redirects=False)
    if response.status_code != 200:
        print(None)
    else:
        data = response.json().get('data').get('children')
        for single in data:
            print(single.get('data').get('title'))
