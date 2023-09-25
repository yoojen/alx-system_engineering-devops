#!/usr/bin/python3
"""Exports to-do list info to to json format."""
import json
import requests


if __name__ == "__main__":
url = "https://jsonplaceholder.typicode.com/"
todos = requests.get(url +"todos").json()

with open("test.json", "w") as file:
json.dump(
{
user.get('id'):
[
{
"username": user.get('username'),
"task": todo.get('title'),
"completed": todo.get('completed')
}for todo in requests.get(url + "todos", params={"userId": user.get('id')}).json()
]for user in requests.get(url + "users").json()
}, file
)  
