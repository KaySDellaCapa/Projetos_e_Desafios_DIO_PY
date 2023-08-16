# É um programa de analise

from bs4 import BeautifulSoup
import requests

# Recebendo o conteudo da requisição http do site.
site = requests.get('https://www.climatempo.com.br/').content #pega todo o código HTML do site que passar
# ESTE SITE É APENAS UM EXEMPLO

# Está baixando do site o HTML desse site.
soup = BeautifulSoup(site, "html.parser")

# Transforma o HTML em string e o print vai exibir o HTML
print(soup.prettify())

# temperatura = soup.find('span', class_='_block_margins-b-5 -gray')
# print(temperatura.string)
# PARA ENCONTRAR ALGO ESPECIFICO DENTRO DO CÓDIGO

print(soup.find('admin'))