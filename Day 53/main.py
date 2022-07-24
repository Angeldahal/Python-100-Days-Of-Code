from bs4 import BeautifulSoup
import requests
spotify_headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

response = requests.get(url = 'https://www.zillow.com/san-diego-ca/rentals/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22San%20Diego%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-117.62945579492188%2C%22east%22%3A-116.58850120507813%2C%22south%22%3A32.488810628093475%2C%22north%22%3A33.15929514301838%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A54296%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A663680%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A3000%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D', headers= spotify_headers)

soup = BeautifulSoup(response.text, 'html.parser')
price_tag_list = soup.find_all('div',class_ = 'list-card-price')
price_list = [price.text for price in price_tag_list]
print(price_list)

apartment_link_tag_list = soup.find_all('a', class_ = 'list-card-link')
apartment_links = [link["href"] for link in apartment_link_tag_list]
main_link = 'https://www.zillow.com'
for link in apartment_links:
    if main_link not in link:
        link = main_link + link
print(apartment_links)


