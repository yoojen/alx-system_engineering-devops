#!/usr/bin/python3
"""Exports to-do list info to to json format."""
import json
import requests
import sys

if __name__ == "__main__":
    userid = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    home = requests.get(url)
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    username = user.get("username")

    with open("{}.json".format(userid), "w") as jsonfile:
        json.dump({userid: [{
            "task": todo.get('title'),
            "completed": todo.get("completed"),
            "username": username
            } for todo in todos
        ]}, jsonfile)
