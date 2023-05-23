
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




default_args={
    "owner":"esrock",
    "retries":5,
    "retry_delay":timedelta(minutes=2)
    
}

'''================================ JAPAN ==========================='''

def japon_instantanea():
    
    #creo dicc vacio
    dict={'mag':[],'place':[],'time':[],'url':[],'tsunami':[],'title':[],'lng':[],'lat':[],'deepth':[]}

    limit=10

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
    df.insert(loc = 0, column = 'idpais', value =3)
    
    
    fecha_hasta = datetime.datetime.today()
    ayer=fecha_hasta.date() - timedelta(days=1)
    mask=df["time"].dt.date>ayer
    df=df[mask]
    df=df.fillna("no data")
    df["tsunami"]="0"
    df['danger']=1
    
    df=df[df["mag"]>3]
    
    return(df)








def generat_cadjap():
    '''
    Extrae los datos de USA del mes actual
    y nos quedamos con los del día de ayer, si los hay
    '''
    import datetime
    df=japon_instantanea()

    # Creamos las listas para armar la cadena sql
    
    idcountry = list(df["idpais"])
    mag = list(df['mag'])
    place = list(df['place'])
    time = list(df['time'])
    tsunami = list(df['tsunami'])
    lng = list(df['lng'])
    lat = list(df['lat'])
    depth = list(df['deepth'])
    danger = list(df['danger'])

    # Armamos la cadena
    cadena = list(zip(idcountry,mag,place,time,tsunami,lng,lat,depth,danger))
    cadena = str(cadena)
    cadena = cadena[1 : -1]

    cadena = "INSERT INTO JAPAN (idcountry,mag,place,time,tsunami,lng,lat,depth,danger) VALUES" + cadena + ";"

    return cadena



'''================================ DAGs ==========================='''



with DAG(dag_id="Sismos_JAPAN_diary",
         default_args=default_args,
         description="load sismos",
         start_date=datetime(2023,5,17,1),
         schedule_interval="@daily",
    
 
    
)as dag:

    task_extr_jap = PythonOperator(
        task_id='extrac_jap',
        python_callable=generat_cadjap,
        provide_context=True,
    )         
    
    task_load_jap = MySqlOperator(
        task_id="load_jap",
        sql = "{{ti.xcom_pull(task_ids='extrac_jap')}}",
        mysql_conn_id="mysql_rds",
        autocommit=True     
    )
    task_extr_jap>>task_load_jap
