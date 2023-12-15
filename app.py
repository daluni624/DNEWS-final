# Streamlit Library - Python WEBsite (ONLY SIMPLE WEB)

import streamlit as st
from datetime import datetime
from src.collector import news_collector

news_category = {
    "society": "사회",
    "politics": "정치",
    "economic": "경제",
    "foreign": "국제",
    "culture": "문화",
    "sports": "스포츠",
    "digital": "IT"
}

st.set_page_config(
    page_title="기사 수집 마법사",
    page_icon="./image/favicon_01.png"
)

st.title(":blue[다음] 뉴스 기사 수집 마법사")
st.text("날짜와 분야를 입력하면 뉴스를 알아서 수집해줘요!")
st.text("by. starjae(이성재)")


@st.cache_data
def convert_df(df):
    return df.to_csv(index=False, encoding="utf-8")


flag = False
with st.form(key="form"):
    category = st.text_input("카테고리를 입력해주세요!").strip()
    date = st.text_input(f'날짜를 입력해주세요! (ex. {datetime.now().strftime("%Y%m%d")})').strip()
    submitted = st.form_submit_button("시작")
    if submitted:
        cmp_date = datetime.now().strftime("%Y%m%d")
        tmp_date = date
        if int(tmp_date) > int(cmp_date):
            st.write("미래의 날짜는 입력이 안돼요!")
        if category in list(news_category.keys()):
            aim_date = datetime(int(date) // 10000, int(date) % 10000 // 100, int(date) % 10000 % 100).strftime("%Y년 %m월 %d일")
            st.write(f'다루니가 열심히 {aim_date}의 "{news_category[category]}"분야 뉴스를 수집하고 있어요!'
                     f'작업이 오래 걸리더라도 잠시만 기다려 주세요!')
            df_news, count = news_collector(category, date)
            csv = convert_df(df_news)
            flag = True
        else:
            st.write("카테고리가 잘못되었어요! 다시 입력해주세요!")

if flag:
    st.write(f'"{news_category[category]}" 뉴스 {count}건 수집 완료!')
    now = datetime.now().strftime("%Y_%m_%d_%H%M%S")
    down = st.download_button(
        label="저장",
        data=csv,
        mime="text/csv",
        file_name=f"{news_category[category]}_news_{now}"
    )
    if down:
        st.write("메모장에서 열어야 파일이 깨지지 않아요.")
