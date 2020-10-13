# 뉴스 데이터는 빅카인즈 API로 받은 형태 그대로 사용
"""
{'news_id': '02100201.20200917161342001',
  'title': '"물적분할시 지분 매각·합병 관여 못해…소액주주 권익 축소된다"',
  ...
  }
"""

# %%
from api_function import *


# %%
# 기업명을 퀴리로 하여 2년치 데이터 모아 뉴스 리스트 생성
def generate_news_list(company_name, published_at=("2018-10-12", "2020-10-12")):
    res = req_search_news(query=company_name, published_at=published_at)
    return res.json()['return_object']['documents']


# %%
# 특정 뉴스의 딕셔너리를 입력받아 요약문장 리턴
def news_info(news):
    return f"Title: {news['title']}\nPublished At: {news['published_at']}\nHilight: {news['hilight']}"


