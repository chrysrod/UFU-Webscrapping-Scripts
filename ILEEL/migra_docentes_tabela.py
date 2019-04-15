#!/usr/bin/env python
#-*- coding: utf-8 -*-
#K:/Chrystian/Python/ILEEL/dev.py

from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import string	
import time
import re
import sys
import os

def main(argv):

	try:
	    source = urlopen(argv[1])
	except HTTPError as error:
	    print("Erro HTTP, codigo do erro:\n")
	    print(error)
	except URLError:
	    print("Servidor web nao encontrado ou o dominio esta incorreto\n")
	else:
		webScrappingTabelas(source)

def webScrappingTabelas(source):

	data = []
	soup = BeautifulSoup(source.read(),"html5lib")
	tabela = soup.find('table')
	tabela_body = tabela.find('tbody')
	linhas = tabela_body.find_all('tr')
	
	for linha in linhas:
	    cols = linha.find_all('td')
	    cols = [ele.text.strip() for ele in cols]
	    data.append([ele for ele in cols if ele]) # Get rid of empty values

	csvGenerator(data)

def csvGenerator(data):

	file = open("K:/Chrystian/Python/ILEEL/docentes_famev.csv","w")
	cont = 0

	for linha in data:
		for elemento in linha:
			if cont == 0:
				file.write('"' + elemento + '"' + ',')
			elif cont == 3:
				file.write('"' + elemento + '"')
			else:
				file.write('"' + elemento + '"' + ',')
			cont += 1
		file.write("\n")
		cont = 0

	file.close()

if __name__ == "__main__":
    main(sys.argv)