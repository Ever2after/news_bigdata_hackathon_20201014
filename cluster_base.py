# %%
import re


# %%
# 공통 함수, 텍스트 전처리 방식
def eliminate_special(sentence):  # 특수문자 제거
    sentence = re.sub('[^가-힣ㄱ-ㅎㅏ-ㅣa-zA-Z0-9]', ' ', sentence)
    return sentence


# 기사 끝에 기자랑 이메일 나오는 것도 지우면 좋을 듯

# %%
# 공통 함수, label을 기반으로 뉴스를 묶어서 리턴
# [n1, n2, n3, .. ] -> [[n1,n2],[n3], ...]
def group_news_by_labels(news_list, labels):
    temp_dict = {}
    for i in range(len(news_list)):
        news, label = news_list[i], labels[i]
        if label in temp_dict.keys():
            temp_dict[label].append(news)
        else:
            temp_dict[label] = [news]

    grouped_news = []
    for key in temp_dict.keys():
        grouped_news.append(temp_dict[key])

    return grouped_news