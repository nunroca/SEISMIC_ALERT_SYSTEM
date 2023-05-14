# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from japon_datos.items import JaponDatosItem
from scrapy.exceptions import CloseSpider
import csv



class japondatosspider(CrawlSpider):
    name = "japond"
    start_urls = ['https://www.data.jma.go.jp/multi/quake/index.html?lang=es']

    rules = [
        Rule(LinkExtractor(restrict_xpaths="//table[@id='quakeindex_table']//td[1]/a"), callback='parse_pagina'),
    ]
    
    def parse_pagina(self, response):
        # Extraer información de la página y guardarla en un archivo CSV
        tabla = response.xpath("//table[@id='earthquake_table']")[0]
        filas = tabla.xpath(".//tr")
        
        with open("terremotos.csv", "a", newline="") as archivo:
            escritor = csv.writer(archivo)
            
            for fila in filas:
                celdas = fila.xpath(".//td/text()").extract()
                
                if len(celdas) > 0:
                    hora_fecha = celdas[0]
                    latitud = celdas[1]
                    longitud = celdas[2]
                    magnitud = celdas[3]
                    profundidad = celdas[4]
                    lugar = celdas[5]
                    
                    escritor.writerow([hora_fecha, latitud, longitud, magnitud, profundidad, lugar])