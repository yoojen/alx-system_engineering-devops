#!/usr/bin/python3
"""Exports information for employee to CSV format."""
import csv
import requests
import sys

if __name__ == "__main__":
url = "https://jsonplaceholder.typicode.com/"
home = requests.get(url)
todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
user = requests.get(url + "users/{}".format(sys.argv[1])).json()
taskTitle = [todo.get("title") for todo in todos]
checkCompletion = [todo.get("completed") for todo in todos]
username = user.get("username")

with open("{}.csv".format(sys.argv[1]), "w", newline="") as file:
writer = csv.writer(file, quoting=csv.QUOTE_ALL)
[
writer.writerow(
[sys.argv[1], username, todo.get('completed'), todo.get('title')]
) for todo in todos
]
