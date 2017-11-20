#!/usr/bin/python


import os
usu = raw_input("Usuario: ")
pas = raw_input("Password: ")
bas = raw_input("Base de Datos: ")

os.system('mysql --user=' + usu + ' --password=' + pas + ' --database=' + bas)
