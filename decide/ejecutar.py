import os
import os.path as path
import hashlib
import subprocess
import sys

#Evitamos un fallo en la consola
S=1
s=1
n=0
N= 0
#----
print("Configurando requirements.txt ...")
f= open("../requirements.txt", 'r')
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
		cmd = 'sudo pip3 install -r ../requirements.txt'
		os.system(cmd)
		content_file.write(str(hashlib.sha256(requirements).hexdigest()))
		


print ("Migrando la BD....")
cmd = './manage.py migrate'
returnedValue = subprocess.call(cmd, shell=True) 

if returnedValue != 0:
	print ("Al migrar la BD algo fue mal...")
else:
	if len(sys.argv)>=2:
		ask= sys.argv[1]
		
	else:
		ask= input("Desea ejecutar los tests? S/n")

	if int(ask):
		print ("Ejecutando los tests ...")
		cmd = './manage.py test'
		returnedValue = subprocess.call(cmd, shell=True)  

		if returnedValue != 0:
			print ('Los Test han fallado')

		else:
			print ("Desplegando app....")
			cmd = './manage.py runserver'
			os.system(cmd)
	else:
		print ("Desplegando app....")
		cmd = './manage.py runserver'
		if not (len(sys.argv)==3 and sys.argv[2]=="test"):
			os.system(cmd)


