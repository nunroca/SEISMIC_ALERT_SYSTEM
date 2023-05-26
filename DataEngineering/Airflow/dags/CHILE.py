
from datetime import datetime
import pandas as pd
from datetime import datetime, timedelta
import requests
import time
from dateutil.rrule import rrule, DAILY , MONTHLY 
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
    "retry_delay":timedelta(minutes=1)
    
}

with open('/opt/airflow/data/modelo_ml.pickle', 'rb') as ml:
    model = pickle.load(ml) 

'''================================ CHILE ==========================='''

def get_url_chile():
    import datetime
    dat= datetime.datetime.today() - datetime.timedelta(days=1)
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
    df[['hora2', 'place']] = df['Fecha Local / Lugar'].str.split(' km ', n=1, expand=True)
    df[["mag","etc"]]=df["Magnitud"].str.split(expand=True)
    return(df)


def nor_danger(a):
    b=0
    if   a==0: b=3
    elif a==1: b=1
    elif a==2: b=3
    elif a==3: b=2
    return(b)


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
       
    return(df)

def generat_cadchile():
    
 
    df_ = generat_datchile()

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

    cadena = "INSERT INTO CHILE (idcountry,mag,place,time,tsunami,lng,lat,depth,danger) VALUES" + cadena + ";"

    
    
    
    return (cadena)


'''================================ DAGs ==========================='''



with DAG(dag_id="Sismos_Chile_diary",
         default_args=default_args,
         description="load Sismos",
         start_date=datetime(2023,5,21,1),
         schedule_interval="@daily",
    
 
    
)as dag:


    task_extr_chile = PythonOperator(
        task_id='extrac_chile',
        python_callable=generat_cadchile,
        provide_context=True,
    )         
    
    task_load_chile=MySqlOperator(
        task_id="load_chile",
        sql = "{{ti.xcom_pull(task_ids='extrac_chile')}}",
        mysql_conn_id="mysql_rds",
        autocommit=True
    )
    task_extr_chile>>task_load_chile