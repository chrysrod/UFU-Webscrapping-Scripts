from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import re

universidade = 'Universidade Federal de Uberlândia'
palavra_chave = 'Professor'

def main(links):

	print('\nAcompanhamento em tempo real\n')

	for link in links:
		try:
		    source = urlopen(link)
		except HTTPError as error:
		    print("Erro HTTP, codigo do erro:\n")
		    print(error)
		except URLError:
		    print("Servidor web nao encontrado ou o dominio esta incorreto")
		else:
			webScrapping(source, universidade, palavra_chave)

	

def webScrapping(source, universidade, palavra_chave):
	soup = BeautifulSoup(source.read(),"html5lib")
	nome = soup.find_all('h2',class_='nome')[0].get_text()
	resumo = soup.find_all('p',class_='resumo')[0].get_text()
	frases = re.split('[.;]', resumo)

	f = open('cargo_lattes.txt','a')
	for linha in frases:
		if universidade.upper() in linha.upper():
			if palavra_chave.upper() in linha.upper():
				print('------------------------------------------------------------------------------------------------------------------------\n')
				print(nome+'\n')
				print(linha.strip()+'\n')
				print('------------------------------------------------------------------------------------------------------------------------\n')
				f.write(linha.strip()+'\n')
			elif (palavra_chave.upper()+'a') in linha.upper():
				print('------------------------------------------------------------------------------------------------------------------------\n')
				print(nome+'\n')
				print(linha.strip()+'\n')
				print('------------------------------------------------------------------------------------------------------------------------\n')
				f.write(linha.strip()+'\n')
	f.close()