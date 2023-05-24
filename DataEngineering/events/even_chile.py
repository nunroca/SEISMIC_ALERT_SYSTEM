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

 
  
    

def get_url_chile():
    import datetime
    dat= datetime.datetime.today()
    year=dat.strftime("%Y")
    month=dat.strftime("%m")
    day=dat.strftime('%Y%m%d')

    url=f"https://www.sismologia.cl/sismicidad/catalogo/{year}/{month}/{day}.html"
    urlx = requests.get (url)
    soup = BeautifulSoup(urlx.content,"html.parser")
    rows = soup.find("table", attrs={"class":"sismologia detalle"}).find_all("tr")
    return  (rows)

def transformar_fecha(dato):
    from datetime import datetime
    fecha_objeto = datetime.strptime(dato, "%Y-%m-%d %H:%M:%S")
    fecha_formateada = fecha_objeto.strftime("%Y/%m/%d %H:%M:%S")
    return fecha_formateada



def dat_inic_chil():
    data=[]
    rows=get_url_chile()
        
    for row in rows:
        cells = row.find_all("td")
        row_data = []
        for cell in cells:
            row_data.append(cell.text.strip())
        data.append(row_data)
    
     
    df =pd.DataFrame(data, columns=["Fecha Local / Lugar","Fecha UTC","Latitud / Longitud","Profundidad","Magnitud"])
    df=df.dropna(how="all")
    df['Fecha UTC'] = df['Fecha UTC'].apply(lambda x: transformar_fecha(x))
    df=df.fillna(0)
    df=df.drop_duplicates()
    df[['lat', 'lng']] = df['Latitud / Longitud'].str.split(expand=True)
    df[['hora2', 'place']] = df['Fecha Local / Lugar'].str.split(' ', n=1, expand=True)
    df["place"]=df["place"].str[8:]
    df[["mag","etc"]]=df["Magnitud"].str.split(expand=True)
    return(df)




def generat_datchile():

    df=dat_inic_chil()

    df.rename(columns={"Profundidad":"depth","Fecha UTC":"time" }, inplace=True)
    df["depth"]=df["depth"].str.replace(" km","")
    df["mag"]=df["mag"].str.replace(" M","")
    
    df["mag"]=df["mag"].astype(float)
    df["depth"]=df["depth"].astype(float)
    df["lat"]=df["lat"].astype(float)
    df["lng"]=df["lng"].astype(float)
    df["place"]=df["place"].astype(str)
        
    df["idcountry"]=2
    df["tsunami"]=0
    df["danger"]=1

    df=df[df["mag"]>=3]

    df.drop(["Fecha Local / Lugar","Latitud / Longitud","hora2","etc","Magnitud"],axis=1,inplace=True)
    
    
    x = np.array(df[["idcountry","mag","tsunami","depth"]])
    result_x = model.predict(x)
    df["danger"]=result_x
    
    #danger
    df["danger"]=df["danger"].apply(lambda x: nor_danger(x))
    
    df=df.head(1)   
    return(df)









def monitoreo_sismchi():
    import time
    event=generat_datchile()
    
    while True:
        datos=generat_datchile()
        if datos is not None:
            
            if (str(datos["time"].iloc[0])!=str(event["time"].iloc[0])):
               
               
                event=datos
                a=texto(datos,"CHILE")
                requests.post("https://api.telegram.org/bot6055516855:AAGQw2iFZQ9Qph-4knJBE-VT5eeXnPZT_58/sendMessage",data={"chat_id":"-988051975","text":a})
                               
        time.sleep(60)


if __name__ == '__main__':
    # Llama a la función que deseas ejecutar
    monitoreo_sismchi()