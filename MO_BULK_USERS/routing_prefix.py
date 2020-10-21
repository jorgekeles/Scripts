#!/usr/bin/python

import os
import sys
from subprocess import call
import subprocess
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


