#!/usr/bin/python3
"""
This script fetches posts from a public API (https://jsonplaceholder.typicode.com/posts)
and either prints their titles to the console or saves them to a CSV file.

Functions:
    fetch_and_print_posts() -- Fetches posts and prints their titles to stdout.
    fetch_and_save_posts()  -- Fetches posts and saves selected fields (id, title, body) to a CSV file.
"""


import requests
import csv

def fetch_and_print_posts():
    """
    Fetches posts from the API and prints each post's title.
    """
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    print("Status Code: ".format(), response.status_code)
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])
def fetch_and_save_posts():
    """
    Fetches posts from the API and writes selected fields (id, title, body)
    to a CSV file named 'posts.csv'.
    """
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    if response.status_code == 200:
        posts = response.json()
        csv_data = []
        for post in posts:
            post_key = {
                "id": post["id"],
                "title": post["title"],
                "body": post["body"],
            }
            csv_data.append(post_key)
            with open("posts.csv", "w", newline="") as f:
                fieldname = ['id', 'title', 'body']
                writer = csv.DictWriter(f, filesnames=fieldname)
                writer.writeheader()
                writer.writerows(csv_data)
        return csv_data
