import requests
import json
from bs4 import BeautifulSoup

url = 'https://lista.mercadolivre.com.br/gamer#D[A:gamer,L:undefined]'

headers = {"User-Agent" : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0'}

page = requests.get(url, headers=headers)

sopa = BeautifulSoup(page.content,'html.parser')

gamer = sopa.find(id='searchResults')

itensgamer = gamer.find_all(class_='results-item highlighted article stack product ')

todasgamerstitulo = [item.find("span", class_='main-title').get_text() for item in itensgamer]

todasgamerspreco = [itens.find(class_='price__container').get_text() for itens in itensgamer]

resultado = {}

resultado["titulo"] = todasgamerstitulo
resultado["preco"] = todasgamerspreco

tudo = {'gamer': resultado}

print(json.dumps(tudo))