#!/usr/bin/python3
"""Function to print hot posts for a subreddit."""
import requests


def top_ten(subreddit):
    """Print 10 hot post titles for a subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    params = {
        "limit": 10
    }
    response = requests.get(url, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
