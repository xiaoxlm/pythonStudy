# HTMLParser
# 如果我们要编写一个搜索引擎，第一步是用爬虫把目标网站的页面抓下来，第二步就是解析该HTML页面，看看里面的内容到底是新闻、图片还是视频。
#
# 假设第一步已经完成了，第二步应该如何解析HTML呢？
#
# HTML本质上是XML的子集，但是HTML的语法没有XML那么严格，所以不能用标准的DOM或SAX来解析HTML。
#
# 好在Python提供了HTMLParser来非常方便地解析HTML，只需简单几行代码：

from html.parser import HTMLParser
from html.entities import name2codepoint
import requests

class MyHTMLParser(HTMLParser):

    bool_location = False
    bool_title = False
    bool_datetime = False

    bool_test = False


    def handle_starttag(self, tag, attrs):
        if len(attrs) > 0:
            # if tag == "p" and attrs[0][1] == "order":
            #     self.bool_test = True
            if tag == "span" and attrs[0][1] == "event-location":
                self.bool_location = True
            if tag == "h3" and attrs[0][1] == "event-title":
                self.bool_title = True
            if tag == "time" and attrs[0][0] == "datetime":
                self.bool_datetime = True

        # params = ''
        # if attrs:
        #     for key, value in attrs:
        #         params += key + '=' + '\'' + value + '\'' + ' '
        #
        # if tag == "p":
        #     self.bool_tag = True

    def handle_endtag(self, tag):
        # print('</%s>' % tag)
        pass

    def handle_startendtag(self, tag, attrs):
        # print('<%s/>' % tag)
        pass

    def handle_data(self, data):
        # if self.bool_test:
        #     print('test:', data)
        #     self.bool_test = False
        if self.bool_location:
            print('location:', data)
            self.bool_location = False
        if self.bool_title:
            print('title:', data)
            self.bool_title = False
        if self.bool_datetime:
            print('datetime:', data)
            self.bool_datetime = False
        # pass

    def handle_comment(self, data):
        # print('<!--', data, '-->')
        pass

    def handle_entityref(self, name):
        # print('&%s;' % name)
        pass

    def handle_charref(self, name):
        # print('&#%s;' % name)
        pass

parser = MyHTMLParser()

html = requests.get("https://www.python.org/events/python-events/")

parser.feed(html.text)

# parser.feed('''<html>
# <head></head>
# <body>
# <!-- test html parser -->
#     <p class='order' id = 'zz'>Some &#1234<a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
#     <input type='button'/>
# </body></html>''')


# feed()方法可以多次调用，也就是不一定一次把整个HTML字符串都塞进去，可以一部分一部分塞进去。

# 特殊字符有两种，一种是英文表示的&nbsp;，一种是数字表示的&#1234;，这两种字符都可以通过Parser解析出来。