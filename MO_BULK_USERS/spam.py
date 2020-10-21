#!/usr/bin/python

import datetime
import calendar
import sys
import os
import argparse
import subprocess
from datetime import  timedelta


print("##########Consulta cantidad de mensajes##########\n")
#####################Ingreso Consulta#############################
fecha_str= datetime.datetime.now().strftime('%Y%m%d')
#fecha_str= str(input("Ingrese Fecha <YYYYMMDD>: "))
entity= "1021"#str(input("Ingrese ID interfaz (ej:1027): "))
limit= "5"#str(input("Ingrese cantidad limite de resultados: "))
fecha_datatime= datetime.datetime.strptime(fecha_str, '%Y%m%d')
dia= fecha_str[6:8]
mes= fecha_str[4:6]
anio= fecha_datatime.year
day= dia
###################Obtengo dia de semana###########################

dicdias = {'MONDAY':'Lunes','TUESDAY':'Martes','WEDNESDAY':'Miercoles','THURSDAY':'Jueves', \
                 'FRIDAY':'Viernes','SATURDAY':'Sabado','SUNDAY':'Domingo','JANUARY':'Enero','February':'Febrero','MARCH':'Marzo','APRIL':'Abril','MAY':'Mayo','JUNE':'Junio','JULY':'Julio','AUGUST':'Agosto','SEPTEMBER':'Septiembre','NOVEMBER':'Noviembre','DECEMBER':'Diciembre'}
fecha = datetime.date(int(anio),int( mes), int(dia))
a= (dicdias[fecha.strftime('%A').upper()]) #type string
b= (dicdias[fecha.strftime('%B').upper()]) 

print("Busqueda de Mensajes del dia "+a+" "+dia+" del mes de "+b+"\n")
#####################################Genero Nombre de Tabla CDR############################

if a == "Lunes":
    delta= timedelta(days=0)
    cdr_fecha= fecha_datatime - delta
    mes_d= cdr_fecha.month
    dia_d= cdr_fecha.day
    anio_d= cdr_fecha.year
    if len(str(dia_d))< 2:
        dia_d= "0"+str(dia_d)
    if len(str(mes_d))< 2:
        mes_d= "0"+str(mes_d)
    cdr= "cdr_"+str(anio)+"_"+str(mes_d)+"_"+str(dia_d)
elif a == "Martes":
    delta= timedelta(days=1)
    cdr_fecha= fecha_datatime - delta
    mes_d= cdr_fecha.month
    dia_d= cdr_fecha.day
    anio_d= cdr_fecha.year
    if len(str(dia_d))< 2:
        dia_d= "0"+str(dia_d)
    if len(str(mes_d))< 2:
        mes_d= "0"+str(mes_d)
    cdr= "cdr_"+str(anio_d)+"_"+str(mes_d)+"_"+str(dia_d)
elif a == "Miercoles":
    delta= timedelta(days=2)
    cdr_fecha= fecha_datatime - delta
    mes_d= cdr_fecha.month
    dia_d= cdr_fecha.day
    anio_d= cdr_fecha.year
    if len(str(dia_d))< 2:
        dia_d= "0"+str(dia_d)
    if len(str(mes_d))< 2:
        mes_d= "0"+str(mes_d)
    cdr= "cdr_"+str(anio_d)+"_"+str(mes_d)+"_"+str(dia_d)
elif a == "Jueves":
    delta= timedelta(days=3)
    cdr_fecha= fecha_datatime - delta
    mes_d= cdr_fecha.month
    dia_d= cdr_fecha.day
    anio_d= cdr_fecha.year
    if len(str(dia_d))< 2:
        dia_d= "0"+str(dia_d)
    if len(str(mes_d))< 2:
        mes_d= "0"+str(mes_d)
    cdr= "cdr_"+str(anio_d)+"_"+str(mes_d)+"_"+str(dia_d)
elif a == "Viernes":
    delta= timedelta(days=4)
    cdr_fecha= fecha_datatime - delta
    mes_d= cdr_fecha.month
    dia_d= cdr_fecha.day
    anio_d= cdr_fecha.year
    if len(str(dia_d))< 2:
        dia_d= "0"+str(dia_d)
    if len(str(mes_d))< 2:
        mes_d= "0"+str(mes_d)
    cdr= "cdr_"+str(anio_d)+"_"+str(mes_d)+"_"+str(dia_d)
elif a == "Sabado":
    delta= timedelta(days=5)
    cdr_fecha= fecha_datatime - delta
    mes_d= cdr_fecha.month
    dia_d= cdr_fecha.day
    anio_d= cdr_fecha.year
    if len(str(dia_d))< 2:
        dia_d= "0"+str(dia_d)
    if len(str(mes_d))< 2:
        mes_d= "0"+str(mes_d)
    cdr= "cdr_"+str(anio_d)+"_"+str(mes_d)+"_"+str(dia_d)
elif a == "Domingo":
    delta= timedelta(days=6)
    cdr_fecha= fecha_datatime - delta
    mes_d= cdr_fecha.month
    dia_d= cdr_fecha.day
    anio_d= cdr_fecha.year
    if len(str(dia_d))< 2:
        dia_d= "0"+str(dia_d)
    if len(str(mes_d))< 2:
        mes_d= "0"+str(mes_d)
    cdr= "cdr_"+str(anio_d)+"_"+str(mes_d)+"_"+str(dia_d)
##################################################################################################
#
######Consulta DB#############
#select= '"select recv_a_number from "'+cdr+'" where in_entity_id="'+entity+'" and day(from_unixtime(recv_msg_time))="'+day+'" and month(from_unixtime(recv_msg_time))="'+mes+'" and year(from_unixtime(recv_msg_time))="'+str(anio)+'" group by day(from_unixtime(recv_msg_time)), recv_a_number having cant>10 order by cant desc limit "'+limit+'";"'
select= '"select recv_a_number from "'+cdr+'" where in_entity_id="'+entity+'" and day(from_unixtime(recv_msg_time))="'+day+'" and month(from_unixtime(recv_msg_time))="'+mes+'" group by day(from_unixtime(recv_msg_time)),recv_a_number having count(*)>500 order by count(*) desc;"'

#re=os.system('mysql -pentcheck -h permem-emgw-a -P 5029 -u entcheck  mediation_segmented -N -s -e '+select)
resultado = os.popen('mysql -pentcheck -h permem-emgw-a -P 5029 -u entcheck  mediation_segmented -N -s -e '+select)

#####################Guardo Salida de Consulta en Fichero#######################
datos=[]
datos= resultado.readlines()
fichero= open('sospechoso.txt', 'w')
for p in datos:
    fichero.write(str(p))
fichero.close()
###############################

##########Primer Consulta###########################
#select= '"select recv_a_number,day(from_unixtime(recv_msg_time)) dia,count(*) cant from "'+cdr+'" where in_entity_id="'+entity+'" and primary_route_id=1006 and day(from_unixtime(recv_msg_time))="'+day+'" and month(from_unixtime(recv_msg_time))="'+mes+'" and year(from_unixtime(recv_msg_time))="'+str(anio)+'" group by day(from_unixtime(recv_msg_time)), recv_a_number having cant>10 order by cant desc limit "'+limit+'";"'
###################################Obtengo Numero en lista Sospechosos#########################################


#######Variables DB#########
user= "iqgw"
pas= "has9877h"
db= "msggw"
#se extraen prefix que estan agregados como sospechossos, routing_prefix_id(MO_BULK_USERS)
datos=[]
comando = 'mysql -u iqgw -p'+pas+' -D'+db+' -s -e "select prefix from routing_prefix where routing_prefix_list_id=13;"'
resultado = os.popen(comando)
datos= resultado.readlines()
###################Guardo Salida en Archivo###########################
fichero= open('prefix.txt', 'w')

for p in datos:
   fichero.write(str(p))
fichero.close()
