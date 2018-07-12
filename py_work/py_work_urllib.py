import ssl, random
from urllib import request, parse
from bs4 import BeautifulSoup

# todo version 2.0 -- 爬取代理ip生成ProxyPool, 通过proxyPool发送爬取请求, 主要改造get_soup()函数
proxy_pool = ["http://180.104.63.114:9000",
              "http://115.223.214.228:9000",
              "http://58.217.14.251:9000",
              "http://114.101.45.27:63909",
              "http://183.147.222.121:9000",
              "http://115.223.221.134:9000",
              "http://115.223.245.41:9000",
              "http://112.240.181.121:9000"]

# 设置ssl -- 兼容urllib发送https请求
def ssl_init():
    ssl._create_default_https_context = ssl._create_unverified_context

# 请求url 返回html被BeautifulSoup解析生成的对象
def get_soup(url):
    global proxy_pool
    proxy_handler = request.ProxyHandler({"http":proxy_pool[random.randint(0, 7)]})
    req_result = request.build_opener(proxy_handler).open(url)

    # req_result = request.urlopen(url)
    return BeautifulSoup(req_result.read().decode("utf-8"), "html.parser")

# 获取所有书签信息
def get_tag():
    soup = get_soup("https://book.douban.com/tag/?view=type")
    table_list = soup.find_all("table", class_="tagCol")

    type_list = []
    for table in table_list:
        link_list = table.find_all("a")

        for link in link_list:
            type_list.append(link.get_text())

    return type_list


# 拼接标签url
def get_subject_url(tag, start):
    return "https://book.douban.com/tag/" + parse.quote(tag) + "?start=" + str(start) + "&type=T"


# 处理页面 -- 打印出爬取到的数据
def subject_handle(tag, start):
    url = get_subject_url(tag, start)
    soup = get_soup(url)

    if soup is None:
        print("Warn::Can't get the tag soup, request url:" + url)
        return

    subject_item_list = soup.find_all("li", class_="subject-item")

    if len(subject_item_list) == 0:
        print("============================ Empty Result ============================")
        return False

    for item in subject_item_list:
        try:
            sub_element = item.find("div", class_="info")
            title_element = sub_element.find("a")
            rating_element = sub_element.find("span", class_="rating_nums")
            pub_element = sub_element.find("div", class_="pub")
            print((title_element["title"], pub_element.get_text().strip(), rating_element.get_text(), title_element["href"]))
        except Exception:
            print("Parse Subject Error, Exception::" + str(Exception))

    return True


# 按每个tag分别爬取，20条每页
def parse_for_tag(tag):
    start = 0
    while True:
        if not subject_handle(tag, start):
            break

        start += 20


# 启动方法
def main_runner():
    ssl_init()

    tag_list = get_tag()
    if len(tag_list) > 0:
        for tag in tag_list:
            print("######################################## Tag::" + tag + " ########################################")
            parse_for_tag(tag)


main_runner()

