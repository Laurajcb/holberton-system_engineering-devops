#!/usr/bin/python3
""" Module to that queries and returns
    the number of subscribers of a subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """ Function that queries the Reddit API and returns the number of subscribers 
        (not active users, total subscribers) for a given subreddit.
    """

    reddit_url = 'https://api.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'My User Agent'}
    response_request = requests.get(
        reddit_url, headers=headers, allow_redirects=False)

    if response_request.status_code == 404:
        return 0

    subscribers = response_request.json()['data']['subscribers']
    return subscribers
