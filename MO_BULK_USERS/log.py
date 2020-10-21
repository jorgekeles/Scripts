#!/usr/bin/python

import commands
import os


l= open('/home/jorge/Documentos/scripts/MO_BULK_USERS/resultados', 'r')
lista= l.readlines()
contenido= l.read()


if os.stat('resultados').st_size== 0:
    print("vacio")
#print(len(contenido))
#print(type(contenido))
#    fichero= open('/var/log/spamers.log','a')
#for p in lista:
##fecha= datetime.datetime.now().strftime('%Y%m%d-%H:%M:%s')
#    fichero.write(fecha+" Se inserta prefix "+p)
#    fichero.close()
#    l.close()

