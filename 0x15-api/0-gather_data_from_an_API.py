#!/usr/bin/python3
"""Write a Python script that, using this REST API,
    for a given employee ID, returns information about
    his/her TODO list progress.
"""

import requests
from sys import argv


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/users/'
    response_user = requests.get(url + argv[1])
    employee_name = response_user.json()['name']

    response_todos = requests.get(url + argv[1] + '/todos')
    total_tasks = response_todos.json()
    done_tasks = []
    for dic in total_tasks:
        if dic['completed']:
            done_tasks.append(dic['title'])

    print('Employee {} is done with tasks({}/{}):'
          .format(employee_name, len(done_tasks), len(total_tasks)))
    for tasks in done_tasks:
        print('\t', tasks)
