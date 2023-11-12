#!/usr/bin/python3
"""
2-recurse.py

This module defines a recursive function 'recurse' that queries the Reddit API
and returns a list containing the titles of all hot articles for a given subreddit.
If no results are found for the given subreddit, the function returns None.

Requirements:
- Prototype: def recurse(subreddit, hot_list=None, after=None)
- If not a valid subreddit, return None.
- Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.
- Your code will NOT pass if you are using a loop and not recursively calling the function! This /can/ be done with a loop
  but the point is to use a recursive function. :)

Usage:
1. Call the script from the command line with a subreddit as an argument.

Example:
$ python3 2-main.py programming

Author: Your Name
"""

import requests

def recurse(subreddit, hot_list=None, after=None):
    """
    Recursively queries the Reddit API to retrieve the titles of all hot articles for a given subreddit.

    Parameters:
    - subreddit (str): The name of the subreddit to search.
    - hot_list (list, optional): A list to store the titles of hot articles. Defaults to None.
    - after (str, optional): The 'after' parameter for pagination. Defaults to None.

    Returns:
    - list or None: A list containing the titles of hot articles or None if the subreddit is invalid.
    """
    if hot_list is None:
        hot_list = []

    headers = {'User-Agent': 'MyBot/1.0 (by /u/gihozoi)'}  

    # Base URL for the Reddit API
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'

    # Add the 'after' parameter if it's provided
    params = {'after': after} if after else {}

    # Make the API request
    response = requests.get(url, headers=headers, params=params)

    # Check if the request was successful
    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        return None

    # Parse the JSON response
    data = response.json()

    # Extract the children (posts) from the response
    children = data.get('data', {}).get('children', [])

    # Append the titles to the hot_list
    for child in children:
        title = child.get('data', {}).get('title', '')
        hot_list.append(title)

    # Check if there are more pages (pagination)
    after = data.get('data', {}).get('after', None)
    if after:
        # Recursively call the function with the 'after' parameter
        return recurse(subreddit, hot_list, after)
    else:
        # No more pages, return the hot_list
        return hot_list

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        result = recurse(subreddit)

        if result is not None:
            print(len(result))
        else:
            print("None")
