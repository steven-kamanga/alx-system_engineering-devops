#!/usr/bin/python3
import requests

"""
This module contains a recursive function that make a query
to the Reddit api and returns a list containing titles of hot articles for a provoded subreddit.
If results are not found the function returns None.
"""

def recurse(subreddit, hot_list=[], after=None):
    """
    This function makes a query to the Reddit api and returns a list containing titles of hot articles for a provoded subreddit.
    If results are not found the function returns None.
    """
    try:
        r = requests.get("https://www.reddit.com/r/{}/hot.json".
                         format(subreddit), 
                         params={"after": after},
                         headers={"User-Agent": "custom"}, 
                         allow_redirects=False
                         ).json()
    except:
        return None
    
    if ("data" in r and "children" in r.get("data")):
        for i in r.get("data").get("children"):
            hot_list.append(i.get("data").get("title"))
        if "after" in r.get("data") and r.get("data").get("after"):
            return recurse(subreddit, hot_list,
                           r.get("data").get("after"))
        else:
            return hot_list
    else:
        return None