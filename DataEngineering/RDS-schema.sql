use alertasSismicas;
show tables;

#It gives permissions to import csv
GRANT SESSION_VARIABLES_ADMIN ON *.* TO juanAdmin;

#create tables 
create table historical_japan(
   id_jp int primary key,
   time datetime,
   lat float,
   lng float,
   depth_ float,
   mag decimal(2,1),
   place varchar(100),
   country varchar(10)
);

create table historical_usa(
   id_usa int primary key,
   time datetime,
   lat float,
   lng float,
   depth_ float,
   mag decimal(2,1),
   place varchar(100),
   country varchar(10)
);

create table historical_chile(
   id_cl int primary key,
   time datetime,
   lat float,
   lng float,
   depth_ float,
   mag decimal(2,1),
   place varchar(100),
   country varchar(10)
);

#Linux terminal command to import
/*sudo mysqlimport --local 
 --user=**** 
 --password=**** 
 --host=database-alertas-sismicas.crcnepco0igw.us-east-1.rds.amazonaws.com 
 --fields-terminated-by=',' 
 --fields-enclosed-by='"' 
 --lines-terminated-by="\n" 
 --ignore-lines=1  alertasSismicas /var/lib/mysql-files/historical_japan.csv */

#considerations

#1-csv file name has to be the same name as the table name it will be in.
#2-if the file is in /var/lib/mysql-files (secure-priv location) the command has to start with sudo because is a root folder.

select * from historical_japan limit 10;
select * from historical_usa limit 10;
select * from historical_chile limit 10;

create table historical_mar_japan(
       id_mjp int primary key,
       country varchar(10),
       mxwatheight decimal(3,2),
       place varchar(80),
       time datetime,
       mag decimal(2,1),
       lng float,
       lat float,
       depth_ float
);

create table historical_mar_usa(
       id_mus int primary key,
       country varchar(10),
       mxwatheight decimal(3,2),
       place varchar(80),
       time datetime,
       mag decimal(2,1),
       lng float,
       lat float,
       depth_ float
);

create table historical_mar_chile(
       id_mcl int primary key,
       country varchar(10),
       mxwatheight decimal(3,2),
       place varchar(80),
       time datetime,
       mag decimal(2,1),
       lng float,
       lat float,
       depth_ float
);
##
-- IMPLEMENTACION DE TRIGERS 
## 
DROP TABLE FACTS2;
#creacion de la tabla FACTS2
CREATE TABLE FACTS2( 
 FactId VARCHAR(20) , 
idcountry INT, 
 mag DOUBLE,  
 place text,
 time timestamp, 
 tsunami text, 
 Ing DOUBLE,  
 lat DOUBLE,
 depth DOUBLE,  
 danger smallint,    
 primary KEY (FactId),
 foreign key (idcountry) references COUNTRIES(idcountry)
 );


#DATOS DE TEST 
INSERT INTO JAPAN 
VALUES(14725,1, 4.3, 'xxx35 km S of Shizunai-furukawach?, Japan', '2023-01-06 20:39:40', 0, 142.291, 42.017, 70.2, 1);
INSERT INTO USA 
VALUES(16505,3, 4.3, 'xxx35 km S of Shizunai-furukawach?, Japan', '2023-01-06 20:39:40', 0, 142.291, 42.017, 70.2, 1);
INSERT INTO CHILE
VALUES(9340,3, 4.3, 'xxx35 km S of Shizunai-furukawach?, Japan', '2023-01-06 20:39:40', 0, 142.291, 42.017, 70.2, 1);
#VER LO DATOS DE MANERA DECENDENTE
SELECT *  FROM CHILE 
ORDER BY idsismo DESC 
LIMIT 100;

truncate TABLE FACTS2;
#ELIMINACION DE DATOS DE TEST 
DELETE FROM JAPAN
where idsismo=14725;
DELETE FROM USA
where idsismo=16505;
DELETE FROM CHILE
where idsismo=9340;
#DATOS DE LA TABLA FACTS2
select * from FACTS2;
DROP trigger FACTS2_AI_CHILE;
#CREANDO LOS TRIGER PARA CADA PAIS 
CREATE TRIGGER FACTS2_AI_JAPAN after insert on JAPAN 
for each row 
INSERT INTO FACTS2(FactId,idcountry,mag,place,time,tsunami,Ing,lat,depth,danger) 
VALUES (CONCAT(NEW.idcountry, '-', NEW.idsismo), 
				NEW.idcountry,NEW.mag,NEW.place,NEW.time,                
                NEW.tsunami,NEW.lng,NEW.lat,NEW.depth,NEW.danger);

CREATE TRIGGER FACTS2_AI_CHILE after insert on CHILE 
for each row 
INSERT INTO FACTS2(FactId,idcountry,mag,place,time,tsunami,Ing,lat,depth,danger) 
VALUES (CONCAT(NEW.idcountry, '-', NEW.idsismo), 
				NEW.idcountry,NEW.mag,NEW.place,NEW.time,                
                NEW.tsunami,NEW.lng,NEW.lat,NEW.depth,NEW.danger);
	
CREATE TRIGGER FACTS2_AI_USA  after insert on USA 
for each row 
INSERT INTO FACTS2(FactId,idcountry,mag,place,time,tsunami,Ing,lat,depth,danger) 
VALUES (CONCAT(NEW.idcountry, '-', NEW.idsismo), 
				NEW.idcountry,NEW.mag,NEW.place,NEW.time,                
                NEW.tsunami,NEW.lng,NEW.lat,NEW.depth,NEW.danger);
