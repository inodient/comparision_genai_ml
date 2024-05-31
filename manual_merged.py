# -*- coding: utf-8 -*-
"""paper_manual_merged

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JpwEm77Oa07V6tCDB8j_eRWVoEucCKwW
"""

import numpy as np
import pandas as pd

marked = pd.read_csv( "/content/drive/MyDrive/Colab Notebooks/Paper/wide_news/news_sentiment_manual coding_May2024 - Comparision.csv" )

marked["merged_sentiment"] = ""
marked["remove"] = ""

marked.columns

# temp = marked[marked["remove_grace"] != 1]
# temp = temp[temp["remove_koo"] != 1]
# temp = temp[temp["remove_kang"] != 1]

len(marked)

# marked = temp

for i in range(0, len(marked)):
  if marked.iloc[i, 2] != 1 and marked.iloc[i, 4] != 1 and marked.iloc[i, 6] != 1:

    s1 = marked.iloc[i, 3]
    s2 = marked.iloc[i, 5]
    s3 = marked.iloc[i, 7]

    print( s1, s2, s3)

    # if (s1==1. and s2==1.) or (s1==1. and s3==1.) or (s2==1. and s3==1.):
    #   sentiment = "positive"
    # elif (s1==-1. and s2==-1.) or (s1==-1. and s3==-1.) or (s2==-1. and s3==-1.):
    #   sentiment = "negative"
    # else:
    #   marked.iloc[i, 8] = "neutral"

    sentiment = ""

    if (s1 + s2 + s3) > 0:
      sentiment = "positive"
    elif (s1 + s2 + s3) < 0:
      sentiment = "negative"
    else:
      sentiment = "neutral"

    marked.iloc[i, 8] = sentiment
    print( sentiment )

  else:
    marked.iloc[i, 9] = 1

marked.to_csv( "/content/drive/MyDrive/Colab Notebooks/Paper/wide_news/news_manual_merged.csv" )

len(marked)



