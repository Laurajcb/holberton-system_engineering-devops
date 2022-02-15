#!/usr/bin/python3
""" Module that queries and returns
    a list containing all titles for a given subreddit
"""

import requests


def recurse(subreddit, hot_list=[], aft=""):
    """ Function that queries the Reddit API and returns
        a list containing the titles of all hot articles for a given subreddit
    """
    reddit_url = 'https://www.reddit.com/r/{}/hot/.json?after={}'.format(
        subreddit, aft)
    headers = {'User-Agent': 'My User Agent'}
    response = requests.get(reddit_url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        aft = response.json()['data']['after']

        for element in response.json()['data']['children']:
            hot_list.append(element['data']['title'])

        if aft:
            recurse(subreddit, hot_list, aft)
        return hot_list
    return None
