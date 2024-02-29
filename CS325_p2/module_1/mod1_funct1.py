import os
import requests
from bs4 import BeautifulSoup

def get_url_from_file(file):
    with open(file, 'r') as f:
        urls = [line.strip() for line in f.readlines()]
    if not urls:
        raise ValueError("URLs not found in file")
    return urls

def get_raw_from_file(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    stories = []
    for story in soup.find_all('p'):
        line = story.text
        stories.append({'line': line})
    return stories