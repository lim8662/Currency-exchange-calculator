import requests
from bs4 import BeautifulSoup

URL = "https://transferwise.com/gb/currency-converter"

def extract_convert_amount(fcode, tcode, amount):


  result = requests.get(f"{URL}/{fcode}-to-{tcode}-rate?amount={amount}")
  soup = BeautifulSoup(result.text, 'html.parser')
  
  rate = soup.find("div", {"class": "row cc-calculator__input-group m-t-3"}).find("span", {"class": "text-success"}).string

  return float(rate) * amount
