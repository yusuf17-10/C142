import csv 
all_movies = []
all_movies_links = []
with open('movies.csv',encoding = "utf8") as f:
    reader = csv.reader(f)
    for i in reader:
        all_movies.append(i)

headers = all_movies[0]
headers.append("poster_link")

all_movies = all_movies[1:]

with open("final.csv","w",encoding="utf8") as f1:
    csv_wiriter = csv.writer(f1)
    csv_wiriter.writerow(headers)
f1.close()
with open("movie_links.csv",encoding="utf8") as f:
    reader = csv.reader(f)
    for i in reader:
        all_movies_links.append(i)

all_movies_links = all_movies_links[1:]

for movie_item in all_movies:
    poster_found = any(movie_item[8] in movie_link_items for movie_link_items in all_movies_links)
    if poster_found:
        for movie_link_item in all_movies_links:
            if movie_item[8] == movie_link_item[0]:
                movie_item.append(movie_link_item[1])
                if len(movie_item) == 28:
                    with open("final.csv","a+",encoding="utf8") as f3:
                        csv_wiriter = csv.writer(f3)
                        csv_wiriter.writerow(movie_item)




