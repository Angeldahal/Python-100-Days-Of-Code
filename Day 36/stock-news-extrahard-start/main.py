import requests
from twilio.rest import Client
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
stock_api_key = "EGDS5AAZ4J2OZ3L8"
news_api_key = "35e4df47f5494417b27176d5ac1f70eb"

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": stock_api_key,

}
response = requests.get(url = "https://www.alphavantage.co/query", params = stock_parameters)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday["4. close"]

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)

diff_percent = (difference / float(yesterday_closing_price)) * 100

if abs(diff_percent) > 1:
    news_parameters ={
    "apikey" : news_api_key,
    "qInTitle": COMPANY_NAME,
    "q" : COMPANY_NAME,
    }
    news_response = requests.get(url= "https://newsapi.org/v2/everything", params = news_parameters)
    news_response.raise_for_status()
    articles = news_response.json()["articles"]
    three_articles = articles[:3]

    formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

    account_sid = os.environ.get("ACCOUNT_SID")
    auth_token =os.environ.get("AUTH_TOKEN")

    client = Client(account_sid, auth_token)
    for article in formatted_articles:
        message = client.messages \
            .create(
                body= article,
                from_ = "+15164004128",
                to = "+9779806736272",
            )
        print(message.status)


