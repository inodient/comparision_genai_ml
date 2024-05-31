# -*- coding: utf-8 -*-
"""merge_news

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Oed05LwTh1A6OwwHPyi2raeNzShijwGe
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set( style="whitegrid" )

news = pd.read_excel( "/content/drive/MyDrive/Colab Notebooks/Paper/newsdata/NewsResult_20230101-20230115.xlsx" )

news = pd.concat([news, pd.read_excel( "/content/drive/MyDrive/Colab Notebooks/Paper/newsdata/NewsResult_20230116-20230131.xlsx" )])

news = pd.concat([news, pd.read_excel( "/content/drive/MyDrive/Colab Notebooks/Paper/newsdata/NewsResult_20230201-20230214.xlsx" )])

news = pd.concat([news, pd.read_excel( "/content/drive/MyDrive/Colab Notebooks/Paper/newsdata/NewsResult_20230215-20230228.xlsx" )])

news = pd.concat([news, pd.read_excel( "/content/drive/MyDrive/Colab Notebooks/Paper/newsdata/NewsResult_20230301-20230315.xlsx" )])

news = pd.concat([news, pd.read_excel( "/content/drive/MyDrive/Colab Notebooks/Paper/newsdata/NewsResult_20230316-20230328.xlsx" )])

news = pd.concat([news, pd.read_excel( "/content/drive/MyDrive/Colab Notebooks/Paper/newsdata/NewsResult_20230329-20230331.xlsx" )])

news = pd.concat([news, pd.read_excel( "/content/drive/MyDrive/Colab Notebooks/Paper/newsdata/NewsResult_20230401-20230415.xlsx" )])

news = pd.concat([news, pd.read_excel( "/content/drive/MyDrive/Colab Notebooks/Paper/newsdata/NewsResult_20230416-20230430.xlsx" )])

news = pd.concat([news, pd.read_excel( "/content/drive/MyDrive/Colab Notebooks/Paper/newsdata/NewsResult_20230501-20230515.xlsx" )])

news = pd.concat([news, pd.read_excel( "/content/drive/MyDrive/Colab Notebooks/Paper/newsdata/NewsResult_20230516-20230531.xlsx" )])

news = pd.concat([news, pd.read_excel( "/content/drive/MyDrive/Colab Notebooks/Paper/newsdata/NewsResult_20230601-20230615.xlsx" )])

news = pd.concat([news, pd.read_excel( "/content/drive/MyDrive/Colab Notebooks/Paper/newsdata/NewsResult_20230616-20230630.xlsx" )])

news = pd.concat([news, pd.read_excel( "/content/drive/MyDrive/Colab Notebooks/Paper/newsdata/NewsResult_20230701-20230715.xlsx" )])

news = pd.concat([news, pd.read_excel( "/content/drive/MyDrive/Colab Notebooks/Paper/newsdata/NewsResult_20230716-20230731.xlsx" )])

news = pd.concat([news, pd.read_excel( "/content/drive/MyDrive/Colab Notebooks/Paper/newsdata/NewsResult_20230801-20230815.xlsx" )])

news = pd.concat([news, pd.read_excel( "/content/drive/MyDrive/Colab Notebooks/Paper/newsdata/NewsResult_20230816-20230831.xlsx" )])

news = pd.concat([news, pd.read_excel( "/content/drive/MyDrive/Colab Notebooks/Paper/newsdata/NewsResult_20230901-20230915.xlsx" )])

news = pd.concat([news, pd.read_excel( "/content/drive/MyDrive/Colab Notebooks/Paper/newsdata/NewsResult_20230916-20230930.xlsx" )])

news = pd.concat([news, pd.read_excel( "/content/drive/MyDrive/Colab Notebooks/Paper/newsdata/NewsResult_20231001-20231015.xlsx" )])

news = pd.concat([news, pd.read_excel( "/content/drive/MyDrive/Colab Notebooks/Paper/newsdata/NewsResult_20231016-20231027.xlsx" )])

news = pd.concat([news, pd.read_excel( "/content/drive/MyDrive/Colab Notebooks/Paper/newsdata/NewsResult_20231028-20231031.xlsx" )])

news = pd.concat([news, pd.read_excel( "/content/drive/MyDrive/Colab Notebooks/Paper/newsdata/NewsResult_20231101-20231114.xlsx" )])

news = pd.concat([news, pd.read_excel( "/content/drive/MyDrive/Colab Notebooks/Paper/newsdata/NewsResult_20231115-20231127.xlsx" )])

news = pd.concat([news, pd.read_excel( "/content/drive/MyDrive/Colab Notebooks/Paper/newsdata/NewsResult_20231128-20231130.xlsx" )])

news = pd.concat([news, pd.read_excel( "/content/drive/MyDrive/Colab Notebooks/Paper/newsdata/NewsResult_20231201-20231215.xlsx" )])

news = pd.concat([news, pd.read_excel( "/content/drive/MyDrive/Colab Notebooks/Paper/newsdata/NewsResult_20231216-20231231.xlsx" )])

"""###. ETL"""

news["date"] = pd.to_datetime( news["일자"], format='%Y%m%d' )
news["sentiment"] = "-"

news.columns = ['indicator', 'date_text', 'company', 'reporter', 'title', 'category1', 'category2', 'category3',
       'accident1', 'accident2', 'accident3', 'people', 'location', 'organization', 'keyword',
       'characteristic', 'content', 'URL', 'excepted', 'date', 'sentiment']

news["excepted"] = news["excepted"].astype(str)
news["excepted"]

news = news[news["excepted"] == "nan"]
news["date"].count()

news = news.reset_index()

news

"""###. Weekday"""

news['weekday'] = news['date'].dt.weekday

# 주중(0~4)인 행만 선택
news_weekday = news[news['weekday'].isin([0, 1, 2, 3, 4])]

news_weekday.drop( columns=["weekday"], inplace=True )

news_weekday = news_weekday.reset_index()

"""###. Save to CSV"""

news.to_csv( "/content/drive/MyDrive/Colab Notebooks/Paper/newsdata/news.csv", index=False )

news_weekday.to_csv( "/content/drive/MyDrive/Colab Notebooks/Paper/newsdata/news_weekday.csv", index=False )



import pandas as pd

news_weekday = pd.read_csv( "/content/drive/MyDrive/Colab Notebooks/Paper/newsdata/news_weekday.csv" )

len( news_weekday )











"""##. Wide News"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set( style="whitegrid" )

news = pd.read_excel( "/content/drive/MyDrive/Colab Notebooks/Paper/wide_news/NewsResult_20230101-20230131.xlsx" )

news = pd.concat([news, pd.read_excel( "/content/drive/MyDrive/Colab Notebooks/Paper/wide_news/NewsResult_20230201-20230228.xlsx" )])

news = pd.concat([news, pd.read_excel( "/content/drive/MyDrive/Colab Notebooks/Paper/wide_news/NewsResult_20230301-20230331.xlsx" )])

news = pd.concat([news, pd.read_excel( "/content/drive/MyDrive/Colab Notebooks/Paper/wide_news/NewsResult_20230401-20230430.xlsx" )])

news = pd.concat([news, pd.read_excel( "/content/drive/MyDrive/Colab Notebooks/Paper/wide_news/NewsResult_20230501-20230531.xlsx" )])

news = pd.concat([news, pd.read_excel( "/content/drive/MyDrive/Colab Notebooks/Paper/wide_news/NewsResult_20230601-20230630.xlsx" )])

news = pd.concat([news, pd.read_excel( "/content/drive/MyDrive/Colab Notebooks/Paper/wide_news/NewsResult_20230701-20230731.xlsx" )])

news = pd.concat([news, pd.read_excel( "/content/drive/MyDrive/Colab Notebooks/Paper/wide_news/NewsResult_20230801-20230831.xlsx" )])

news = pd.concat([news, pd.read_excel( "/content/drive/MyDrive/Colab Notebooks/Paper/wide_news/NewsResult_20230901-20230930.xlsx" )])

news = pd.concat([news, pd.read_excel( "/content/drive/MyDrive/Colab Notebooks/Paper/wide_news/NewsResult_20231001-20231031.xlsx" )])

news = pd.concat([news, pd.read_excel( "/content/drive/MyDrive/Colab Notebooks/Paper/wide_news/NewsResult_20231101-20231130.xlsx" )])

news = pd.concat([news, pd.read_excel( "/content/drive/MyDrive/Colab Notebooks/Paper/wide_news/NewsResult_20231201-20231231.xlsx" )])



news = news.sort_values( by="일자" )

news["date"] = pd.to_datetime( news["일자"], format='%Y%m%d' )
news["sentiment"] = "-"

news.columns = ['indicator', 'date_text', 'company', 'reporter', 'title', 'category1', 'category2', 'category3',
       'accident1', 'accident2', 'accident3', 'people', 'location', 'organization', 'keyword',
       'characteristic', 'content', 'URL', 'excepted', 'date', 'sentiment']

news["excepted"] = news["excepted"].astype(str)
news["excepted"]

news = news[news["excepted"] == "nan"]
news["date"].count()

news = news.reset_index(drop=True)

news['weekday'] = news['date'].dt.weekday

# 주중(0~4)인 행만 선택
news_weekday = news[news['weekday'].isin([0, 1, 2, 3, 4])]

news_weekday.drop( columns=["weekday"], inplace=True )

news_weekday = news_weekday.reset_index(drop=True)

news_weekday

news_weekday.to_csv( "/content/drive/MyDrive/Colab Notebooks/Paper/wide_news/news_weekday.csv", index=False )


















