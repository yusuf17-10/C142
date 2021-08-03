from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd 
import numpy as np

df2 = pd.read_csv("final.csv")
df2  = df2[df2["soup"].notna()]


count = CountVectorizer(stop_words = "english")
count_matrix = count.fit_transform(df2["soup"])



cosine_sim = cosine_similarity(count_matrix,count_matrix)

df2 = df2.reset_index()
indices = pd.Series(df2.index,index=df2["title"])

def recommendation(title):
  idx = indices[title]
  sim_scores = list(enumerate(cosine_sim[idx]))
  sim_scores = sorted(sim_scores,key = lambda x:x[1], reverse=True)
  sim_scores = sim_scores[1:11]
  movie_indices = [i[0] for i in sim_scores]
  return df2[["title","poster_link","release_date","runtime","vote_average","overview"]].iloc[movie_indices].values.tolist()
  