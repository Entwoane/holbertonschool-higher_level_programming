#!/usr/bin/python3
"""
This module interacts with the JSONPlaceholder API to fetch and process posts.

It provides functionality to retrieve posts, print their titles, and save the
post data to a CSV file. The module uses the requests library for API
interactions and the csv module for file operations.
"""


import requests
import csv

url = 'https://jsonplaceholder.typicode.com/posts'


def fetch_and_print_posts():
    """
    Fetch posts from the JSONPlaceholder API and print their titles.

    This function sends a GET request to the API, checks for a successful
    response (status code 200), and then prints the title of each post.
    If the request fails, no output is produced.

    Returns:
        None
    """
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Status Code: {response.status_code}")
        r_json = response.json()
        for post in r_json:
            print(post['title'])


def fetch_and_save_posts():
    """
    Fetch posts from the JSONPlaceholder API and save them to a CSV file.

    This function retrieves posts from the API, extracts the 'id', 'title',
    and 'body' fields from each post, and writes this data to a CSV file
    named 'posts.csv'. If the API request fails, the function will not
    create or modify the CSV file.

    Returns:
        None
    """
    response = requests.get(url)
    if response.status_code == 200:
        posts = response.json()
        fields = ['id', 'title', 'body']
        struct_fields = [{field: post[field] for field in fields}
                         for post in posts]
        with open('posts.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()
            writer.writerows(struct_fields)
