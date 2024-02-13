
import requests
from bs4 import BeautifulSoup
import csv

def get_news_data(url):
    response = requests.get(url, timeout=600000)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    news_data = []

    # Extract information from the current page
    articles = soup.find_all('div', class_='col_l_12')
    # for article in articles:
    #     heading = article.find('figcaption',class_='')
    #     # //description = article.find('div', class_='w_description').text.strip()
    #     article_url = article.find('a', href=True)
        
    #     news_data.append({
    #         'heading': heading,
    #         # 'description': description,
    #         'url': article_url
    #     })
    for article in articles:
            image_elem = article.find('img')
            article_url_elem = article.find('a')
            figcaption_elem = article.find('figcaption')

        # Check if elements are found before accessing their attributes
            if image_elem and article_url_elem and figcaption_elem:
               image_src = image_elem.get('src', '')
               article_url = article_url_elem.get('href', '')
               figcaption_content = figcaption_elem.text.strip()
            
            news_data.append({
                'image_src': image_src,
                'url': article_url,
                'figcaption': figcaption_content
            })

    return news_data

def crawl_website(base_url, num_pages):
    all_news = []

    for page in range(1, num_pages + 1):
        url = f"{base_url}/{page}"
        news_data = get_news_data(url)
        all_news.extend(news_data)

    return all_news

def write_to_csv(data, filename):
    # fields = ['heading',  'url','img']
    fields = ['figcaption',  'url','image_src']


    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.DictWriter(csvfile, fieldnames=fields)
        csvwriter.writeheader()
        csvwriter.writerows(data)

if __name__ == "__main__":
    base_url = "https://www.gadgetsnow.com/tech-news"
    num_pages_to_crawl = 1000  # Change this to the desired number of pages
    csv_filename = "news_data2.csv"

    result = crawl_website(base_url, num_pages_to_crawl)

    # Print the result
    for i, news in enumerate(result, start=1):
        # print(f"News {i}:\nHeading: {news['heading']}\nURL: {news['url']}\n")
          print(f"News {i}:\nHeading: {news['figcaption']}\nURL: {news['url']}\n image: {news['image_src']}\n")

    # Write the result to a CSV file
    write_to_csv(result, csv_filename)
    print(f"Results written to {csv_filename}")
