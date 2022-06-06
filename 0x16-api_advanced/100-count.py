#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit
"""

import operator
import requests


def count_words(subreddit, word_list, dict_list={}, after=''):
    url = 'https://www.reddit.com/r/'+subreddit+'/hot.json?after='+after
    json = requests.get(url, headers={'user-agent': 'Mozilla/5.0'}).json()

    if 'error' in json or json['data']['children'] == []:
        return None

    if len(dict_list) == 0:
        for word in word_list:
            dict_list[word] = 0

    children = json['data']['children']
    for child in children:
        tokens = child['data']['title'].upper()
        tokens = tokens.split()
        for token in tokens:
            for word in word_list:
                if token == word.upper():
                    dict_list[word] += 1
    after = json['data']['after']
    if after is None:
        sorted_dict = sorted(dict_list.items(), key=operator.itemgetter(1),
                             reverse=True)
        ordered = False
        size = len(sorted_dict)
        while ordered is False:
            ordered = True
            for i in range(size):
                if (i < size - 1):
                    if (sorted_dict[i][1] == sorted_dict[i+1][1] and
                            sorted_dict[i][0] > sorted_dict[i+1][0]):
                        ordered = False
                        aux = sorted_dict[i]
                        sorted_dict[i] = sorted_dict[i+1]
                        sorted_dict[i+1] = aux

        for value in sorted_dict:
            if value[1] > 0:
                print("{}: {}".format(value[0], value[1]))
    else:
        count_words(subreddit, word_list, dict_list, after)
