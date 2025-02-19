#!/usr/bin/python3
"""
This module fetches and processes posts from JSONPlaceholder API.
It provides functions to print post titles and save posts to a CSV file.
"""


import requests
import csv

url = 'https://jsonplaceholder.typicode.com/posts'


def fetch_and_print_posts():
    """
    Fetches posts from the API and prints their titles.
    """
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Satus Code: {response.status_code}")
        r_json = response.json()
        for post in r_json:
            print(post['title'])


def fetch_and_save_posts():
    """
    Fetches posts from the API and saves them to a CSV file.
    """
    response = requests.get(url)
    if response.status_code == 200:
        posts = response.json()
        fields = ['id', 'title', 'body']
        struct_fields = [{field: post[field] for field in fields}
                         for post in posts]
    with open('posts.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(struct_fields)
