import requests

r = requests.get(url='http://www.baidu.com/')
print(r.url)
print(r.text)
