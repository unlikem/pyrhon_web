import requests
from bs4 import BeautifulSoup
import re

r = requests.get("https://python123.io/ws/demo.html")
demo = r.text
# print(demo)
soup = BeautifulSoup(demo, "html.parser")

# print(soup.find_all('a'))

# for tag in soup.find_all(True):
#     print(tag.name)

# for tag in soup.find_all(re.compile('b')):
#     print(tag.name)

# course = soup.find_all('p', 'course')
# print(len(course))












