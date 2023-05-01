import requests
from bs4 import BeautifulSoup
#website Url
URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
#get all movie data from website
all_movies = soup.find_all(name='div',class_='jsx-4245974604')
#get all movie names
movie_titles = [movie.getText() for movie in all_movies]
#Reverse the list order
movies = movie_titles[::-1]

#create file
with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")