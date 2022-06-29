from tech_news.database import db


# Requisito 10
def top_5_news():
    news = list(db.news.aggregate([
        {"$project": {
            "_id": False,
            "title": "$title",
            "url": "$url",
            "popularity": {"$sum": ["$shares_count", "$comments_count"]},
        }},
        {"$sort": {"popularity": -1}},
        {"$limit": 5},
    ]))
    return [(noticia["title"], noticia["url"]) for noticia in news]


# Requisito 11
def top_5_categories():
    categories = list(db.news.aggregate([
        {"$unwind": "$categories"},
        {"$group": {
            "_id": "$categories",
            "count": {"$sum": 1}
        }},
        {"$sort": {"count": -1, "_id": 1}},
        {"$limit": 5},
    ]))
    return [category["_id"] for category in categories]
