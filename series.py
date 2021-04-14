import requests
import pandas as pd
from bs4 import BeautifulSoup
import csv

page = requests.get('https://www.minhaserie.com.br/series')
soup = BeautifulSoup(page.content, 'html.parser')
series = soup.find("div",class_='card-list')

itens = series.find_all("li", class_='vertical')

itenstitulos = [item.find("h2", class_='info-title').get_text() for item in itens]

itensvotos = [item.find("div", class_='ratingbox current').get_text() for item in itens]

itensvisitas = [item.find("div", class_='rate-info').get_text() for item in itens]

itensestilos = [item.find("span", class_='cat').get_text() for item in itens]

itensdescricoes = [item.find('p').get_text() for item in itens]



coisas_de_serie = pd.DataFrame(
    {
        'titulos': itenstitulos,
        'votos': itensvotos,
        'visitas': itensvisitas,
        'estilos': itensestilos,
        'descricoes': itensdescricoes
    })
print(coisas_de_serie)
coisas_de_serie.to_csv('VamoLaDnv.csv')
