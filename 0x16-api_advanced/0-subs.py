#!/usr/bin/python3
"""This query fetches th number of subscriber on reddit"""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    response = requests.get(url, allow_redirects=False)
    if response.status_code == 404:
        return 0
    return response.json().get("data").get("subscribers")
