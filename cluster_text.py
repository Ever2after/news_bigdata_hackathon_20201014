# %%
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import normalize
from sklearn.cluster import KMeans
from cluster_base import *


# %%
def cluster_with_text(text_lst, preprocessor=eliminate_special):
    # 데이터 전처리
    text_list = []
    for text in text_lst:
        text_list.append(preprocessor(text))

    n_clusters = len(text_list) // 10
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(text_list)
    X = normalize(X)
    kmeans = KMeans(n_clusters=n_clusters).fit(X)
    labels = kmeans.labels_
    centers = kmeans.cluster_centers_
    return labels, centers


# %%
def cluster_with_title(news_list):
    title_lst = []
    for news in news_list:
        title_lst.append(news['title'])
    labels, centers = cluster_with_text(title_lst)
    grouped = group_news_by_labels(news_list, labels)
    return grouped


