# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JaponDatosItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()


    #datos del sismo
    fecha = scrapy.Field()
    latitud = scrapy.Field()
    longitud = scrapy.Field()
    magnitud = scrapy.Field()
    profundidad = scrapy.Field()
    lugar = scrapy.Field()
    



    pass
