import mechanicalsoup

from application import utilites
from application import homework

def main(url, keywords):
    browser = mechanicalsoup.StatefulBrowser()
    articles = utilites.get_articles(browser, url)
    find_in_preview, find_in_article = homework.find_articles_by_keywords(browser, articles, keywords)

    print(f'\nНайдено статей по ключевым словам в превью [{len(find_in_preview)}]:')
    print(*find_in_preview, sep='\n')

    print(f'\nНайдено статей по ключевым словам в тексте статьи [{len(find_in_article)}]:')
    print(*find_in_article, sep='\n')


if __name__ == "__main__":
    KEYWORDS = ['дизайн', 'фото', 'web', 'python']
    source_url = 'https://habr.com/ru/all/'
    main(source_url, KEYWORDS)
