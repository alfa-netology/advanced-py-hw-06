import re
import mechanicalsoup
from application import utilites


def main():
    KEYWORDS = ['дизайн', 'фото', 'web', 'python']
    keywords_pattern = '|'.join([f"\\b{word}\\b" for word in KEYWORDS])

    url = 'https://habr.com/ru/all/'
    browser = mechanicalsoup.StatefulBrowser()

    articles = utilites.get_articles(browser, url)

    find_keywords_in_preview = ()

    for article in articles:
        article_date = utilites.date_beautify(article.find('span', class_='post__time').text)
        artricle_link = article.find('a', class_='post__title_link').get('href')
        article_title = article.find('a', class_='post__title_link').text
        article_preview = article.find('div', class_='post__text').text.strip()

        if re.search(keywords_pattern, article_preview, flags=re.I):
            find_keywords_in_preview += (f"<{article_date}> - <{article_title}> - <{artricle_link}>",)

    print(*find_keywords_in_preview, sep='\n')


if __name__ == "__main__":
    main()
