import requests
from bs4 import BeautifulSoup


def getHuaweiDownloadCount():
    # 由于网站反爬虫，需要模拟浏览器
    needHeaders = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/34.0.1847.137 Safari/537.36 LBBROWSER'}

    r = requests.get('http://app.hicloud.com/app/C10573550', headers=needHeaders)
    soup = BeautifulSoup(str(r.content, 'utf-8'), 'lxml')
    a = soup.select(
        '#bodyonline > div > div.lay-main > div.lay-left.hdn-x > div > div > div.app-info.flt > ul:'
        'nth-child(1) > li:nth-child(2) > p:nth-child(1) > span.grey.sub')[0].get_text()
    print('华为下载量' + a)


def getMiDownloadCount(packageName):
    # 由于网站反爬虫，需要模拟浏览器
    needHeaders = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/34.0.1847.137 Safari/537.36 LBBROWSER'}

    r = requests.get('http://app.mi.com/details?id=' + packageName + '&ref=search',
                     headers=needHeaders)
    soup = BeautifulSoup(str(r.content, 'utf-8'), 'lxml')
    a = soup.select('body > div.main > div.container.cf '
                    '> div.app-intro.cf > div.app-info > div > span')[0].get_text()
    print('小米评分等级' + a)


def getYYBDownloadCount(packageName):
    # 由于网站反爬虫，需要模拟浏览器
    needHeaders = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/34.0.1847.137 Safari/537.36 LBBROWSER'}

    r = requests.get('https://sj.qq.com/myapp/detail.htm?apkName=' + packageName+"",
                     headers=needHeaders)
    soup = BeautifulSoup(str(r.content, 'utf-8'), 'lxml')
    a = soup.select('#J_DetDataContainer > div > div.det-ins-container.J_Mod > div.det-ins-data '
                    '> div.det-insnum-line > div.det-ins-num')
    if a.__len__() > 0:
        print('应用宝下载量：' + a[0].getText())
    else:
        print('未找到该应用')



inputName = input('请输入要查询的包名')

# getHuaweiDownloadCount()
# getMiDownloadCount(inputName)
getYYBDownloadCount(inputName)
