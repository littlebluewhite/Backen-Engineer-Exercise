import sys
import bs4
import requests
import re


class FindInAlexa:
    url_dict = {"top": "https://www.alexa.com/topsites/",
                "country": "https://www.alexa.com/topsites/countries"
                }

    def __init__(self, action, *args):
        self.__action = action
        self.__arg = " ".join(*args)
        self.__url = self.url_dict[action]
        self.__headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                                        "AppleWebKit/537.36 (KHTML, like Gecko) "
                                        "Chrome/89.0.4389.82 Safari/537.36"}

    def __action_top(self):
        html = requests.get(self.__url, headers=self.__headers)
        try:
            html.raise_for_status()
            objsoup = bs4.BeautifulSoup(html.text, 'lxml')
            datatag = objsoup.select('div .td.DescriptionCell > p > a')
            hrefattrs = datatag[int(self.__arg)-1].get("href")
            result = "Top " + self.__arg + " url: " + "https://www.alexa.com" + hrefattrs
            print(result)
        except Exception as err:
            print("fail %s" % err)

    def __action_country(self):
        html = requests.get(self.__url, headers=self.__headers)
        try:
            html.raise_for_status()
            pattern = r'<a href="(countries/[A-Z]+)">' + self.__arg + r'</a>'
            country_url = re.findall(pattern, html.text)
            country_url = "https://www.alexa.com/topsites/" + country_url[0]
            country_html = requests.get(country_url, headers=self.__headers)
            country_html.raise_for_status()
            objsoup = bs4.BeautifulSoup(country_html.text, 'lxml')
            datatags = objsoup.select('div .td.DescriptionCell > p > a')
            print("Top 20 in "+self.__arg+":")
            for datatag in datatags[:20]:
                print("https://www.alexa.com" + datatag.get("href"))
        except Exception as err:
            print("fail %s" % err)

    def action(self):
        if self.__action == "top":
            self.__action_top()
        elif self.__action == "country":
            self.__action_country()


if __name__ == '__main__':
    find = FindInAlexa(sys.argv[1], sys.argv[2:])
    find.action()
