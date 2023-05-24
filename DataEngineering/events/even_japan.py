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







def tsuna(a):
    b="1"
    if a=="None":
        b="0"
    return (b)


def generat_datjapon():
    
    #creo dicc vacio
    dict={'mag':[],'place':[],'time':[],'url':[],'tsunami':[],'title':[],'lng':[],'lat':[],'deepth':[]}

    limit=5

    import datetime
    #creo un bucle para recorrer los diferentes offset sin superar la fecha mínima registrada   
  
        #Obtengo url personalizada para la fecha
    urlP2p = f"https://api.p2pquake.net/v1/human-readable?limit={limit}"
        #hago la request en la api
    responseP2p = requests.get(urlP2p)
        #cambio el formato a tipo json
    jsonDataP2p = responseP2p.json()
        #itero por la cantidad de datos que pedí
    for i in range(limit):
            #intento poblar el diccionario
            try:
                #primero me fijo que pueda acceder a esa fila
                try:a=jsonDataP2p[i]
                except:pass
                #Pueblo el diccionario y en caso de nulos completo el valor con None
                #Magnitud:            
                try:dict['mag'].append(float(a['earthquake']['hypocenter']['magnitude']))
                except:dict['mag'].append(None)
                #Lugar
                try:dict['place'].append(a['points'][0]['addr'])
                except:dict['place'].append(None)
                #Fecha
                try:dict['time'].append(datetime.datetime.strptime(a['time'], '%Y/%m/%d %H:%M:%S.%f'))            
                #try:dict['time'].append(a['time'])
                except:dict['time'].append(None)
                #Url
                #modifico el índice con el que se puede acceder a cada valor
                
                try:dict['url'].append(f"https://api.p2pquake.net/v1/human-readable?limit=1")
                except:dict['url'].append(None)
                #indico si hay tsunami registrado            
                try:dict['tsunami'].append(a['earthquake']["domesticTsunami"])
                except:dict['tsunami'].append(None)
                #Dejo la columna title como complementaria a place          
                try:dict['title'].append(a['earthquake']['hypocenter']['name'])
                except:dict['title'].append(None)
                #Cologo longitud
                try:dict['lng'].append(float(a['earthquake']['hypocenter']['longitude'][1:]))
                except:dict['lng'].append(None)
                #coloco latitud
                try:dict['lat'].append(float(a['earthquake']['hypocenter']['latitude'][1:]))
                except:dict['lat'].append(None)
                #coloco profundidad
                try:dict['deepth'].append(float(a['earthquake']['hypocenter']['depth'][:-2]))
                except:dict['deepth'].append(None)
            except: 
                pass

    df=pd.DataFrame(dict)
    #borro duplicados
    df.drop_duplicates(inplace=True)
    #filtro filas con vacíos
    filtros=[None,'']
    for i in filtros:
        #Creo máscaras 
        m1=df['mag'].values !=i
        m2=df['title'].values !=i
        m3=df['lng'].values !=i
        m4=df['lat'].values !=i
        m5=df['deepth'].values !=i
        #Aplico las máscaras
        df=df[m1 & m2 & m3 & m4 & m5]
    df.insert(loc = 0, column = 'idcountry', value =3)
    
    
    df=df.fillna("no data")
    df["tsunami"]="0"
    df['danger']=1
    
    df=df[df["mag"]>3]
    
    x = np.array(df[["idcountry","mag","tsunami","deepth"]])
    result_x = model.predict(x)
    df["danger"]=result_x
       
    #danger
    df["danger"]=df["danger"].apply(lambda x: nor_danger(x))    
    
    #tsuna
    df["tsunami"]=df["tsunami"].apply(lambda y: tsuna(y))    
    
    df=df.head(1)
    df.rename(columns={"deepth":"depth"},inplace=True)
    
        
    df["place"]=df["place"].str.decode("UTF-8")
    
    df=df.reindex(columns=["time","depth","lat","lng","place","mag","idcountry","tsunami","danger"])
    return(df)



def monitoreo_sismjap():
    import time
    event=generat_datjapon()
    
    while True:
        datos=generat_datjapon()
        if datos is not None:
            
            if (str(datos["time"].iloc[0])!=str(event["time"].iloc[0])):
                a=texto(datos,"JAPAN")
                requests.post("https://api.telegram.org/bot6055516855:AAGQw2iFZQ9Qph-4knJBE-VT5eeXnPZT_58/sendMessage",data={"chat_id":"-988051975","text":a})
            
            
         
                   
        time.sleep(60) 
        






if __name__ == '__main__':
    # Llama a la función que deseas ejecutar
    monitoreo_sismjap()