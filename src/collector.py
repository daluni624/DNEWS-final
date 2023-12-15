import requests  # extract source code
from bs4 import BeautifulSoup  # Select wanted information
from src.service_news import get_news
import pandas as pd


def news_collector(category, date, page=1, cnt=0):
    collect_list = []  # only used for converting dataframe
    while True:
        url = f"https://news.daum.net/breakingnews/{category}?page={page}&regDate={date}"
        result = requests.get(url)
        if result.status_code == 200:
            doc = BeautifulSoup(result.text, "html.parser")
            lists_url = doc.select("ul.list_news2 a.link_txt")

            if len(lists_url) == 0:
                break

            for url in lists_url:
                cnt += 1
                print(cnt+1, "=" * 50)
                data = get_news(url["href"], category)  # get title, contents, publish date of article.
                collect_list.append(data)
        else:
            print("경로 오류. 다시 확인하세요.")
        page += 1
    col_name = ["category", "title", "content", "date"]
    df_news = pd.DataFrame(collect_list, columns=col_name)
    return df_news, cnt  # tuple
