from datetime import datetime as dt
from datetime import timedelta

import mechanicalsoup

def date_beautify(article_date):
    today = str(dt.date(dt.now()))
    yesterday = str(dt.date(dt.now()) - timedelta(days=1))
    return article_date.replace('сегодня', today).replace('вчера', yesterday)

def get_articles(browser, url):
    browser.open(url)
    page = browser.get_current_page()
    return page.find_all('article', class_='post post_preview')

def get_article_full_text(browser, link):
    browser.open(link)
    return browser.get_current_page().find('div', class_='post__text').text
