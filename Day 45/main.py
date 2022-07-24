from bs4 import BeautifulSoup
import requests

response = requests.get(url = "https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
article_tag = soup.find_all(name = "a", class_ = "titlelink")
article_text = [article.getText() for article in article_tag] 
article_link = [link['href'] for link in article_tag]

article_upvote_tag = soup.find_all(name = "span", class_ = "score")
article_upvote = [int(article.getText().split()[0]) for article in article_upvote_tag]

largest_number = max(article_upvote)
largest_index = article_upvote.index(largest_number)

print(article_text[largest_index])
print(article_link[largest_index])


