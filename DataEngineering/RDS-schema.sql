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


