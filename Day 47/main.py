from bs4 import BeautifulSoup
import requests
import smtplib

MY_EMAIL = "angeldahal02@yahoo.com"
MY_PASSWORD = "#Angaldahal@12()"


amazon_headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}
response = requests.get(url = "https://www.amazon.com/dp/B098D6LZLW/ref=dp_cr_wdg_tit_rfb", headers = amazon_headers)

soup = BeautifulSoup(response.text , "html.parser")
price = soup.find("span", class_ = "a-offscreen")
price = price.getText()[1:]
price_as_float = float(price)

contents = f'Samsung Tab A7 Lite 8.7" Gray 32GB (SM-T220NZAAXAR) is now ${price_as_float}'
with smtplib.SMTP("smtp.mail.yahoo.com", port = 465) as connection:
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs="Angeldahal202@gmail.com",
        msg=f"Subject:Amazon Price Alert!\n\n{contents}"
    )
