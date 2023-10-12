#!/usr/bin/python3
"""fetch api with not more thatn 10"""
import requests


def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of
    the first 10 hot posts listed for a given subreddit.
    """

    response = requests.get('https://api.reddit.com/r/{}/hot?limit=10'
                            .format(subreddit),  allow_redirects=False)

    if response.status_code == 200:
        subreddit_info = response.json()
        for post in subreddit_info['data']['children']:
            print(post['data']['title'])
    else:
        print(None)
