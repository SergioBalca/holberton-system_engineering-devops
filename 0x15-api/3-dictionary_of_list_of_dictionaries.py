#!/usr/bin/python3
"""Python script to export data in the JSON format"""

from csv import QUOTE_ALL, writer
import json
from requests import get
from sys import argv

if __name__ == '__main__':

    users = get('https://jsonplaceholder.typicode.com/users').json()
    todos = get('https://jsonplaceholder.typicode.com/todos').json()

    dict = {}
    dict_list = []
    json_file = 'todo_all_employees.json'
    with open(json_file, 'w', encoding='utf8') as f:
        for item in users:
            USER_ID = item.get('id')
            USERNAME = item.get('username')
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
