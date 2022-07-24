from bs4 import BeautifulSoup
import requests

# date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
date= "2022-06-17"
spotify_headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

response = requests.get("https://www.billboard.com/charts/hot-100/"+ date, headers = spotify_headers)

soup = BeautifulSoup(response.text, 'html.parser')
song_names_list = soup.find_all("h3",class_ = "c-title")
print(song_names_list)
