import csv

all_movies = []
liked_movies = []
not_liked_movies = []
did_not_watch = []

with open('final.csv',encoding = "utf8") as f:
    reader = csv.reader(f)
    for i in reader:
        all_movies.append(i)

all_movies = all_movies[1:]
