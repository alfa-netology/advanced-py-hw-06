import re
from tqdm import tqdm
from application import utilites


def find_articles_by_keywords(browser, articles, keywords):
    keywords_pattern = '|'.join([f"\\b{word}\\b" for word in keywords])
    find_keywords_in_preview = ()
    find_keywords_in_article = ()

    for article in tqdm(articles, desc='collect data:'):
        date = utilites.date_beautify(article.find('span', class_='post__time').text)
        link = article.find('a', class_='post__title_link').get('href')
        title = article.find('a', class_='post__title_link').text
        preview = article.find('div', class_='post__text').text.strip()
        full_text = utilites.get_article_full_text(browser, link)

        if re.search(keywords_pattern, preview, flags=re.I):
            find_keywords_in_preview += (f"<{date}> - <{title}> - <{link}>",)

        if re.search(keywords_pattern, full_text, flags=re.I):
            find_keywords_in_article += (f"<{date}> - <{title}> - <{link}>",)

    return find_keywords_in_preview, find_keywords_in_article
