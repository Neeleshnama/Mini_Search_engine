import requests
from bs4 import BeautifulSoup

def get_article_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a', {'class': 'wclink2'})
    article_links = [link['href'] for link in links]
    return article_links

def main():
    base_url = 'https://www.hindustantimes.com/science/page/'

    max_pages = 3  # Set the maximum number of pages to crawl

    all_article_links = []
    for page_num in range(1, max_pages + 1):
        current_url = base_url + str(page_num)
        article_links = get_article_links(current_url)
        all_article_links.extend(article_links)

    for index, link in enumerate(all_article_links, start=1):
        print(f"Article {index}: {link}")

if __name__ == "__main__":
    main()
