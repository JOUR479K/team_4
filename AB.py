import csv
from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen

BASE_URL = "http://www.rollingstone.com/search?q=andrew%20bird"

def get_article_links(section_url):
	html = urlopen(section_url).read()
	soup = BeautifulSoup(html, "lxml")
	boccat = soup.find("div", "primary")
	article_links = ["http://www.rollingstone.com/" + section.a["href"] for section in boccat.findAll("section")]
	return {"article_url": article_links}

def write_to_csv(filename, results):
    with open(filename, 'wb') as csvfile:
                        w = csv.writer(csvfile)
                        w.writerow(['first_header','second_header'])
                        for section_url, links in results:
                            for link in links:
                                w.writerow([section_url, link])
