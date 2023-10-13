#!/usr/bin/python3
"""This query fetches th number of subscriber on reddit"""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers."""
    url = "https://api.reddit.com/r/{}/about.json".format(subreddit)

    response = requests.get(url, allow_redirects=False)
    if response.status_code != 200:
        return 0
    data = response.json().get('data')
    return data.get("subscribers")
