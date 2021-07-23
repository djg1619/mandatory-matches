#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests

url = 'https://www.goal.com/en-us/live-scores'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

match = soup.find('span',class_='match-row__date')

competition = soup.find('span',class_='competition-name')

home = soup.find('td', class_="match-row__team-home")

away = soup.find('td', class_="match-row__team-away")

for match,home,away in zip(soup.find_all('span', class_='match-row__date'),soup.find_all('td', class_="match-row__team-away"),soup.find_all('td', class_="match-row__team-home")):
    print(competition.text + " " +match.text,home.text,'VS',away.text)


# In[ ]:




