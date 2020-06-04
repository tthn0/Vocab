""" The commented part is the old version """

import requests
from bs4 import BeautifulSoup

reset = '\033[0m'
bold = '\033[1m'
italic = '\x1B[3m'
cyan = '\033[36m'
darkgrey = '\033[90m'

# URL = 'https://learnersdictionary.com/word-of-the-day'
# page = requests.get(URL)
# soup = BeautifulSoup(page.content, 'html.parser')

# word = soup.find('span', class_='hw_txt').text
# kind = soup.find('div', class_='fl').text
# definition = soup.find('div', class_='midbt').text

# print(f"{cyan}{word}{reset}: {darkgrey}{italic}{bold}{kind}{reset} {definition[2:].strip()}")

URL = 'https://www.dictionary.com/e/word-of-the-day/'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

word = soup.find('div', class_='wotd-item-headword__word').text.strip()
pron = soup.find('div', class_='wotd-item-headword__pronunciation').text.strip()
kind = soup.find('span', class_='luna-pos').text.strip()
definition = soup.find('div', class_='wotd-item-headword__pos').find_all('p')[1].text.strip()

pron = pron[0:1:] + pron[2::]
pron = pron[0:-2:] + pron[-1::]

print(f"{bold}{cyan}{word}{reset} {pron}: {italic}{darkgrey}{kind}{reset}\n{definition}\n")
