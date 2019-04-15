from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
from lxml import etree
import string	
import time
import re
import sys
import os

def main(link):
	try:
	    source = urlopen('http://buscatextual.cnpq.br/buscatextual/visualizacv.do?metodo=apresentar&id=K4253617A7')
	except HTTPError as error:
	    print("Erro HTTP, codigo do erro:\n")
	    print(error)
	except URLError:
	    print("Servidor web nao encontrado ou o dominio esta incorreto")
	else:
		webScrapping(source)

def webScrapping(source):
	soup = BeautifulSoup(source.read(),"html5lib")
	resumo = soup.find_all('p',class_='resumo')[0].get_text()
	frases = re.split('[.;]', resumo)

	universidade = 'Universidade Federal de Uberlândia'
	termo = 'professor'

	f = open('lattes.txt','a')
	for linha in frases:
		if universidade.upper() in linha.upper() and termo.upper() in linha.upper():
			f.write(linha+'\n')
	f.close()