#!/usr/bin/python3
"""
This module uses the 'requests' library to retrieve the number of subscribers for a given subreddit using the Reddit API.

The 'number_of_subscribers' function takes a subreddit name as input and queries the Reddit API to fetch the subscriber count.
If the subreddit is valid, it returns the number of subscribers; otherwise, it returns 0.

The 'requests' library is used for making HTTP GET requests to the Reddit API.
"""

import requests

def number_of_subscribers(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        if 'data' in data and 'subscribers' in data['data']:
            return data['data']['subscribers']
        else:
            return 0  
    except:
        return 0  

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subscribers = number_of_subscribers(sys.argv[1])
        print(subscribers)
