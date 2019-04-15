from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import cargo_docente
import string	
import sys

def main(argv):

	tag_html = 'table'

	try:
	    source = urlopen(argv[1])
	except HTTPError as error:
	    print("Erro HTTP, codigo do erro:\n")
	    print(error)
	except URLError:
	    print("Servidor web nao encontrado ou o dominio esta incorreto\n")
	else:
		webScrapping(source,tag_html)

def webScrapping(source,tag_html):
	soup = BeautifulSoup(source.read(),"html5lib")
	tabela = soup.find_all(tag_html)[0].get_text().split('\n')
	dados = []

	for item in tabela:
		if 'lattes.cnpq.br' in item.strip():
			dados.append(item.strip())
		elif item.strip() in string.whitespace:
			pass
		else:
			pass

	cargo_docente.main(dados)

main(sys.argv)