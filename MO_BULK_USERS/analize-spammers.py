#!/usr/bin/python

import commands
import os
import datetime

#fecha= datetime.datetime.now().strftime('%Y%m%d-%H:%M:%S')
commands.getoutput('/usr/bin/python spam.py')
commands.getoutput('/usr/bin/perl Compara.pl')
lista=[]
l= open('resultados', 'r')
lista= l.readlines()
#######Variables DB#########
user= "iqgw"
pas= "has9877h"
db= "msggw"
############################
contenido= l.read
if contenido != '':
	fichero= open('/var/log/spamers.log', 'a')
	for p in lista:
		fecha= datetime.datetime.now().strftime('%Y%m%d-%H:%M:%S')
		fichero.write(fecha+" Se inserta prefix "+p)
fichero.close()
l.close()
##################################Insert Base##################################
#Funciona OK

for l in lista:
	insert= '"insert into routing_prefix (routing_prefix_list_id,prefix) values(13,"'+(l[:-1])+'"); "'
	comando= 'mysql -uiqgw -p'+pas+' -D'+db+' -s -e '+insert
	os.popen(comando)
#os.remove('resultados')
