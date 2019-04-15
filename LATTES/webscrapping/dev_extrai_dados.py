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

def main(argv):
	try:
	    source = urlopen('http://buscatextual.cnpq.br/buscatextual/visualizacv.do?metodo=apresentar&id=K4234034J5')
	except HTTPError as error:
	    print("Erro HTTP, codigo do erro:\n")
	    print(error)
	except URLError:
	    print("Servidor web nao encontrado ou o dominio esta incorreto")
	else:
		webScrapping(source)

def webScrapping(source):
	soup = BeautifulSoup(source.read(),"html5lib")

	nome = soup.find_all('h2',class_='nome')[0].get_text()
	atualizacao = soup.find_all('ul',class_='informacoes-autor')[0].find_all('li')[1].get_text()
	qualificacao = soup.find_all('p',class_='resumo')[0].get_text()
	body = soup.find_all('div',class_='content-wrapper')[0].get_text()

	print('Nome: ', nome)
	print(atualizacao)
	print(qualificacao)
	print(body)
	
	os.system("PAUSE")

if __name__ == "__main__":
    main(sys.argv)

"""
	f = open('lattes.txt','wb')
	for line in dados_brutos:
		f.write(line.encode(sys.stdout.encoding, errors='replace'))
	f.close()
"""