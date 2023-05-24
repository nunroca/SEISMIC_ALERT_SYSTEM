from datetime import datetime
import pandas as pd
from datetime import datetime, timedelta
import requests
import time
from dateutil.rrule import rrule, DAILY , MONTHLY 
from bs4 import BeautifulSoup

#ml
import pickle
import numpy as np
from sklearn.cluster import KMeans

import json
from urllib.request import urlopen


with open('modelo_ml.pickle', 'rb') as ml:
    model = pickle.load(ml) 

def bot(a:str):
    r=requests.post("https://api.telegram.org/bot6055516855:AAGQw2iFZQ9Qph-4knJBE-VT5eeXnPZT_58/sendMessage",
                    data={"chat_id":"-988051975","text":a})
    data=json.loads(r.text)

def texto(a,pais:str):
    time=str(a["time"].iloc[0])
    depth=str(a["depth"].iloc[0])
    lat=str(a["lat"].iloc[0])
    lng=str(a["lng"].iloc[0])
    place=str(a["place"].iloc[0])
    mag=str(a["mag"].iloc[0])
    idcountry=pais
    tsunami=str(a["tsunami"].iloc[0])
    danger=str(a["danger"].iloc[0])
    b="country: "+idcountry+"\n"+"place: "+place+"\n"+"time: "+time+"\n"+"magnitude: "+mag+"\n"+"depth: "+depth+"\n"+"latitud: "+lat+"\n"+"longitude: "+lng+"\n"+"sismo tipo "+danger
    return b

def nor_danger(a):
    b=0
    if   a==8: b=3
    elif a==6: b=2
    elif a==2: b=2
    elif a==0: b=2
    elif a==7: b=2
    elif a==3: b=1
    elif a==9: b=1
    elif a==1: b=1
    elif a==4: b=1
    return(b)


def consultarAPIUsa():
    '''
    Consulta la API de USA
    -> DataFrame
    '''
    import datetime as dt
    # Definimos las fechas desde y hasta para la url
    fecha_hasta = dt.datetime.today() 
    fecha_desde = fecha_hasta - dt.timedelta(days=1)
    
    # Formateamos las fechas
    fecha_desde = dt.datetime.strftime(fecha_desde, '%Y-%m-%d')
    fecha_hasta = dt.datetime.strftime(fecha_hasta, '%Y-%m-%d')

    # armamos la url
    url = f'https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime={fecha_desde}&endtime=2023-12-31%2023:59:59&maxlatitude=50&minlatitude=24.6&maxlongitude=-65&minlongitude=-125&minmagnitude=3&orderby=time-asc'

    # Obtenemos el DataFrame ya procesado
   
    resp = requests.get(url).json()

    # Guardamos los datos en formato diccionario
    dict={'mag':[],'place':[],'time':[],'url':[],'tsunami':[],'title':[],'lng':[],'lat':[],'deepth':[]}
    #recorremos la catidad de "filas" que tiene
    for i in range(len(resp['features'])):
        
        a=resp['features'][i]
        #agrego al diccionario magnitud, tiempo, si produjo tsunami 
        lista_propierties=['mag','time']
        for elemento in lista_propierties:
            if a['properties'][elemento]is None:
                dict[elemento].append(np.nan) 
            else:
                dict[elemento].append(float(a['properties'][elemento]))
                
        #agrego lugar, url con información a ampliar y el título     
        lista_propierties2=['place','url','title','tsunami']
        for elemento in lista_propierties2:
            if a['properties'][elemento]is None:
                dict[elemento].append(None)
            else:
                dict[elemento].append(a['properties'][elemento])

        #Agrego al diccionario latitud, longitud y profundidad
        list_geometry=['lng','lat','deepth']
        for indice, elemento in enumerate(list_geometry):
            if a['geometry']['coordinates'][indice] is None:
                dict[elemento].append(np.nan)
            else:
                dict[elemento].append(float(a['geometry']['coordinates'][indice]))

    #Devuelvo el diccionario hecho df
    return (pd.DataFrame(dict))    
    

def generat_datusa ():
    
    import datetime 
    
    df=consultarAPIUsa()
    
        
    df["place"]=df["place"].fillna("no data")
    df=df.fillna(0)
    df=df.drop_duplicates()
    df=df[["mag","place","time","lng","lat","deepth","tsunami"]]
    
    #corregimos las fechas
    df.time=df.time.apply(lambda x: datetime.datetime.fromtimestamp(int(x)//1000).strftime('%Y-%m-%d %H:%M:%S.%f') if x!=np.nan else x)
    #pasamos a formato fecha
    df.time=df.time.apply(lambda x: datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f') if x!=np.nan else x)
    
   
    df.rename(columns={'deepth':'depth' }, inplace=True)
    df["idcountry"]=1
    df["danger"]=1
    df=df[["idcountry","mag","place","time","tsunami","lng","lat","depth","danger"]]
    
    
    df=df[df["mag"]>3]  
   
    x = np.array(df[["idcountry","mag","tsunami","depth"]])
    result_x = model.predict(x)
    df["danger"]=result_x
    
    #danger
    df["danger"]=df["danger"].apply(lambda x: nor_danger(x))      
    df=df.sort_values("time",ascending=False)  
    df=df.head(1)
    df=df.reindex(columns=["time","depth","lat","lng","place","mag","idcountry","tsunami","danger"])
    return df







def monitoreo_sismusa():
    import time
    event=generat_datusa()
    
    while True:
        datos=generat_datusa()
        if datos is not None:
            
            if (str(datos["time"].iloc[0])!=str(event["time"].iloc[0])):
                event=datos
                a=texto(datos,"USA")
                requests.post("https://api.telegram.org/bot6055516855:AAGQw2iFZQ9Qph-4knJBE-VT5eeXnPZT_58/sendMessage",data={"chat_id":"-988051975","text":a})
             
                
        time.sleep(60)


if __name__ == '__main__':
    # Llama a la función que deseas ejecutar
    monitoreo_sismusa()