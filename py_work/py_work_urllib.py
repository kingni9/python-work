import ssl
from urllib import request, parse
from bs4 import BeautifulSoup

# 设置ssl -- 兼容urllib发送https请求
def ssl_init():
    ssl._create_default_https_context = ssl._create_unverified_context

# 请求url 返回html被BeautifulSoup解析生成的对象
def get_soup(url):
    req_result = request.urlopen(url)
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


def get_subject_url(tag, start):
    return "https://book.douban.com/tag/" + parse.quote(tag) + "?start=" + str(start) + "&type=T"


def subject_handle(tag, start):
    url = get_subject_url(tag, start)
    soup = get_soup(url)

    if soup is None:
        print("Warn::Can't get the tag soup, requst url:" + url)
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


def parse_for_tag(tag):
    start = 0
    while True:
        if not subject_handle(tag, start):
            break

        start += 20


def main_runner():
    ssl_init()

    tag_list = get_tag()
    if len(tag_list) > 0:
        for tag in tag_list:
            print("######################################## Tag::" + tag + " ########################################")
            parse_for_tag(tag)


main_runner()

