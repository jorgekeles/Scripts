#!/usr/bin/python
from io import open
import os

fichero = open('/etc/hosts','r')
hosts = fichero.read().split('\n')
fichero.close()


listado = open('roas','r')
roas = listado.read().split()
listado.close()


for roa in roas:
	if roa in hosts:
	fichero1 = open('lista_final','a')
	fichero.write(roa+'\n')
fichero.close()