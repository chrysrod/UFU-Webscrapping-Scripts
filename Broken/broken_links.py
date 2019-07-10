from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import sys

def main(argv):

    websites = ["www.ifilo.ufu.br","www.ifilo.ufu.br/graduacao/filosofia"]

    if argv[1] == "-v":
        verbose = True
    else:
        verbose = False

    for website in websites:

        api_link = "https://api.hackertarget.com/pagelinks/?q=" + website

        try:
            source = urlopen(api_link)
        except HTTPError as error:
            print("HTTP Error, error code: " + error + "\n")
        except URLError:
            print("Web server not found\n")
        else:
            verifyBrokenLinks(source,website,verbose)

def verifyBrokenLinks(source,website,verbose):
    
    data = source.readlines()
    links_related = []
    links_related_2 = []
    links_related_3 = []
    broken_links = []

    for line_encoded in data:
        if website in line_encoded.decode("utf-8"):
            links_related.append(line_encoded.decode("utf-8"))    

    for link in links_related:
        if "#" not in link:
            try:
                source_code = urlopen(link)
            except HTTPError as error:
                broken_links.append(link)
                if verbose == True:
                    print("Broken link: " + link)
            except URLError:
                broken_links.append(link)
                if verbose == True:
                    print("Broken link: " + link)
            else:
                if link not in links_related:
                    links_related_2.append()
                if verbose == True:
                    print("Not a broken link: " + link)

    for link in links_related_2:
        if "#" not in link:
            try:
                source_code = urlopen(link)
            except HTTPError as error:
                broken_links.append(link)
                if verbose == True:
                    print("Broken link: " + link)
            except URLError:
                broken_links.append(link)
                if verbose == True:
                    print("Broken link: " + link)
            else:
                if link not in links_related_2:
                    links_related_3.append()
                if verbose == True:
                    print("Not a broken link: " + link)

    for link in links_related_3:
        if "#" not in link and link not in links_related or links_related_2:
            try:
                source_code = urlopen(link)
            except HTTPError as error:
                broken_links.append(link)
                if verbose == True:
                    print("Broken link: " + link)
            except URLError:
                broken_links.append(link)
                if verbose == True:
                    print("Broken link: " + link)
            else:
                if verbose == True:
                    print("Not a broken link: " + link)

    if broken_links:
        print("Broken Links List:")
        for broken_link in broken_links:
            print(broken_link)

if __name__ == "__main__":
    main(sys.argv)
