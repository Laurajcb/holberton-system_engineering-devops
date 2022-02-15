#!/usr/bin/python3
""" Module to that queries and returns
    the first 10 hot post of a given subreddit
"""

import requests


def top_ten(subreddit):
    """Function that queries the Reddit API and returns the 10 first 
        for a given subreddit.
    """

    reddit_url = 'https://api.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'My User Agent'}
    response_request = requests.get(
        reddit_url, headers=headers, allow_redirects=False)

    if response_request.status_code == 200:
        data = response_request.json()['data']['children']
        for posts in data[:10]:
            print(posts['data']['title'])

    else:
        print('None')
