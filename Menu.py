import subprocess

def pantalla():
    print('El siguiente programa no tiene captura de errores, si se equivoca en alguna inserción de datos')
    print('se cerrará el menú y tendrá que empezar desde cero')
    print('------')
    print('Pulse el número de la opción a seleccionar')
    print('0 -> Desplegar el proyecto local')
    print('1 -> Desplegar en docker el proyecto local')
    print('2 -> Desplegar en docker el proyecto de master de Decide-Europa-Autenticación')
    #print('3 -> Desplegar el proyecto en heroku')
    print('4 -> Salir')
    metodo = input()
    return metodo

def bash(bashCommand):
	output = subprocess.check_output(['bash','-c', bashCommand])
	return output

def main():
    metodo = pantalla()

    # main
    bandera = False
    if(metodo ==  '0'):
        print('------')

        print('Quitando los contenedores de decide')
        print('------')

        bashCommand = 'sudo docker-compose down'
        bash(bashCommand)

        print('------')

        print('Lanzando la aplicación')
        print('------')

        bashCommand = 'cd decide && python3 manage.py runserver'
        bash(bashCommand)

        print('------')

        bashCommand = 'cd ..'
        bash(bashCommand)


    if (metodo == '1'):
        print('------')

        print('Quitando los contenedores de decide')
        print('------')

        bashCommand = 'sudo docker-compose down'
        bash(bashCommand)
        print('------')

        print('Borrando las imagenes de los contenedores en desuso')
        print('------')

        bashCommand = 'sudo docker system prune -af'
        bash(bashCommand)
        print('------')

        print('Desplegando decide local en el contenedor')
        print('------')

        bashCommand = 'sudo docker-compose up -d'
        bash(bashCommand)
        print('------')

        bashCommand = 'cd ..'
        bash(bashCommand)

    if (metodo == '2'):
        print('------')

        print('Quitando los contenedores de decide')
        print('------')

        bashCommand = 'sudo docker-compose down'
        bash(bashCommand)
        print('------')

        print('Borrando las imagenes de los contenedores en desuso')
        print('------')

        bashCommand = 'sudo docker system prune -af'
        bash(bashCommand)
        print('------')

        print('Desplegando decide local en el contenedor')
        print('------')

        bashCommand = 'cd docker && sudo docker-compose up -d'
        bash(bashCommand)
        print('------')

        bashCommand = 'cd ..'
        bash(bashCommand)

    #if (metodo == '3'):
	#	bashCommand = "sudo apt update"
	#	bash(bashCommand)
		
    if (metodo == '4'):
        bandera = True

    return bandera

if __name__ == '__main__':
    elementos = []
    while True:
        (bandera) = main()
        if(bandera):
            break
