import re
from html.parser import HTMLParser
from urllib.request import urlopen

'''
class MyHTMLParser(HTMLParser):

    def error(self, message):
        print('error')
        pass

    # <%s>类型
    def handle_starttag(self, tag, attrs):
        print('handle_starttag: <%s>' % tag)

    # </%s>类型
    def handle_endtag(self, tag):
        print('handle_endtag: </%s>' % tag)

    # <%s/>类型
    def handle_startendtag(self, tag, attrs):
        print('handle_startendtag: <%s/>' % tag)

    def handle_data(self, data):
        print("handle_data: %s" % data)

    def handle_comment(self, data):
        print('handle_comment: <!--', data, '-->')

    def handle_entityref(self, name):
        print('handle_entityref: &%s;' % name)

    def handle_charref(self, name):
        print('handle_charref: &#%s;' % name)
'''


# parser = MyHTMLParser()
# parser.feed('''
# <html>
# <head></head>
# <body>
# <!-- test html parser -->
#     <p>
#         Some <a href=\"#\">html</a>
#         HTML&nbsp;tutorial...&#1234
#         <br>
#         END
#     </p>
# </body>
# </html>''')


# 习题
class PythonHtmlParser(HTMLParser):

    def __init__(self):
        super().__init__()
        self.__parsedata = ''
        self.__currentTag = ''

    # def error(self, message):
    #     pass
    #
    # def handle_starttag(self, tag, attrs):
    #     self.__currentTag = tag
    #     if tag == 'time':
    #         self.__currentTag = 'time'
    #     elif tag == 'h3':
    #         if ('class', 'event-title') in attrs:
    #             self.__currentTag = 'h3'
    #     elif (tag == 'a') and ('/events/python-events/' in attrs[0][1]):
    #         self.__currentTag = 'events'
    #     elif tag == 'span':
    #         if ('class', 'event-location') in attrs:
    #             self.__currentTag = 'span'
    #
    # def handle_endtag(self, tag):
    #     self.__currentTag = ""
    #
    # def handle_data(self, data):
    #     if self.__currentTag == 'time':
    #         print('会议时间', data)
    #     elif self.__currentTag == 'events':
    #         print('会议地点', data)
    #     elif (self.__currentTag == 'span' and ('▼' not in data) and (
    #             '▲' not in data) and ('≡' not in data)):
    #         print('会议名称', data)
    #         print('------------------------------')

    def handle_starttag(self, tag, attrs):
        if ('class', 'event-title') in attrs:
            self.__parsedata = 'name'  # 设置爬取名称状态
        if tag == 'time':
            self.__parsedata = 'time'
        if ('class', 'say-no-more') in attrs:
            self.__parsedata = 'year'
        if ('class', 'event-location') in attrs:
            self.__parsedata = 'location'

    def handle_endtag(self, tag):
        if tag == 'h3' or tag == 'span':
            self.__parsedata = ''

    def handle_data(self, data):
        if self.__parsedata == 'name':
            print('会议名称:%s' % data)

        if self.__parsedata == 'time':
            print('会议时间:%s' % data)

        if self.__parsedata == 'year':
            if re.match(r'\s\d{4}', data):
                # 因为后面还有两组 say-no-more 后面的data却不是年份信息,所以用正则检测一下
                print('会议年份:%s' % data.strip())

        if self.__parsedata == 'location':
            print('会议地点:%s' % data)
            print('----------------------------------')


with urlopen('https://www.python.org/events/python-events/') as f:
    parser = PythonHtmlParser()
    parser.feed(f.read().decode('utf-8'))
