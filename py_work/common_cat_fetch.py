from bs4 import BeautifulSoup
from urllib import request

def get_soup(url):
    req_result = request.urlopen(url);
    return BeautifulSoup(req_result.read().decode("utf-8"), "html.parser")

def main(domain, methods):
    method_to_app = {}

    if methods:
        for method in methods:
            url = "http://cat.qipeipu.net/cat/r/cross?op=query&domain=" + domain + "&date=20181001&reportType=month&method=" + method
            soup = get_soup(url)
            trs = soup.find_all("tr", class_="right")

            for i in range(0, len(trs)):
                tds = trs[i].find_all("td")

                if len(tds) > 0:
                    method_name = tds[3].text.strip()

                    if not method_to_app.get(method_name):
                        method_to_app[method_name] = {tds[1].text.strip(),}
                    else:
                        app_names = method_to_app.get(method_name)
                        app_names.add(tds[1].text.strip())
                        method_to_app[method_name] = app_names

    for key, values in method_to_app.items():
        print(str(key) + ":" + str(values))


main("trade-service", ["DeliveryOrderUpdateService"])