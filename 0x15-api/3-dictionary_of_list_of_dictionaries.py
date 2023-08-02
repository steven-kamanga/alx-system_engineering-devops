#!/usr/bin/python3
""" Python script to export data in the JSON format."""
import json
import requests


if __name__ == "__main__":
    r = requests.get("https://jsonplaceholder.typicode.com/users/")
    user = r.json()
    list_ids = [int(u.get("id")) for u in user]
    d = {}
    for i in list_ids:
        r = requests.get("https://jsonplaceholder.typicode.com/users/",
                         params={"id": i}).json()
        user = r[0].get("username")
        r = requests.get("https://jsonplaceholder.typicode.com/todos/",
                         params={"userId": i})
        todos = r.json()
        l = []
        dd = {}
        for t in todos:
            dd = {"username": user,
                  "task": t.get("title"),
                  "completed": t.get("completed")
                  }
            l.append(dd)
        d.update({i: l})
        with open("todo_all_employees.json", "w") as f:
            json.dump(d, f)
