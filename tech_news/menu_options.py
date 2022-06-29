from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_source,
    search_by_category,
)
from tech_news.analyzer.ratings import top_5_news, top_5_categories


def option_0():
    size = input(
        "Digite quantas notícias serão buscadas:\n"
    )
    return get_tech_news(int(size))


def option_1():
    title = input(
        "Digite o título:\n"
    )
    return search_by_title(title)


def option_2():
    date = input(
        "Digite a data no formato aaaa-mm-dd:\n"
    )
    return search_by_date(date)


def option_3():
    source = input(
        "Digite a fonte:\n"
    )
    return search_by_source(source)


def option_4():
    category = input(
        "Digite a categoria:\n"
    )
    return search_by_category(category)


def option_5():
    return top_5_news()


def option_6():
    return top_5_categories()


def option_7():
    return print("Encerrando script")


menu_options_dict = {
    "0": option_0,
    "1": option_1,
    "2": option_2,
    "3": option_3,
    "4": option_4,
    "5": option_5,
    "6": option_6,
    "7": option_7,
}


class Menu_Options:
    def option_0():
        size = input(
            "Digite quantas notícias serão buscadas:\n"
        )
        return get_tech_news(size)

    def option_1():
        title = input(
            "Digite o título:\n"
        )
        return search_by_title(title)

    def option_2():
        date = input(
            "Digite a data no formato aaaa-mm-dd:\n"
        )
        return search_by_date(date)

    def option_3():
        source = input(
            "Digite a fonte:\n"
        )
        return search_by_source(source)

    def option_4():
        category = input(
            "Digite a categoria:\n"
        )
        return search_by_category(category)

    def option_5():
        return top_5_news()

    def option_6():
        return top_5_categories()

    def option_7():
        return print("Encerrando script")
