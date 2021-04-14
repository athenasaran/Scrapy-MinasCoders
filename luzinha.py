import scrapy
import json

class minhaAranha(scrapy.Spider):
    name = 'minha-aranha'
    start_urls = ['https://lista.mercadolivre.com.br/luzinha#D[A:luzinha,L:undefined]']
    
    def parse(self, response):
        self.log('AQUI {}'.format(response.url))
        
        titulos = response.xpath('//span[@class="main-title"]/text()').extract()
        print(titulos)
        precos = response.xpath('//div[@class="item__price "]//text()').extract()
        print(precos)
        
        resultado = {}



        resultado["titulo"] = titulos

        resultado["preco"] = precos



        tudo = {'luzinha': resultado}
        
        with open('luzinha.json', 'w') as json_file:
            json.dump(tudo,json_file)


