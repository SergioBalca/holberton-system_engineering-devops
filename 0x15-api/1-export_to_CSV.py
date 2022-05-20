#!/usr/bin/python3
""" Using this REST API, for a given employee ID, returns
information about his/her TODO list progress. """

from csv import QUOTE_ALL, writer
from requests import get
from sys import argv

if __name__ == '__main__':

    USER_ID = argv[1]
    users = get('https://jsonplaceholder.typicode.com/users/{}'.
                format(USER_ID)).json()
    todos = get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                format(USER_ID)).json()

    csv_file = '{}.csv'.format(USER_ID)
    response_list = []
    USERNAME = users.get('username')
    with open(csv_file, 'w', encoding='utf8', newline='') as f:
        w = writer(f, quoting=QUOTE_ALL)
        for task in todos:
            TASK_COMPLETED_STATUS = task.get('completed')
            TASK_TITLE = task.get('title')
            response_list.append(USER_ID)
            response_list.append(USERNAME)
            response_list.append(TASK_COMPLETED_STATUS)
            response_list.append(TASK_TITLE)
            w.writerow(response_list)
