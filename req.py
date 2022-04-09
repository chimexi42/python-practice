import requests
from requests.exceptions import HTTPError
# url = 'https://imgs.xkcd.com/comics/contingency_plan.png'
#
# r = requests.get(url)
#
# print(dir(r))
# print(r.ok)
# # print(r.text)
# with open('comic.png', 'wb') as f:
#     f.write(r.content)

# print(r.status_code)
# print(r.headers)

# url = 'https://httpbin.org/delay/3'
# # payload = {'username': 'chima', 'password': 'testing'}
# req = requests.get(url)
# print(req.url)
# print(req.text)

for url in ['https://api.github.com/', 'https://api.github.com/invalid']:
    try:
        response = requests.get(url)

        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP errpr occured: {http_err}')
    except Exception as err:
        print(f'Other error occured: {err}')
    else:
        print('success')




