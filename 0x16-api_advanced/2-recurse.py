#!/usr/bin/python3
""" queries the Reddit API and returns a list containing the titles
    of all hot articles for a given subreddit.
    If no results are found for the given subreddit,
    the function should return None
"""


from requests import get


def recurse(subreddit, hot_list=[], after=None):
    """ queries the Reddit API and returns a list containing the titles
        of all hot articles for a given subreddit.
        If no results are found for the given subreddit,
        the function should return None
    """

    url = 'https://www.reddit.com/r/{}/hot.json?after={}'
    .format(subreddit, after)
    data_json = get(url, headers={'user-agent': 'SergioBalca'},
                    allow_redirects=False).json()

    if 'error' in data_json or data_json['data']['children'] == []:
        return None

    for item in data_json['data']['children']:
        """Saving first page of posts"""
        hot_list.append(data_json['data']['title'])
    after = data_json['data']['after']
    if after is None:
        return hot_list
    else:
        return recurse(subreddit, hot_list, after)
