#https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html
from airflow import DAG
from datetime import datetime, timedelta
from airflow.decorators import dag
from airflow.operators.python import PythonOperator
from airflow.decorators import task
import pendulum
from airflow.operators.mysql_operator import MySqlOperator

def saludar():
    print('hello world iam working')

sql_query= "insert into ficha(id, nombre, apellido) values (1, 'juan', 'araoz');"


#dag creation

default_args={
    'owner': 'Airflow',
    'start_date': pendulum.datetime(2023,5,16),
    'retries': 3,
    'retry_delay': timedelta(seconds=5)

}

dag = DAG(
    'mi_primer_test',
    default_args=default_args,
    description='enviar hola mundo cada hora',
    schedule_interval= timedelta(minutes=5)
)

saludarxd = PythonOperator(
    task_id = 'solo_saludar',
    python_callable=saludar ,
    dag=dag 
)


@task(task_id='despedida', dag=dag)
def despedirse():
    print('adios')
chau = despedirse()

insert_query = MySqlOperator(sql= sql_query, task_id='insertSQL', dag=dag, mysql_conn_id="mysql_conn")

saludarxd >> chau >> insert_query