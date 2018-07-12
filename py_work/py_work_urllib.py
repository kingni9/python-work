import ssl, random
from urllib import request, parse
from bs4 import BeautifulSoup

# todo version 2.0 -- 爬取代理ip生成ProxyPool, 通过proxyPool发送爬取请求, 主要改造get_soup()函数
proxy_pool = []

# 设置ssl -- 兼容urllib发送https请求
def ssl_init():
    ssl._create_default_https_context = ssl._create_unverified_context

def init_proxy_pool(scan_pages):
    for page in range(3, scan_pages + 1):
        try:
            url = "https://www.kuaidaili.com/free/inha/" + str(page)

            soup = get_soup(url)
            table = soup.find("table", class_="table table-bordered table-striped")
            if table is not None:
                tr_list = table.find_all("tr")
                if len(tr_list) > 0:
                    for tr in tr_list:
                        td_list = tr.find_all("td")

                        if len(td_list) > 0:
                            proxy_url = "http://" + str(td_list[0].get_text()) + ":" + str(td_list[1].get_text())
                            if proxy_url not in proxy_pool:
                                print("Get Proxy Url Success::" + proxy_url)
                                proxy_pool.append(proxy_url)
        except Exception:
            pass

# 根据代理池的对象发送请求
def get_proxy_soup(url):
    global proxy_pool
    proxy_handler = request.ProxyHandler({"http":proxy_pool[random.randint(0, (len(proxy_pool) - 1))]})
    req_result = request.build_opener(proxy_handler).open(url)

    # req_result = request.urlopen(url)
    return BeautifulSoup(req_result.read().decode("utf-8"), "html.parser")

# 请求url 返回html被BeautifulSoup解析生成的对象
def get_soup(url):
    req_result = request.urlopen(url);
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
    init_proxy_pool(50)

    if len(proxy_pool) < 50:
        print("Scan Proxy Pool Failed::Pool size litter then 50")
        return

    print("Get Total Proxy Pool Size:::" + str(len(proxy_pool)))

    tag_list = get_tag()
    if len(tag_list) > 0:
        for tag in tag_list:
            print("######################################## Tag::" + tag + " ########################################")
            parse_for_tag(tag)


main_runner()