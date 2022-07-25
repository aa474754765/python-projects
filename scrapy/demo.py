import requests
from bs4 import BeautifulSoup
import os
from tqdm import tqdm

req = requests.request(method="GET", url="https://www.yingsx.com/0_100/")

req.encoding = 'utf-8'

html = req.text

bs = BeautifulSoup(html, 'lxml')

dt = bs.find('div', id='list').find_all('dt')[1]

# url 列表
urlList = []
# name 文章名 列表
nameList = []

# dt.find_all_next('dd') 找到 第二个 dt 标签后 所有的 dd 返回一个 列表
for dd in dt.find_all_next('dd'):
    # 获取每个 a 标签 的 href 属性值，即 每一章 的 url
    urlList.append('https://www.yingsx.com' + dd.find('a').get('href'))
    # 获取每个 a 标签 的 内容，即 每一章 的 标题名
    nameList.append(dd.find('a').text)

if not os.path.exists('元尊'):
    os.mkdir('元尊')

print(len(urlList))

for i, url in enumerate(tqdm(urlList)):
    req = requests.request(method="GET", url=url)
    req.encoding = 'utf-8'
    html = req.text
    bs = BeautifulSoup(html, 'lxml')

    # 找到正文
    content = bs.find('div', id='content').text.strip().split('\xa0' * 4)

    path = '元尊\\' + nameList[i] + '.txt'
    print(path)
    if os.path.exists(path):
        os.remove(path)
    f = open(path, 'w', encoding='utf-8')
    for str in content:
        f.write(str)
    f.close()
    break
