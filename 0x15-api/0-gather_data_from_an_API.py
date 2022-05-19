#!/usr/bin/python3
""" Using this REST API, for a given employee ID, returns
information about his/her TODO list progress. """

from requests import get
from sys import argv

if __name__ == '__main__':

    user_id = argv[1]
    users = get('https://jsonplaceholder.typicode.com/users/{}'.
                format(user_id)).json()
    todos = get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                format(user_id)).json()

    EMPLOYEE_NAME = users.get('name')
    NUMBER_OF_DONE_TASKS = 0
    for task in todos:
        if task.get('completed') is True:
            NUMBER_OF_DONE_TASKS += 1
        TOTAL_NUMBER_OF_TASKS = len(todos)

    print("Employee {} is done with tasks({}/{}):".format(
        EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for title in todos:
        TASK_TITLE = title.get('title')
        if title.get('completed') is True:
            print("\t {}".format(TASK_TITLE))
