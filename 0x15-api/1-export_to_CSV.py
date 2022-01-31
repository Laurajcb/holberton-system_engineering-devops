#!/usr/bin/python3
"""Using what you did in the task #0,
    extend your Python script to export data in the CSV format.
"""

from sys import argv
import csv
import requests


if __name__ == "__main__":

    url = 'https://jsonplaceholder.typicode.com/users/'
    response_username = requests.get(url + argv[1])
    username = response_username.json()['username']
    tasks_list = []
    response_todos = requests.get(url + argv[1] + "/todos/")
    for items in response_todos.json():
        tasks_list.append([items["userId"], username,
                           items['completed'], items['title']])

    with open(str(tasks_list[0][0]) + '.csv', 'w') as file:
        write = csv.writer(file, quoting=csv.QUOTE_ALL)
        write.writerows(tasks_list)