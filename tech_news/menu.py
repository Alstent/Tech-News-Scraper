import sys
# from tech_news.menu_options import menu_options_dict4
# from tech_news.menu_options import Menu_Options
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_source,
    search_by_category,
)
from tech_news.analyzer.ratings import top_5_news, top_5_categories


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


# Requisito 12
def analyzer_menu():
    option = input("""
        Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por fonte;
 4 - Buscar notícias por categoria;
 5 - Listar top 5 notícias;
 6 - Listar top 5 categorias;
 7 - Sair.
 """)
    try:
        getattr(Menu_Options, f"option_{option}")()
        # Menu_Options["op"]()
    except AttributeError:
        sys.stderr.write("Opção inválida\n")
