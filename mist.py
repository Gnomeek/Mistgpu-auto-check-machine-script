import requests
from bs4 import BeautifulSoup
import time
from wxpy import *
import sys


def get_page(username, password):
	account = {
		'username': username,
		'password': password,
	}
	loginurl = "https://mistgpu.com/login/"
	session = requests.Session()
	session.post(loginurl, data = account)

	mainurl = "https://mistgpu.com/create/"
	rsp = session.get(mainurl)
	page = rsp.text
	with open("page.html", "w") as f:
		for i in page:
			f.write(i)

def get_machine(machine_id):
	with open("page.html","r") as page:
		soup = BeautifulSoup(page, features="lxml")
	machine_attr = {
		'class': "card form-check",
		'class': "form-check-input",
		'value': machine_id,
		}
	machine = soup.find_all(attrs = machine_attr)
	print(str(machine))
	if str(machine).find("disabled=") != -1:
		return "not yet"
	else:
		return "find it"

def send_notification(bot, result):
	if result == "find it":
		bot.file_helper.send('Now the machine is available!')


if __name__=="__main__":
	username = sys.argv[1]
	password = sys.argv[2]
	machine_id = sys.argv[3]

	# bot = Bot()
	while True:
		get_page(username, password)
		result = get_machine(machine_id)
		send_notification(bot, result)
		time.sleep(30)