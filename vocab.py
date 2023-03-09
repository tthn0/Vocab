""" This program outputs the word of the day from dictionary.com
Usage: $ python3 vocab.py
"""

import requests
from bs4 import BeautifulSoup

# Define ANSI escape codes
reset = "\033[0m"
bold = "\033[1m"
italic = "\x1B[3m"
cyan = "\033[36m"
red = "\u001b[31m"
darkgrey = "\033[90m"

# Start scraper
try:
    URL = "https://www.dictionary.com/e/word-of-the-day/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
except:
    print(red + "An error occured." + reset)
    exit()

# Find the word of the day, pronounciation, kind of word, and definition
word = soup.find("div", class_="otd-item-headword__word").text.strip()
pron = soup.find("span", class_="otd-item-headword__pronunciation__text").text.replace(" ",  "").strip()
kind = soup.find("span", class_="luna-pos").text.strip()
definition = soup.find("div", class_="otd-item-headword__pos").find_all("p")[1].text.strip()

# Print Everything
args = (bold, cyan, word, reset, pron, italic, darkgrey, kind, reset, definition)
print("\n%s%s%s%s %s: %s%s%s%s\n%s\n" % args)
