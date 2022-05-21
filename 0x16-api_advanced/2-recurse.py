#!/usr/bin/python3
"""Module with top_ten recurse function"""

import sys
from requests import get
from sys import argv


def recurse(subreddit, hot_list=[], after=''):
    """ queries the Reddit API and returns a list containing the titles
        of all hot articles for a given subreddit.
        If no results are found for the given subreddit,
        the function should return None
    """
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'
    .format(subreddit, after)
    data_json = get(url,
                    headers={'user-agent': 'SergioBalca'},
                    allow_redirects=False).json()

    if 'error' in data_json and data_json['error'] == '404':
        return None
    """To avoid key error in case a no valid subreddit is passed"""
    if 'data' in data_json:
        for dict in data_json['data']['children']:
            """Saving first page in the list"""
            hot_list.append(dict.get('data').get('title'))
        after = data_json.get('data').get('after')
    """After is None in the last page"""
    if after is None:
        return hot_list
    else:
        """To go to next page"""
        return recurse(subreddit, hot_list, after)
