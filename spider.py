# extracts all the pages from all links within website
# Python3
# Had to google and import a different library for Python3
# Converted a byte-like object to a string(line 21)
# use decode(errors="ignore" to ignore any errors while decoding)
import requests
import re 
import urllib.parse as urlparse


def request(url):
	try:
		return requests.get("http://" + url)
	except requests.exceptions.ConnectionError:
		pass

target_url = "https://www.surfline.com/"
target_links = []

def extract_links_from(url):
	response = requests.get(url)
	return re.findall('(?:href=")(.*?)"', response.content.decode(errors="ignore"))

def crawl(url):
	href_links = extract_links_from(url)
	for link in href_links:
		link = urlparse.urljoin(url, link)
		
		if target_url in link and link not in target_links:
			target_links.append(link)
			print(link)
			crawl(link)

crawl(target_url)
