#!/usr/bin/python3
"""Using what you did in the task #0, extend your Python
    script to export data in the JSON format.
"""

from sys import argv
import json
import requests


if __name__ == "__main__":

    url = 'https://jsonplaceholder.typicode.com/users/'
    response_username = requests.get(url + argv[1])
    username = response_username.json()['username']

    response_todos = requests.get(url + argv[1] + '/todos/')
    tasks_list = []
    for items in response_todos.json():
        tasks_list.append({"task": items['title'],
                           "completed": items['completed'],
                           "username": username})

    with open(argv[1] + ".json", 'w') as json_file:
        json.dump({argv[1]: tasks_list}, json_file)
