import requests
from bs4 import BeautifulSoup

URL = "https://www.iban.com/currency-codes"

def extract_country_list():
  countries = []
  result = requests.get(URL)
  soup = BeautifulSoup(result.text, 'html.parser')
  table = soup.find_all("tr")

  for tr in table[1:]:
    countries.append([td.text.replace('\n', '').replace('\xa0', '').replace('\t', '').strip() for td in tr.find_all('td')])

  countries = [td for td in countries if not "No universal currency" in td]

  return countries
