#comandos
1-usar el .yaml modificado  --> en carpeta actual
2-mkdir -p ./dags ./logs ./plugins  --> crear las carpetas dags, logs y plugins
3-echo -e "AIRFLOW_UID=$(id -u)" > .env  --> crear un archivo .env con las variables de entorno, AIRFLOW_UID=50000 en win
4-chequear la version de la imagen de airflow en el yaml si es necesario
5-sudo docker-compose up airflow-init 
6-sudo docker-compose up