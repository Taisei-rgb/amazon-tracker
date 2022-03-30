import requests
from bs4 import BeautifulSoup

amazon_url = "https://www.amazon.co.jp/gp/product/B07B8BVT8K/ref=ppx_yo_dt_b_asin_title_o02_s00?ie=UTF8&psc=1"

def amazon_tracking_price():
  amazon_page = requests.get(amazon_url)
  soup = BeautifulSoup(amazon_page.content, "html.parser")
  # print(soup)

  title = soup.find(id="productTitle")
  price = soup.find("span", class_="a-price-whole").get_text()
  convert_price = int(price.replace(",", ""))
  print(convert_price)

  if(convert_price > 3000):
    send_line_notify()

def send_line_notify():
  print("LINEに通知がいきました✨")
  line_notify_token = "GcwZZSYvZ3cMiWHq7aq9h1B0Ji4SxM5yTbTkaO7OPyk"
  line_notify_api = "https://notify-api.line.me/api/notify"
  token_info = {"Authorization": f"Bearer {line_notify_token}"}
  send_info = {"message": "ミルクティー味プロテインの価格が下がっているよ✨[URL](https://www.amazon.co.jp/gp/product/B07B8BVT8K/ref=ppx_yo_dt_b_asin_title_o02_s00?ie=UTF8&psc=1)"}
  requests.post(line_notify_api, headers=token_info, data=send_info)

amazon_tracking_price()
