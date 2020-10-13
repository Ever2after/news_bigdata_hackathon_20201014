# %%
# 빅카인즈 API를 함수로 정리해놓음.
import json
import requests


def req_search_news(query="삼성전자", published_at=("2018-10-12", "2020-10-12"),
                    provider=[], category=[], category_incident=[], byline="", provider_subject=[],
                    subject_info=[""], subject_info1=[""],subject_info2=[""],subject_info3=[""], subject_info4=[""],
                    sort={"date": "desc"}, hilight=200, return_from=0, return_size=100000,
                    fields=["byline", "category", "category_incident", "provider_news_id"]):
    url = "http://tools.kinds.or.kr:8888/search/news"
    req = {
        "access_key": "8e754d1c-d967-49dd-ae0b-c22ed25fb5aa",
        "argument": {
            "query": query,
            "published_at": {"from": published_at[0], "until": published_at[1]},
            "provider": provider,
            "category": category,
            "category_incident": category_incident,
            "byline": byline,
            "provider_subject": provider_subject,
            "subject_info": subject_info,
            "subject_info1": subject_info1,
            "subject_info2": subject_info2,
            "subject_info3": subject_info3,
            "subject_info4": subject_info4,
            "sort": sort,
            "hilight": hilight,
            "return_from": return_from,
            "return_size": return_size,
            "fields": fields
        }
    }
    res = requests.post(url, data=json.dumps(req))
    return res


def req_search_detail(news_ids=["01500701.2015083110018412570"],
                      fields=["content", "byline", "category", "category_incident", "images", "provider_subject",
                              "provider_news_id", "publisher_code"]):
    url = "http://tools.kinds.or.kr:8888/search/news"
    req = {
        "access_key": "8e754d1c-d967-49dd-ae0b-c22ed25fb5aa",
        "argument": {
            "news_ids": news_ids,
            "fields": fields
        }
    }
    res = requests.post(url, data=json.dumps(req))
    return res


def req_todays_issue(date="2019-01-01", provider=[]):
    url = "http://tools.kinds.or.kr:8888/issue_ranking"
    req = {
        "access_key": "8e754d1c-d967-49dd-ae0b-c22ed25fb5aa",
        "argument": {
            "date": date,
            "provider": provider
        }
    }
    res = requests.post(url, data=json.dumps(req))
    return res


def req_related_words(query="청와대", published_at=("2019-01-01", "2019-01-31"), provider=[],
                      category=[], category_incident=[], byline="",
                      provider_subject=[]):
    url = "http://tools.kinds.or.kr:8888/word_cloud"
    req = {
        "access_key": "8e754d1c-d967-49dd-ae0b-c22ed25fb5aa",
        "argument": {
            "query": query,
            "published_at": {"from": published_at[0], "until": published_at[1]},
            "provider": provider,
            "category": category,
            "category_incident": category_incident,
            "byline": byline,
            "provider_subject": provider_subject
        }
    }
    res = requests.post(url, data=json.dumps(req))
    return res


def req_keyword_trend(query="정부", published_at=("2018-01-01", "2018-12-31"), provider=[],
                      category=[], category_incident=[], byline="",
                      provider_subject=[], interval="month", normalize=False):
    url = "http://tools.kinds.or.kr:8888/time_line"
    req = {
        "access_key": "8e754d1c-d967-49dd-ae0b-c22ed25fb5aa",
        "argument": {
            "query": query,
            "published_at": {"from": published_at[0], "until": published_at[1]},
            "provider": provider,
            "category": category,
            "category_incident": category_incident,
            "byline": byline,
            "provider_subject": provider_subject,
            "interval": interval,
            "normalize": normalize
        }
    }
    res = requests.post(url, data=json.dumps(req))
    return res

"""
# %%
articles = (req_search_news().json()['return_object']['documents'])
print(len(articles))

# %%
articles = req_search_news(query="헬릭스미스", published_at=('2020-05-12', '2020-10-12'), hilight=400).json()['return_object']['documents']
print(len(articles))
print(articles[0])
"""
