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
        x = []
        dd = {}
        for t in todos:
            dd = {"username": user,
                  "task": t.get("title"),
                  "completed": t.get("completed")
                  }
            x.append(dd)
        d.update({i: x})
        with open("todo_all_employees.json", "w") as f:
            json.dump(d, f)
