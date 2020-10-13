# %%
from class_def import *
from api_function import *
from cluster_text import *
from cluster_time import *
from excel_save import *

# %%
company_name = "삼양옵틱스"  # 분석할 기업명 선택
news_list = generate_news_list(company_name)  # 해당 기업의 2년치 뉴스 가져와서 리스트에 저장
print(f"Length: {len(news_list)}")
print(news_info(news_list[0]))

# %%
c_title = cluster_with_title(news_list)  # title 기반 text_clustering 후 결과 저장
print(f"NumofCluster: {len(c_title)}")

# %%
save_dir = "C://Users//HasunSong//PycharmProjects//news_bigdata_hackathon//result_20201014.xlsx"  # 엑셀 파일에 저장
save_as_excel(company_name, c_title, save_dir)

# %%
c_title_time = []
for i in range(len(c_title)):  # title 기반 text_clustering 된 각각을 다시 발행일 기준으로 time_clustering
    if len(c_title[i]) > 3:
        temp = cluster_with_date(c_title[i])
        c_title_time.append(temp)
    else:
        c_title_time.append([c_title[i]])

# %%
save_as_excel(company_name, c_title_time, save_dir)  # 시트 하나 추가해서 그 결과도 엑셀 파일에 저장,