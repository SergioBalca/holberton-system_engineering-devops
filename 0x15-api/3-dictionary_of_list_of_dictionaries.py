#!/usr/bin/python3
"""Python script to export data in the JSON format"""

import json
from requests import get


if __name__ == '__main__':

    users = get('https://jsonplaceholder.typicode.com/users').json()
    url = 'https://jsonplaceholder.typicode.com/todos'

    dict = {}

    json_file = 'todo_all_employees.json'
    with open(json_file, 'w', encoding='utf8') as f:
        for item in users:
            dict_list = []
            USER_ID = {'userID': item['id']}

            todos = get(url, params=USER_ID).json()
            for element in todos:
                USERNAME = item.get('username')
                TASK_TITLE = element.get('title')
                TASK_COMPLETED_STATUS = element.get('completed')
                user_tasks = {
                    'task':  TASK_TITLE,
                    'completed': TASK_COMPLETED_STATUS,
                    'username': USERNAME,
                }
                dict_list.append(user_tasks)
                dict[item['id']] = dict_list
        json.dump(dict, f)
