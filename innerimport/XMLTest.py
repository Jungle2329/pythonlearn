from urllib.request import urlopen
from xml.parsers.expat import ParserCreate

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''


def f2c(f_t):
    return int(5 / 9 * (f_t - 32))


"""
<a href="/">python</a>
会产生3个事件：
start_element事件，在读取<a href="/">时；
char_data事件，在读取python时；
end_element事件，在读取</a>时。
"""


class DefaultSaxHandler(object):

    def __init__(self):
        self.weather_city = ''
        self.weather = []

    # 拿到起始节点
    def start_element1(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))
        if name == 'yweather:location':
            self.weather_city = attrs['city']
        if name == 'yweather:forecast':
            self.weather.append(attrs)

    # 拿到结束节点
    def end_element1(self, name):
        print('sax:end_element: %s' % name)

    def char_data1(self, text):
        print('sax:char_data: %s' % text)


"""
handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)
"""

url = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where' \
      '%20woeid%20%3D%202151330&format=xml'

with urlopen(url) as f:
    data = f.read().decode('utf-8')


def parseXml(xml_str):
    handler = DefaultSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element1
    # parser.EndElementHandler = handler.end_element
    # parser.CharacterDataHandler = handler.char_data
    parser.Parse(xml_str)

    # print(handler.weather_json.replace('\'', '\"'))
    # json_str = json.loads(handler.weather_json.replace('\'', '\"'))
    print(handler.weather_city)
    weather_list = handler.weather
    for x in weather_list:
        print('城市：%s 日期%s 最高温度%s 最低温度%s 天气%s' % (
            handler.weather_city, x['date'], f2c(int(x['high'])), f2c(int(x['low'])), x['text']))


parseXml(data)
