# %%
from cluster_base import *
from sklearn.cluster import KMeans
from datetime import datetime
import numpy as np


# %%
def date_str_to_ymd(date_str):  # "2020-09-21T00:00:00.000+09:00" -> 2020,9,21
    pattern = r"\d{4}-\d{2}-\d{2}"
    match = re.findall(pattern, date_str)
    y = int(match[0].split("-")[0])
    m = int(match[0].split("-")[1])
    d = int(match[0].split("-")[2])
    return y, m, d


def ymd_to_score(y, m, d):  # 년월일 -> 2018년 1월 1일부터 며칠 지났는지 계산,
    time1 = datetime(2018, 1, 1)
    time2 = datetime(y, m, d)
    time_delta = time2 - time1
    return time_delta.days


def date_str_to_score(date_str):
    ymd = date_str_to_ymd(date_str)
    return ymd_to_score(ymd[0], ymd[1], ymd[2])


# %%
def cluster_with_date(news_list):
    date_list = []
    for news in news_list:
        date_list.append([date_str_to_score(news['published_at'])])
    date_list = np.array(date_list)

    n_clusters = max(len(news_list) // 5, 2)
    kmeans = KMeans(n_clusters=n_clusters).fit(date_list)
    labels, centers = kmeans.labels_, kmeans.cluster_centers_
    grouped = group_news_by_labels(news_list, labels)
    return grouped
