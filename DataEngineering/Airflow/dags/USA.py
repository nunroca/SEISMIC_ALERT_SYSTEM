
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
    url = f'https://earthquake.usgs.gov/fdsnws/event/1/query?format=csv&starttime={fecha_desde}&endtime={fecha_hasta}&&maxlatitude=50&minlatitude=24.6&maxlongitude=-65&minlongitude=-125&minmagnitude=3&orderby=time-asc'

    # Obtenemos el DataFrame ya procesado
    dt_procesado=pd.read_csv(url,delimiter=',')

    return dt_procesado

def transformar_fecha(dato):
    fecha_sin_tz = dato.replace("T", " ").replace("Z", "")
    fecha_objeto = datetime.strptime(fecha_sin_tz, "%Y-%m-%d %H:%M:%S.%f")
    fecha_formateada = fecha_objeto.strftime("%Y/%m/%d %H:%M:%S")
    return fecha_formateada

def generat_datusa ():
    df=consultarAPIUsa()
    df["place"]=df["place"].fillna("no data")
    df=df.fillna(0)
    df=df.drop_duplicates()
    df=df[["mag","place","time","longitude","latitude","depth"]]
    df['time'] = df['time'].apply(lambda x: transformar_fecha(x))
    df.rename(columns={'latitude':'lat', 'longitude':'lng' }, inplace=True)
    df["idcountry"]=1
    df["tsunami"]=0
    df["danger"]="1"
    df=df[["idcountry","mag","place","time","tsunami","lng","lat","depth","danger"]]
    
    df=df[df["mag"]>3]  
       
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
         start_date=datetime(2023,5,16,1),
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
