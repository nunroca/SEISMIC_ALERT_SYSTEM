
from datetime import datetime
import pandas as pd
from datetime import datetime, timedelta
import requests
import time
from dateutil.rrule import rrule, DAILY , MONTHLY 

import requests
from bs4 import BeautifulSoup

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.mysql_operator import MySqlOperator


#ml
import pickle
import numpy as np
from sklearn.cluster import KMeans




default_args={
    "owner":"esrock",
    "retries":5,
    "retry_delay":timedelta(minutes=2)
    
}




with open('/opt/airflow/data/modelo_ml.pickle', 'rb') as ml:
    model = pickle.load(ml) 




'''================================ USA ==========================='''

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
    url = f'https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime={fecha_desde}&endtime={fecha_hasta}&&maxlatitude=50&minlatitude=24.6&maxlongitude=-65&minlongitude=-125&minmagnitude=3&orderby=time-asc'

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
    
    
    
def nor_danger(a):
    b=0
    if   a==0: b=3
    elif a==1: b=1
    elif a==2: b=3
    elif a==3: b=2
    return(b)    
    
 
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
       
    return df

def generat_cadusa():
    '''
    Extrae los datos de USA del mes actual
    y nos quedamos con los del día de ayer, si los hay
    '''
    df_ = generat_datusa()

    # Creamos las listas para armar la cadena sql
    
    idcountry = list(df_["idcountry"])
    mag = list(df_['mag'])
    place = list(df_['place'])
    time = list(df_['time'])
    tsunami = list(df_["tsunami"])
    lng = list(df_['lng'])
    lat = list(df_['lat'])
    depth = list(df_['depth'])
    danger = list(df_['danger'])

    # Armamos la cadena
    cadena = list(zip(idcountry,mag,place,time,tsunami,lng,lat,depth,danger))
    cadena = str(cadena)
    cadena = cadena[1 : -1]

    cadena = "INSERT INTO USA (idcountry,mag,place,time,tsunami,lng,lat,depth,danger) VALUES" + cadena + ";"


    return cadena

'''================================ DAGs ==========================='''



with DAG(dag_id="Sismos_USA_diary",
         default_args=default_args,
         description="load sismos",
         start_date=datetime(2023,5,21,1),
         schedule_interval="@daily",
    
 
    
)as dag:

    task_extr_usa = PythonOperator(
        task_id='extrac_usa',
        python_callable=generat_cadusa,
        provide_context=True,
    )         
    
    task_load_usa=MySqlOperator(
        task_id="load_usa",
        sql = "{{ti.xcom_pull(task_ids='extrac_usa')}}",
        mysql_conn_id="mysql_rds",
        autocommit=True     
    )
    task_extr_usa>>task_load_usa
