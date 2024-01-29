import os
import requests
from bs4 import BeautifulSoup

def get_url_from_file(file):
    with open(file, 'r') as f:
        urls = [line.strip() for line in f.readlines()]
    if not urls:
        raise ValueError("URLs not found in file")
    return urls

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

def main():
    url_filename = 'url.txt'
    try:
        urls = get_url_from_file(url_filename)
    except Exception as e:
        print(f"An error occurred while getting the URLs from the file: {e}")
        return

    for url in urls[:5]:
        stories = get_news_from_url(url)
        filename = f'story{urls.index(url) + 1}.txt'
        write_stories_to_file(stories, filename)

if __name__ == "__main__":
    main()