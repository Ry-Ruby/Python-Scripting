# Extracting HTML attributes from target url
# posting forms to login page 

import requests
from bs4 import BeautifulSoup
import urllib.parse


def request(url):
	try:
		return requests.get("http://" + url)
	except requests.exceptions.ConnectionError:
		pass 

target_url = "http://172.16.124.4/dvwa/login.php"
response = requests.get(target_url)

parsed_html = BeautifulSoup(response.content, features="lxml")
forms_list = parsed_html.findAll("form")

for form in forms_list:
	action = form.get("action")
	post_url = urllib.parse.urljoin(target_url, action)
	method = form.get("method")

	inputs_list = form.findAll("input")
	post_data = {}
	for input in inputs_list:
		input_name = input.get("name")
		input_type = input.get("type")
		input_value = input.get("value")
		if input_type == "text":
			input_value = "test"

		post_data[input_name] = input_value
	result = requests.post(post_url, data=post_data)
	print(result.content)