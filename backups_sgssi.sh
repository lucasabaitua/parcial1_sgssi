#!/bin/bash

#Funciones para llevar acabo el backup de los archivos de la carpeta /home/user/Escritorio/Seguridad#
#Para el uso en otro tipo de ejercicios cambiar directorios#


#Crea una carpeta donde se guardaran los backups en la direccion /var/tmp/ llamada Backups#
#Dentro de la carpeta crearemos 2:
# 	1. Para backups de los archivos de Seguridad (Seg)
#	2. Para backup de la BD del workbench (BD)

fecha=`date +%d-%m-%y`
fechaAnt=`date -d yesterday +%d-%m-%y`      
# guarda la fecha actual y la del dia anterior en caso de hacer una copia incremental del anterior día #                       
cd /var/tmp/Backups/Seg
mkdir $fecha

# creamos el directorio del backup de este día
cd /home/lucas/Escritorio/Seguridad 
vacio= $(ls /var/tmp/Backups/Seg/$fechaAnt | grep “$fechaAnt”)

# comprobamos si existe un backup anterior para hacer una copia incremental o si no hacer una completa
if [ -z $vacio ]
then       
	rsync -av /home/lucas/Escritorio/Seguridad/  /var/tmp/Backups/Seg/$fecha
else 
	rsync -av --link-dest=/var/tmp/Backups/Seg/$fechaAnt . /var/tmp/Backups/Seg/$fecha
fi 

# vamos a la carpeta dedicada al guardado de la base de datos y la exportamos a una carpeta creada del día actual
cd /var/tmp/Backups/BD
mkdir $fecha
mysqldump -u 'root' -p'1234' 'sgssi' > /var/tmp/Backups/BD/$fecha/backup_SGSSI.sql

