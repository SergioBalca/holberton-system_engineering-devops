#!/usr/bin/python3
"""Python script to export data in the JSON format"""

from csv import QUOTE_ALL, writer
import json
from requests import get
from sys import argv

if __name__ == '__main__':

    USER_ID = argv[1]
    users = get('https://jsonplaceholder.typicode.com/users/{}'.
                format(USER_ID)).json()
    todos = get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                format(USER_ID)).json()

    USERNAME = users.get('username')
    json_file = '{}.json'.format(USER_ID)
    dict = {}
    dict_list = []
    with open(json_file, 'w', encoding='utf8') as f:
        for element in todos:
            TASK_TITLE = element.get('title')
            TASK_COMPLETED_STATUS = element.get('completed')
            user_tasks = {
                'task':  TASK_TITLE,
                'completed': TASK_COMPLETED_STATUS,
                'username': USERNAME,
            }
            dict_list.append(user_tasks)
            dict[USER_ID] = dict_list
        json.dump(dict, f)
