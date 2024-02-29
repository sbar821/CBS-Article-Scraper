import os
import requests
from bs4 import BeautifulSoup

def get_news_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    stories = []
    for story in soup.find_all('p', attrs={'class': 'sc-eb7bd5f6-0 fYAfXe'}):
        line = story.text
        stories.append({'line': line})
    return stories

def write_stories_to_file(stories, filename):
    try:
        with open(filename, 'w') as f:
            f.write('\n'.join([story['line'] for story in stories]))
    except Exception as e:
        print(f"An error occurred: {e}")
