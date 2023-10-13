#!/usr/bin/python3
"""function that detch title and hold them in the list with recusive call."""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Returns a list of hot post titles"""
    url = "https://api.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "advancedapi by(eugene)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    res = response.json().get("data")
    after = res.get("after")
    count += res.get("dist")
    for c in res.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
