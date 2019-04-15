#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

def main():

	source = urlopen('http://www.novo.ifilo.ufu.br/graduacao/filosofia/fichas-de-disciplinas')
	tag_html = 'tbody'

	webScrapping(source,tag_html)

def webScrapping(source,tag_html):
	soup = BeautifulSoup(source.read(),"html5lib")
	tabela = soup.find_all(tag_html)[0].get_text().split('\n')
	dados = []

	for item in tabela:
		if item.strip() in string.whitespace:
			pass
		else:
			dados.append(item.strip())

	file = open('fichas_disciplinas_site_antigo.txt','r')
	
	for i in file:
		check = 0
		for item in dados:
			if i[:6] in item:
				print('Disciplina confere ', i)
				check = 1
		if check == 0:
			print('Disciplina não confere ', i)
	file.close()

if __name__ == "__main__":
	main()