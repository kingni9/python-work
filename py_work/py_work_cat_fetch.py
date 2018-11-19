from bs4 import BeautifulSoup
from urllib import request

# 体积相关应用cat-dao调用数据 #
domain_name = "logistics-service"
start_date = "20181101"
end_date = "20181201"


def get_soup(url):
    req_result = request.urlopen(url);
    # req_result = request.urlopen(url)
    return BeautifulSoup(req_result.read().decode("utf-8"), "html.parser")

def parser_soup(url):
    soup = get_soup(url)
    trs = soup.find_all("tr", class_=" right")
    for i in range(1, len(trs)):
        tds = trs[i].find_all("td")
        tds_str = tds[1].text + "    " + tds[0].text[len("[:: show ::] "):].strip()
        print(tds_str)

def main():
    url = "http://cat.qipeipu.net/cat/r/t?op=history&domain=" + domain_name + "&ip=All&reportType=month&type=DAO&sort=total&startDate=" + start_date + "&endDate=" + end_date
    parser_soup(url)


main()