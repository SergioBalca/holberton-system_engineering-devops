#!/usr/bin/python3
"""Module with number_of_subscribers function"""

from requests import get
from sys import argv


def number_of_subscribers(subreddit):
    """ Queries the Reddit API and returns the number
        of subcribers for a given subreddit
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    data_json = get(url,
                    headers={'user-agent': 'SergioBalca'},
                    allow_redirects=False).json()

    """If not a valid subreddit, return 0"""
    if 'error' in data_json and data_json['error'] == 404:
        return 0
    r = data_json.get('data').get('subscribers')
    if r:
        return r
    else:
        return 0
