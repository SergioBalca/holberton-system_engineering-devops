#!/usr/bin/python3
"""Module with top_ten function"""

from requests import get
from sys import argv


def top_ten(subreddit):
    """ Queries the Reddit API and prints the titles of the
        first 10 hot posts listed for a given subreddit
    """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    data_json = get(url,
                    headers={'user-agent': 'SergioBalca'},
                    allow_redirects=False).json()

    if 'error' in data_json and data_json['error'] == '404':
        print(None)
        return None
    """To avoid key error in case a no valid subreddit is passed"""
    if 'data' in data_json:
        for dict in data_json['data']['children']:
            print(dict.get('data').get('title'))
    else:
        print(None)
        return None
