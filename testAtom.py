#Задание №1
def first():
	print("""Ошибка 500 говорит о том, что сервер не может обработать запрос
к сайту, на странице которого вы находитесь.
При этом браузер не может точно сообщить, что именно пошло не так
Ошибка означает ошибку на сервере, следовательно, необъходимо как можно быстрее
обнаружить эту ошибку. Просмотреть логи, дебаг кода, понять где проблема и исправить ее
""")
##########################################################################################
##########################################################################################
##########################################################################################
#Задание №2
def testic(al):
	print(al)


def create_handlers(callback):
	handlers: list = []
	for step in range(5):
		handlers.append(lambda step=step: callback(step))

	return handlers

def execute_handlers(handlers: list):
	for handler in handlers:
		handler()

def second():
	execute_handlers(create_handlers(testic))
##########################################################################################
##########################################################################################
##########################################################################################
#Задание №3
from bs4 import BeautifulSoup as BS
def third():
	from bs4 import BeautifulSoup as BS
	page = open("site.txt", encoding="utf8")
	soup = BS(page.read(), 'html.parser')
	countTags = 0
	countAttr = 0
	for child in soup.find_all(): 
		if(len(list(child.attrs.keys()))) > 0:
			countAttr += 1
		countTags += 1
	print(countTags)
	print(countAttr)
##########################################################################################
##########################################################################################
##########################################################################################
#Задание №4
import requests
def fourth():
	print(requests.get("https://ifconfig.me/ip").text)
##########################################################################################
##########################################################################################
##########################################################################################
def fife():
	firstV = "1.10"
	secondV = "1.1."
	if firstV == secondV:
		return 0
	fv = firstV.split('.')
	sv = secondV.split('.')
	lf = len(fv); ls = len(sv)
	workLen = 0
	if lf > ls:
		workLen = ls
	else:
		workLen = lf
	for i in range(workLen):
		if int(fv[i]) > int(sv[i]):
			return -1
		elif int(fv[i]) < int(sv[i]):
			return 1
	if lf > ls:
		return 1
	else:
		return -1

choose = int(input("Выберите номер задания: "))
if choose == 1:
	first()
elif choose == 2:
	second()
elif choose == 3:
	third()
elif choose == 4:
	fourth()
elif choose == 5:
	print(fife())

