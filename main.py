from bs4 import BeautifulSoup
import requests

def search(keyword):
  headers = {
    'User-Agent': (
      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
      'AppleWebKit/537.36 (KHTML, like Gecko) '
      'Chrome/39.0.2171.95 '
      'Safari/537.36'
    )
  }
  res = requests.get(f'https://www.onoffmix.com/event/main?s={keyword}', headers=headers)

  html = BeautifulSoup(res.text, 'html.parser')
  events = html.find_all('article', class_='event_area')
  events = [{
    'id': e.find('a')['href'][-6:],
    'title': e.find('h5', class_='title')['title'],
    'date': e.find('div', class_='date').text,
  } for e in events]

  return events

events = search('해커톤')
events += [event for event in search('아이디어톤') if event['id'] not in events]
print(*events, sep='\n')
