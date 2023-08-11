#!/usr/bin/python3
import requests
"""
This module contains a recursive function that make a query
to the Reddit api and returns a list containing titles of hot articles for a provoded subreddit.
If results are not found the function returns None.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """queries Reddit API and returns list of titles of hot articles"""
    req = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Custom"},
        params={"after": after},
    )

    if req.status_code == 200:
        for get_data in req.json().get("data").get("children"):
            dat = get_data.get("data")
            title = dat.get("title")
            hot_list.append(title)
        after = req.json().get("data").get("after")

        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
    else:
        return None
