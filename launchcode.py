from requests import get
from bs4 import BeautifulSoup

'''
TODO: prepend http://education.launchcode.org/skills-front-end/
to link, while replacing index 13:15
'''

lc = 'http://education.launchcode.org/skills-front-end/course-outline/'

response = get(lc)
soup = BeautifulSoup(response.text, 'html.parser')
td = soup.find_all('td')
links = []
for num in range(1, len(td), 5):
    link = str(td[num])
    links.append(link)


print(links[0][13])
print(links[0][14])