#!/usr/bin/python3
"""This module uses the 'requests' library to retrieve the
 number of subscribers for a given subreddit using the Reddit API.

The 'number_of_subscribers' function takes a subreddit name as 
input and queries the Reddit API to fetch the subscriber count.
If the subreddit is valid, it returns the number of subscribers; otherwise, it returns 0.

The 'requests' library is used for making HTTP GET requests to the Reddit API.
"""

import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json().get('data').get('subscribers')
    else:
        return 0
