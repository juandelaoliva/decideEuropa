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
* [Sistema desplegado](https://decidevisualizacion.herokuapp.com/doc/)

Resumen
-
Se ha procedido a la actualización del módulo visualizer en el proyecto DecideEuropa. Para la actualización se ha implementado tecnologías como Travis y Heroku, así como librerías como Mathplotlib, numpy y Fusioncharts. Como entorno de desarrollo hemos utilizado de nuevo Django para trabajar sobre el codigo que nos entregaron.
Los problemas a tratar eran una mejora de la muestra de la votación, la cual era en su anterior iteración era una id de la votación junto con el título de la misma. En nuestra nueva iteración hemos añadido tablas y un grafico de tarta así como información de contacto y descripción del mismo proyecto.

Introducción y contexto
-
DecideEuropa es un sistema de votación construido en Python con el FrameWork Django. En este sistema los usuarios pueden crear votaciones, las cuales pueden rellenar ellos mismos con sus votos. Al haber votado todos, se puede iniciar el proceso de votación para mostrar los resultados.

El trabajo que se ha realizado ha sido modificar el módulo visualizer del este mismo proyecto. Éste es el módulo que se encarga de mostrar los resultados de una forma que una persona que no tenga control sobre la base de datos pueda comprenderlos. Para ello se ha mejorado la presentación, ya que la original era muy pobre. 

En el nuevo formato se han añadido una serie de tablas y un grafico de tarta, así como un bot de instagram para mostrar ahí los resultados.

Descripción del sistema
-

El sistema de DecideEuropa se divide en varios subsistemas, entre los que se encuentran el que nuestro grupo está modificando, el de visualización. Éste se encarga unica y exclusivamente de mostrar lo que ha salido a partir de las votaciones que se han iniciado.

El sistema de visualización de DecideEuropa publica en css la información registrada en las votaciones. Para ello necesita la integración del sistema de postprocesado ya que, para que el sistema muestre los votos, han de ser procesados en información visible.
Esto se muestra en el archivo visualizer.html que pide los parametros que hemos introducido.

También se compone de un bot de Telegram que muestra estas mismas respuestas a petición del usuario.
Este sistema está preparado para el despliegue y la integración continua gracias a Heroku y Travis respectivamente.

Los cambios que se han aplicado son los siguientes:
* Se ha implementado el archivo common.css para visualización en dicho lenguaje.
* Se ha añadido un bot de Telegram para mostrar los gráficos creados.
* Se ha modificado el archivo visualizer.html desde cero para acoplarlo a las nuevas vistas.
* Se ha añadido la implementación con Travis y con Heroku, para la integración continua y el despliegue.

Planificación del proyecto
-
se presentará la planificación del trabajo y qué tareas se han hecho. Haciendo hincapié en el reparto de tareas. Es importante que estén explícitas las iteraciones funcionales que se han realizado por parte de los miembro del equipo. Tenga muy en cuenta lo expresado en la sección 2.2.2 del enunciado del proyecto en cuánto a división de tareas. Recuerde que también entregará el diario del grupo por lo que no es necesario que aquí detalle lo que va en ese entregable.


Manolo - Controlador, librería de visualización y compresor, creación de carpetas de css y vista basica. Gestión de errores 404, creación de votaciones

Felipe - Generacion del archivo de documentación.md y implementación del sistema de Travis CI

Alfonso - Implementación del bot de Telegram y unificación con decide. Implementación de Heroku. Coordinación con otros grupos. Llenado de la wiki de github.

Elena - Generación del CSS y parte de la documentación.

Juan - Reunión de coordinación de otros subgrupos. Desarrollo inicial de la documentación del submodulo. Creación y administración del repositorio. Adición del subsistema al proyecto padre. 

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
La gestión de incidencias que hemos utilizado en Decide-Europa-Visualización Ha estado estrechamente relacionado con la utilización de issues con las correspondientes labels, al detectar un posible fallo o error en el correspondiente commit se procederá a comentar en la issue el fallo si lo conoce, además se creará una issue con  una etiqueta  de Bug y de High priority, para facilitar la identificación de los fallos por parte de los demás miembros del grupo.Será responsabilidad del commit que ha generado el error subsanarlo ,no obstante si otro miembro detecta el error y sabe subsanarlo podrá proceder solicitando luego un commit para subir los cambios
Ejemplo realización gestión de la incidencia:

[Gestión de incidencias](https://github.com/juandelaoliva/decideEuropa/wiki/Ejemplo-de-gesti%C3%B3n-de-incidencias)

La gestión de incidencias con otros grupos ha seguido una metodología similar a la de nuestro subgrupo (Visualización)
Si se producen conflictos con los merges se tendrá que abrir una discusión en los comentarios de la issue determinada.
Toda la información detallada de la gestión con los demás subsistemas vendrá explicada en: 

[Documento Gestión Decide Europa](https://github.com/decide-europa/decide-europa/wiki/Documento-Gesti%C3%B3n-Decide-Europa)


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
Para la integración y build se usa principalmente Travis CI, un servicio para la automatización de la misma en contenedores. Este principalmente divide la tarea de integración en jobs que se ejecutan al principio del git clone de un repositorio.

Travis CI sigue una linea de procesos estipulada en el travis.yml que incluye la modificación de local_settings a local_settings.travis.py y cada job se encarga de recorrerlo cada vez que se ejecuta la bajada del repositorio.

También uno puede entrar en la pagina web de Travis CI asociada al proyecto para comprobar si la build en cuestión se ha ejecutado bien o no.

Gestión de liberaciones, despliegue y entregas
-
se explicarán los procesos, técnicas y herramientas para la gestión de las liberaciones, despliegue y entregas del proyecto. Evite poner información de las herramientas en sí que se pueda encontrar en fuentes bibliográficas o internet. Si es del caso haga referencia a ellas. Céntrese en los aspectos particulares de su proyecto en concreto:

* Proceso definido para las liberaciones con un apartado explícito de cómo ha elegido la licencia de software para su proyecto
* Proceso definido para el despliegue
* Proceso definido para las entregas
* Política de nombrado e identificación de los entregables

En cuanto al nombrado de los entregables, se usa la política de nombrado de versiones facilitando primeramente el numero de version, seguido de una barra y el año de la versión.

Finalmente se añadiría el nombre de la versión, en el caso de que la entrega no sea final, la versión tendrá como nombre "beta".

Ejemplo: version 1.1.0 /2019 beta

Mapa de herramientas
-
se dará un esquema de cómo se conectan las herramientas que se usan en el proyecto, qué relaciones tienen o qué relaciones propondría añadir. No olvide explicar bien el mapa de herramientas. Se trata del mapa de herramientas de gestión de la configuración. El mapa de herramientas que se usen para el desarrollo (como bases de datos u otros) no es necesario que aparezca aquí.

Ejercicio de propuesta de cambio
-
Inclusion de css en el subsistema visualizacion

Se comienza mediante la creacion de una issue en git con la tarea asignada, relacionandola a aquellos desarrolladores que esten incluidos en la misma, seleccionando y/o creando aquellos labels que sean necesarios. Se referenciara el proyecto asi como el Milestone asociado.
Se describira brevemente la tarea a realizar , asi como la relacion a otras issues.

Una vez generada la issue pasaremos al desarrollo de la tarea.

Para la implementacion de css en el projecto necesitaremos crear una carpeta static en la carpeta decide/decide/.
En ella generaremos el documento css common, donde incluiremos los estilos a implementar en las vistas.

Una vez generado el documento necesitamos referenciar la carpeta static en settings.py, facilitando asi posteriores referenciaciones a la misma.

Una vez referenciadas procedemos a realizar los cambios en la vista base.html, haciendo participes asi a todas las vistas de la carpeta static/css/ ya que todas las vistas heredan de ella.

Finalmente realizamos los cambios en la vista, referenciando las diferentes clases en los tags.

Terminados y comprobados los cambios en el projecto procedemos a subirlos a la rama de desarrollo del usuario mediante los siguientes comandos:

        git checkout devManuel
        git add decide
        git add visualizacion
        git add base
        git commit -m "Implementacion de css"
        git push origin devManuel
        
 Comprobamos que los cambios se han subido con exito en la rama del desarrollador. Si no hay errores generamos un pull request de la rama master, abriendo con ella una nueva issue pidiendo la revision del codigo por otro desarrolador, esperando su visto bueno para realizar el merge con la rama master. El merge se realiza mediante los siguientes comandos:
 
        git checkout master
        git merge origin devManuel
        
Si existen conflictos se procedera a la solucion de los mismo mediante su entorno de desarrollo (Visual Studio). Una vez solucionados se procede a la subida a master:

        git add decide
        git add visualizacion
        git add base
        git commit -m "Implementacion de css"
        git push
        
 Una vez comprobada la subida con exito se procede a cerrar la issue de subida.
        

Conclusiones y trabajo futuro
-
Para mejorar la entrega sería considerable implementar un sistema de selección de gráficos, de manera que sólo se visualice el gráfico deseado haciendo más cómodo su uso.

Además hacer uso de slack como herramienta de comunicación ya que es un sistema de comunicación en auge.

Finalmente se ha planteado hacer que el bot de visualización de votos funcione de manera aislada y hacer uso de datos reales recibidos por parte de postproducción ya que actualmente los datos usados han sido creados por nosotros, al ser imposible usar los de otros equipos.
