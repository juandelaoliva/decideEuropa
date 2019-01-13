Decide-Europa-Visualización
============

Grupo 1 
-------
ID de opera: 127
--------

Miembros del grupo (en orden alfabético): 
--------
* [Alarcón Tamayo, Alfonso](http://github.com/alfalatam): 5
* [Barbadillo Serrano, Manuel](http://github.com/Bwer23): 5
* [De la Oliva Aguilar, Juan Manuel](http://github.com/juandelaoliva): 3 
* [Molina Pineda, Elena](http://github.com/elenaMo): 3
* [Trinidad Márquez, Felipe](http://github.com/feltrimar): 3

Enlaces de interés:
--------
* [Repositorio de código](https://github.com/juandelaoliva/decideEuropa)
* [Sistema desplegado]

Resumen
-
Se ha procedido a la actualización del módulo visualizer en el proyecto DecideEuropa. Para la actualización se ha implementado tecnologías como Travis y Heroku, así como librerías como Mathplotlib, numpy y Fusioncharts. Como entorno de desarrollo hemos utilizado de nuevo Django para trabajar sobre el codigo que nos entregaron.
Los problemas a tratar eran una mejora de la muestra de la votación, la cual era en su anterior iteración era una id de la votación junto con el título de la misma. En nuestra nueva iteración hemos añadido tablas y un grafico de tarta así como información de contacto y descripción del mismo proyecto.

Introducción y contexto
-
Se pondrá en contexto el proyecto elegido y los aspectos fundamentales para entender el resto del documento. La introducción es como un resumen ampliado.



Descripción del sistema
-
se explicará el sistema desarrollado desde un punto de vista funcional y arquitectónico. Se hará una descripción tanto funcional como técnica de sus componentes y su relación con el resto de subsistemas. Habrá una sección que enumere explícitamente cuáles son los cambios que se han desarrollado para el proyecto.

Planificación del proyecto
-
se presentará la planificación del trabajo y qué tareas se han hecho. Haciendo hincapié en el reparto de tareas. Es importante que estén explícitas las iteraciones funcionales que se han realizado por parte de los miembro del equipo. Tenga muy en cuenta lo expresado en la sección 2.2.2 del enunciado del proyecto en cuánto a división de tareas. Recuerde que también entregará el diario del grupo por lo que no es necesario que aquí detalle lo que va en ese entregable.

Entorno de desarrollo
-
El equipo de desarrolladores decideEuropa visualizacion ha hecho uso del entorno de desarrollo python, en su version 3.6.0, haciendo uso del framework Django. Para su instalacion, se pone a disposicion del usuario el documento requirements.txt, en el cual se engloban todas las librerias necesarias para el correcto funcionamiento de la aplicacion.
Para instalar el entorno de desarrollo el usuario debe escribir el siguiente comando en consola:
    sudo apt-get install python3.6
Finalizada la instalacion del entorno de desarrollo, se procedera a la instalacion del proyecto asi como el framework DSjango y sus librerias.
 Para descargar el projecto se hara uso de la herramienta git mediante el comando:
    git clone https://github.com/juandelaoliva/decideEuropa.git
Una vez descargado el projecto se procedera a instalar el framework y sus librerias. Para ello navegaremos hasta el directorio del projecto /decideEuropa y ejecutaremos el siguiente comando:
    pip3 install -r requirements.txt
Si durante la instalacion de las librerias ocurriese algun error, se procedera a instalar las librerias individualmente. Para ello abriremos requirements.txt y instalaremos las librerias alli descritas mediante el siguiente comando:
    pip3 install "libreria"
Tras esto tendremos que crearnos nuestra base de datos con postgres:
    sudo su - postgres
    psql -c "create user decide with password 'decide'"
    psql -c "create database decide owner decide"
Procederemos a configurar los datos en local_settings.py para nuestras rutas en local. Unavez configuradas las rutas pertinentes realizaremos la primera migracion para preparar la base de datos, ejecutando el siguiente codigo desde la carpeta decide:
    ./manage.py migrate
Ya podemos ejecutar nuestro projecto en local:
    ./manage.py runserver


Gestión de incidencias
-
se describirá el proceso de gestión de incidencias que ha seguido en el proyecto. También deberá enlazar partes de su proyectos donde se evidencie que ha seguido ese proceso.

La gestión de incidencias debería contener explícitamente dos apartados. Uno de cómo se han gestionado la incidencias internas y otro el cómo se han gestionado y se ofrece protocolo para gestionar las incidencias externas tanto las recibidas como las que se reporten a otros subsistemas.

Cuando una incidencia esté relacionada con un commit, señalar el commit dentro de la propia incidencia y viceversa.

Gestión de depuración
-
se describirá el proceso de gestión de depuración que ha seguido en el proyecto. También deberá enlazar partes de su proyectos donde se evidencie que ha seguido ese proceso.

En este apartado sería ideal que pudiera tener un ejemplo de una incidencia que haya gestionado y que haya dado lugar a un proceso de depuración y cómo, usando el proceso definido, pudo solventarla.

Gestión del código fuente
-
se explicarán los procesos, técnicas y herramientas para la gestión del código del proyecto. Evite poner información de las herramientas en sí que se pueda encontrar en fuentes bibliográficas o internet. Si es del caso haga referencia a ellas. Céntrese en los aspectos particulares de su proyecto en concreto:

* Guía de cómo y cuándo hacer commits: de enlaces concretos a ejemplos que se puedan ver en su repositorio de cómo ha seguido esas guías.
* Usage model del repositorio: ¿cómo se gestiona el repositorio?

Gestión de la construcción e integración continua
-
Se explicarán los procesos, técnicas y herramientas para la gestión de la construcción e integración continua del proyecto. Evite poner información de las herramientas en sí que se pueda encontrar en fuentes bibliográficas o internet. Si es del caso haga referencia a ellas. Céntrese en los aspectos particulares de su proyecto en concreto:

Proceso de integración continua que usa
-
Herramientas que está usando para dar soporte a ese proceso
Gestión de liberaciones, despliegue y entregas
se explicarán los procesos, técnicas y herramientas para la gestión de las liberaciones, despliegue y entregas del proyecto. Evite poner información de las herramientas en sí que se pueda encontrar en fuentes bibliográficas o internet. Si es del caso haga referencia a ellas. Céntrese en los aspectos particulares de su proyecto en concreto:

* Proceso definido para las liberaciones con un apartado explícito de cómo ha elegido la licencia de software para su proyecto
* Proceso definido para el despliegue
* Proceso definido para las entregas
* Política de nombrado e identificación de los entregables

Mapa de herramientas
-
se dará un esquema de cómo se conectan las herramientas que se usan en el proyecto, qué relaciones tienen o qué relaciones propondría añadir. No olvide explicar bien el mapa de herramientas. Se trata del mapa de herramientas de gestión de la configuración. El mapa de herramientas que se usen para el desarrollo (como bases de datos u otros) no es necesario que aparezca aquí.

Ejercicio de propuesta de cambio
-
se presentará un ejercicio con una propuesta concreta de cambio en la que a partir de un cambio que se requiera, se expliquen paso por paso (incluyendo comandos y uso de herramientas) lo que hay que hacer para realizar dicho cambio. Debe ser un ejercicio ilustrativo de todo el proceso de evolución y gestión de la configuración del proyecto.

Conclusiones y trabajo futuro
-
se enunciarán algunas conclusiones y se presentará un apartado sobre las mejoras que se proponen para el futuro (curso siguiente) y que no han sido desarrolladas en el sistema que se entrega
