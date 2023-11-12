import requests

def recurse(subreddit, hot_list=None, after=None):
    if hot_list is None:
        hot_list = []

    headers = {'User-Agent': 'MyBot/1.0 (by /u/gihozoi)'}  # Add your Reddit username here

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

