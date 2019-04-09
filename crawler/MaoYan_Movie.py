import requests
from bs4 import BeautifulSoup
import re
import csv

def get_one_page(url):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
    # 不加 headers 爬不了
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text

def get_thumb(url):
    pattern = re.compile(r'(.*?)@.*?')
    thumb = re.search(pattern, url)
    return thumb.group(1)

def get_release_time(data):  # 该方法在parse_one_page中使用使用
    pattern = re.compile(r'(.*?)(\(|$)')
    items = re.search(pattern, data)
    if items is None:
        return '未知'
    return items.group(1)

def get_release_area(data):
    pattern = re.compile(r'.*\((.*)\)')
    # $表示匹配一行字符串的结尾，这里就是(.*?)；\(|$,表示匹配字符串含有(,或者只有(.*?)
    items = re.search(pattern, data)
    if items is None:
        return '未知'
    return items.group(1)

# 用 beautifulsoup find_all()函数爬取
def parse_one_page(html):
    soup = BeautifulSoup(html,"lxml")
    items = range(10)
    for item in items:
        yield{
        'index': soup.find_all(class_='board-index')[item].string,
        # 'thumb': soup.find_all(class_ = 'board-img')[item].attrs['src'],
        # 用.get('src')获取图片 src 链接，或者用 attrs['src']
        'name': soup.find_all(name = 'p',attrs = {'class' : 'name'})[item].string,
        'star': soup.find_all(name = 'p',attrs = {'class':'star'})[item].string.strip()[3:],
        'time': get_release_time(soup.find_all(class_ ='releasetime')[item].string.strip()[5:]),
        'area': get_release_time(soup.find_all(class_ ='releasetime')[item].string.strip()[5:]),
        'score':soup.find_all(name = 'i',attrs = {'class':'integer'})[item].string.strip() + soup.find_all(name = 'i',attrs = {'class':'fraction'})[item].string.strip()
        }

#  用 beautifulsoup + css 选择器提取
def parse_one_page2(html):
    soup = BeautifulSoup(html, 'lxml')
    items = range(10)
    for item in items:
        yield{
        'index': soup.select('dd i.board-index')[item].string,
        # iclass 节点完整地为'board-index board-index-1',写 board-index 即可
        'thumb': get_thumb(soup.select('a > img.board-img')[item]["src"]),
        # 表示 a 节点下面的 class = board-img 的 img 节点,注意浏览器 eelement 里面是 src 节点，而 network 里面是 src 节点，要用这个才能正确返回值
        'name': soup.select('.name a')[item].string,
        'star': soup.select('.star')[item].string.strip()[3:],
        'time': get_release_time(soup.select('.releasetime')[item].string.strip()[5:]),
        'area': get_release_area(soup.select('.releasetime')[item].string.strip()[5:]),
        'score': soup.select('.integer')[item].string + soup.select('.fraction')[item].string
        }


def write_to_csv(item):
    with open('猫眼top100.csv', 'a', encoding='utf_8_sig',newline='') as f:
        # 'a'为追加模式（添加）
        # utf_8_sig 格式导出 csv 不乱码
        fieldnames = ['index', 'thumb', 'name', 'star', 'time', 'area', 'score']
        w = csv.DictWriter(f, fieldnames = fieldnames)
        # w.writeheader()
        w.writerow(item)

def main():
    url = 'http://maoyan.com/board/4?offset=0'
    html = get_one_page(url)
    for item in parse_one_page(html):
        # print(item)
        write_to_csv(item)

if __name__ == '__main__':
    main()





