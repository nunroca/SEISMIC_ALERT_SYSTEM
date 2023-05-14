# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv
import scrapy
from scrapy import signals
from scrapy.exporters import CsvItemExporter



class JaponDatosPipeline:
    def process_item(self, item, spider):
        return item


class TerremotosPipeline:
    def __init__(self):
        self.archivo = None
        self.escritor = None
    
    def open_spider(self, spider):
        self.archivo = open("terremotos.csv", "w", newline="")
        campos = ["hora_fecha", "latitud", "longitud", "magnitud", "profundidad", "lugar"]
        self.escritor = csv.DictWriter(self.archivo, fieldnames=campos)
        self.escritor.writeheader()
    
    def close_spider(self, spider):
        if self.archivo is not None:
            self.archivo.close()
    
    def process_item(self, item, spider):
        self.escritor.writerow(item)
        return item