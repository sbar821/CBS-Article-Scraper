import os
import requests
from bs4 import BeautifulSoup
from module_1.mod1_funct1 import get_url_from_file, get_raw_from_file
from module_2.mod2_funct1 import write_stories_to_file, get_news_from_url
def main():
    url_filename = 'url.txt'
    try:
        urls = get_url_from_file(url_filename)
    except Exception as e:
        print(f"An error occurred while getting the URLs from the file: {e}")
        return

    for url in urls[:5]:
        raw = get_raw_from_file(url)
        rawFile = f'Data/raw/raw{urls.index(url) + 1}.txt'
        write_stories_to_file(raw,rawFile)
        stories = get_news_from_url(url)
        filename = f'Data/processed/story{urls.index(url) + 1}.txt'
        write_stories_to_file(stories, filename)

if __name__ == "__main__":
    main()