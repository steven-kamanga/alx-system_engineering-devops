#!/usr/bin/python3
""" Queries Reddit's api to get the total amount of subscribers
for a given subreddit.

Returns:
        int: 0
"""
import requests


def number_of_subscribers(subreddit):
    """ Returns the num of subscribers """
    r = requests.get("https://reddit.com/r/{}/about.json".format(subreddit),
                     headers={"User-Agent": "custom"})
    if (r.status_code == 200):
        return r.json().get("data").get("subscribers")
    else:
        return 0