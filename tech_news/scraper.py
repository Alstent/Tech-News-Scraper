from time import sleep
import requests
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url, timeout=1):
    try:
        sleep(1)
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
    except (requests.HTTPError, requests.ReadTimeout):
        return None
    else:
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    content = Selector(html_content)
    urls = []

    for tech_news in content.css("div.tec--list__item"):
        url = tech_news.css("a[href*=https]::attr(href)").get()
        urls.append(url)
    return urls


# Requisito 3
def scrape_next_page_link(html_content):
    content = Selector(html_content)
    next_page_url = content.css("a[href*='page']::attr(href)").get()
    return next_page_url


def filter_numbers(string):
    if not string:
        return 0
    list = string.split()
    for i in list:
        if i.isdigit():
            return int(i)


# Requisito 4
def scrape_noticia(html_content):
    content = Selector(html_content)
    url = content.css("meta[property*='url']::attr(content)").get()
    title = content.css("h1[id*='title']::text").get()
    # timestamp = content.css("time[id*='date']::attr(datetime)").get()
    timestamp = content.css("time#js-article-date::attr(datetime)").get()
    writer = content.css("div[class*='author'] p *::text").get()
    if not writer:
        writer = content.css("a[href*=autor]::text").get()
    shares_count = content.css("div[class*='toolbar__item']::text").get()
    comments_count = content.css("button[id*='comm']::attr(data-count)").get()
    summary = content.css(
        ".tec--article__body > p:first-child *::text"
    ).getall()
    sources = content.css(
        ".z--mb-16 h2.z--text-base.z--font-semibold ~ div a.tec--badge::text"
    ).getall()
    categories = content.css("div[id*='categories'] a::text").getall()
    noticia = {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer.strip() if writer else writer,
        "shares_count": filter_numbers(shares_count),
        "comments_count": int(comments_count) if comments_count else 0,
        "summary": "".join(summary),
        "sources": [source.strip() for source in sources],
        "categories": [category.strip() for category in categories],
    }
    return noticia


# Requisito 5
def get_tech_news(amount):
    news = []
    next_page = "https://www.tecmundo.com.br/novidades"
    while len(news) < amount:
        html = fetch(next_page)
        for news_url in scrape_novidades(html):
            if len(news) == amount:
                break
            content = fetch(news_url)
            news.append(scrape_noticia(content))
        next_page = scrape_next_page_link(html)
        if not next_page:
            break
    create_news(news)
    return news
