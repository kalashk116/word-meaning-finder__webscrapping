import requests
from bs4 import BeautifulSoup

word = input("Enter a word: ")

url1 = f"https://www.merriam-webster.com/dictionary/{word}"
url2 = f"https://www.dictionary.com/browse/{word}"

response1 = requests.get(url1)
response2 = requests.get(url2)

soup1 = BeautifulSoup(response1.content, 'html.parser')
soup2 = BeautifulSoup(response2.content, 'html.parser')


phonetics_elem = soup2.find(spanclass="pron-spell-content css-7iphl0 evh0tcl1")
if phonetics_elem is None:
    phonetics = 'not found'
else:
    phonetics = phonetics_elem.text

meaning_elem = soup1.find('span', class_='dtText')
if meaning_elem is None:
    meaning = 'not found'
else:
    meaning = meaning_elem.text

print(f"Phonetics: {phonetics}")
print(f"Meaning: {meaning}")

