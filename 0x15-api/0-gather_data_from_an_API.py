#!/usr/bin/python3
"""request through api and show on the stout"""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    home = requests.get(url)
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    user = requests.get(url + "users", params={"id": sys.argv[1]}).json()
    taskTitle = [todo.get("title") for todo in todos
                 if todo.get("completed") is True]

    for one in user:
        name = one.get("name")
    print("Employee  {} is done with task({}/{})"
          .format(name, len(taskTitle), len(todos)))
    [print("\t{}".format(todo.get("title"))) for todo in todos if
     todo.get("completed") is True]
