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
    points = []
    for news in news_list:
        points.append([date_str_to_score(news['published_at']),0])
    points = np.array(points)

    #k값을 1부터 k_max까지 돌려보고 최소의 WSS score를 탐색한다.
    k_max = max(len(news_list)//2, 1)+1
    
    for k in range(1, k_max, 1):
      kmeans = KMeans(n_clusters = k).fit(points)
      centroids = kmeans.cluster_centers_
      labels = kmeans.labels_
      #wss 계산과정
      pred_clusters = kmeans.predict(points)
      curr_sse = 0
      
      # calculate square of Euclidean distance of each point from its cluster center and add to current WSS
      for i in range(len(news_list)):
        curr_center = centroids[pred_clusters[i]]
        curr_sse += (points[i, 0] - curr_center[0]) ** 2 + (points[i, 1] - curr_center[1]) ** 2
      #값 리스트에 저장  
      #날짜가 같은 기사끼리 명확하게 군집화되면 이 점수가 0에 매우 급격히 수렴한다. 
      #따라서  0.001 이하가 되는 최초의 k을 클러스터 수로 지정하고 label과 centroid를 return한다.
      if curr_sse<0.0001:
          grouped = group_news_by_labels(news_list, labels)
          return grouped
      #0.0001이하가 되지 않고 끝에 도달할 경우 그냥 마지막 label, centroid를 return
      if k==k_max-1:
          grouped = group_news_by_labels(news_list, labels)
          return grouped
