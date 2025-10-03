import requests as req
from bs4 import BeautifulSoup

class BestMovies:
    def __init__(self,year,ratings,language,genre):
        self.year = year
        self.ratings = ratings
        self.language = language
        self.genre = genre
        self.url = f'https://www.imdb.com/search/title/?release_date={self.year}-01-01,{self.year}-12-31&user_rating={self.ratings},10&languages={self.language}&genres={self.genre}'
        self.headers = {"User-Agent" : "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N)"
                        "AppleWebKit/537.36 (KHTML, like Gecko)"
                        " Chrome/140.0.0.0 Mobile Safari/537.36 Edg/140.0.0.0"}
        self.response = req.get(url = self.url , headers = self.headers).text
        self.soup = BeautifulSoup(self.response , "lxml")

    def display(self):
        print(self.url)
        movie_names = self.soup.find_all("h3" , {"class" : "ipc-title__text ipc-title__text--reduced"})
        movie_ratings = self.soup.find_all("span" , {"class" : "ipc-rating-star--rating"})
        all_a = self.soup.find_all("div" , {"class" : "sc-ec40e84d-0 dTHKNo"})
        for i in all_a:
            print(i.find("h3" , {"class" : "ipc-title__text ipc-title__text--reduced"}).text)
            print(i.find("span" , {"class" : "ipc-rating-star--rating"}).text ) if (i.find("span" , {"class" : "ipc-rating-star--rating"})) else "not rated"
            print()
year = input("Enter year : ").strip()
ratings = input("Enter minimum rating : ").strip()
language = input("Enter language : ").strip()
genre = input("Enter Genre : ").strip()
print()

obj = BestMovies(year,ratings,language,genre)

print(f"Top {genre} movies of {year} with rating above {ratings} in {language}")
print()
obj.display()
