import requests
from bs4 import BeautifulSoup


def get_news(url: str, category: str):
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")
    title = doc.select("h3.tit_view")
    news_title = title[0].get_text()
    print(f"Title : {news_title}")

    date = doc.select("span.num_date")[0].get_text()
    print(f"Published : {date}")

    content_list = doc.select("div.article_view p")
    content = ""
    for p in content_list:
        content += p.get_text()
    print(f"<contents>\n{content}")

    data = {
        "category": category,
        "title": news_title,
        "content": content,
        "date": date
    }
    return data
