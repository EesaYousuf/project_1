""" Web Scraper to Fetch News Headlines
Uses requests and BeautifulSoup to scrape headlines from a news website"""
import requests
from bs4 import BeautifulSoup

def fetch_headlines():
    url = 'https://news.ycombinator.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    headlines = soup.find_all('a', class_='storylink')
    print("Top News Headlines:\n")
    for idx, headline in enumerate(headlines[:10], 1):
        print(f"{idx}. {headline.get_text()}")

if __name__ == '__main__':
    fetch_headlines()
