import os
import os.path as path
import hashlib
import subprocess

print("Configurando requirements.txt ...")
f= open("requirements.txt", 'r')
requirements= f.read()
rewrite= True
if path.exists("checkVersion.txt"):
	with open('checkVersion.txt','r') as content_file:
		requirementsCheck= content_file.readline()
		if requirementsCheck == hashlib.sha256(requirements).hexdigest():
			rewrite= False
if rewrite:
	with open('checkVersion.txt','w') as content_file:
			
		print ("Instalando el requirements....")
		cmd = 'pip3 install -r requirements.txt'
		os.system(cmd)
		content_file.write(str(hashlib.sha256(requirements).hexdigest()))
		


print ("Migrando la BD....")
cmd = 'cd decide && ./manage.py migrate'
returnedValue = subprocess.call(cmd, shell=True) 

if returnedValue != 0:
	print ("Al migrar la BD algo fue mal...")
else:
	print ("Ejecutando los tests ...")
	cmd = 'cd decide && sudo ./manage.py test'
	returnedValue = subprocess.call(cmd, shell=True)  

	if returnedValue != 0:
		print ('Los Test han fallado')

	else:
		print ("Desplegando app....")
		cmd = 'cd decide && ./manage.py runserver'
		os.system(cmd)

