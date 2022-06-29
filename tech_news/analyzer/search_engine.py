from tech_news.database import search_news
from datetime import datetime


def return_tuple(list):
    return [(noticia["title"], noticia["url"]) for noticia in list]


# Requisito 6
def search_by_title(title):
    list = search_news({"title":  {"$regex": title, "$options": "i"}})
    return return_tuple(list)


# Requisito 7
def search_by_date(date):
    try:
        datetime.strptime(date, '%Y-%m-%d')
        list = search_news({"timestamp":  {"$regex": date}})
        return return_tuple(list)
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    list = search_news({"sources":  {"$regex": source, "$options": "i"}})
    return return_tuple(list)


# Requisito 9
def search_by_category(category):
    list = search_news({"categories":  {"$regex": category, "$options": "i"}})
    return return_tuple(list)
