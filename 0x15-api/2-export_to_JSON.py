#!/usr/bin/python3
""" Python script to export data in the JSON format."""
import json
import requests
import sys
argv = sys.argv


if __name__ == "__main__":
    r = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                     .format(argv[1]))
    user = r.json().get("username")

    r = requests.get("https://jsonplaceholder.typicode.com/todos/",
                     params={"userId": argv[1]})
    todos = r.json()
    l = []
    dd = {}
    for t in todos:
        dd = {"task": t.get("title"),
              "completed": t.get("completed"),
              "username": user
              }
        l.append(dd)
    d = {argv[1]: l}
    with open("{}.json".format(argv[1]), "w") as f:
        json.dump(d, f)
