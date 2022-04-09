import requests
from requests_html import HTMLSession
from bs4 import  BeautifulSoup

#
# r = requests.get("https://jsonplaceholder.typicode.com/todos/1")
# print(r.json())
# print(r.content)
# print(r.status_code)
#
#
# payload = {"data": "data"}
#
# data = requests.post('https://httpbin.org/post', data=payload)
# print(data.json())
#
# s = HTMLSession()
# r = requests.get('https://httpbin.org/headers')
#
# rh = s.get('https://httpbin.org/headers')
# print(r.text)
# print((rh.text))
#
# url = 'https://httpbin.org/headers'
#
# headers = {
#     "User-Agent": "Chrome Windows hp probook",
#     "Accept-Language": "en-GB, en;q=0.5"
#
# }
# req = requests.get(url, headers=headers)
# print(req.text)

r= requests.get('https://api.dailysmarty.com/posts')
# print(r.text)
print(r.json()['posts'])

r = requests.get('https://xkcd.com/353/')
print(dir(r))
print(help(r))
print(r.content)


print('hello World')

