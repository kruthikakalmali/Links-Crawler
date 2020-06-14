import requests
import re
from optparse import OptionParser
import sys
from appdirs import unicode
from termcolor import colored
if sys.version_info[0] >= 3:
    from urllib.parse import urljoin
else:
    import urlparse
class Crawler:
    def __init__(self):
        self.script_desc()
        self.target_links = []
    def arguman_al(self):
        parse = OptionParser(description=self.description,epilog=self.a,prog=self.program)
        parse.add_option("-u", "--url", dest="url", help="Hedef url")
        (options, arguments) = parse.parse_args()
        if not options.url:
            parse.error("error parsing")
        return options
    def get_links(self,url):
        try:
            if "http://" in url   or "https://" in url:
                response=requests.get(url)
                return re.findall('(?:href=")(.*?)"', str(response.content))
            else:
                response=requests.get("http://"+url)
                return re.findall('(?:href=")(.*?)"',str(response.content))
        except requests.exceptions.ConnectionError:
            pass
        except requests.exceptions.InvalidURL:
            pass
        except UnicodeError:
            pass


    def crawl(self,url):
        href_links=self.get_links(url)
        if href_links:
            for link in href_links:
                link=urljoin(url,link)
                if "#" in link:
                    link=link.split("#")[0]
                if options.url in link and link not in self.target_links:
                    self.target_links.append(link)
                    print(link)
                    self.crawl(link)

    def result_count(self):
        print(colored(str(len(self.target_links))));

    def script_desc(self):
        self.program="spider"
        self.a=""
        if sys.version_info[0] >= 3:
            self.description = ""
        else:
            self.description = unicode("", "utf8")
            self.a = unicode(self.a,"utf8")

    def keyboardinterrupt_message(self):
        print("you pressed ctrl+c")
try:
    crawl=Crawler()
    options=crawl.arguman_al()
    #print(colored(options.url+"\n"))
    crawl.crawl(options.url)
    #crawl.result_count()
except KeyboardInterrupt:
    crawl.keyboardinterrupt_message()


