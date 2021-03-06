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


Manuel - Controlador, librería de visualización y compresor, creación de carpetas de css y vista basica. Gestión de errores 404, creación de votaciones

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
La gestión de la depuración de código se llevará a cabo junto a las correspondientes issues y labels para facilitar la identificación, si se encontrase un error y no se supiese subsanar, primero se procedería a comentar en la propia issue el error por si algún miembro puede ayudarle, después de esto:

o se solicita ayuda a otros miembros ya que no eres capaz y otro equipo se encarga del proceso de arreglo

o bien se detecta el error y se procede a eliminar este del ultimo commit para arreglar el fallo, mediante su correspondiente creación de la issue y su validación para el commit,cuando se elimina o cambia código por errores en la issue del commit se debe comprobar por otro miembro que bien el error esta subsanado y que el resto del proyecto funciona correctamente como en las peticiones del commit,una vez validado se procede a la subida

Un ejemplo de la depuración de código puede verse en el siguiente enlace:

[Ejemplo de depuración de código](https://drive.google.com/drive/folders/1f352Y3U_zUzATCNZ_h9PrJf5DQOxsfli)


Gestión del código fuente
-
El código fuente se ha gestionado mediante la herramienta [GitHub](https://github.com) de la siguiente manera:

1. Cada componente del grupo se creará una rama de desarrollo hija de la rama master. Ej: devJohn
2. Una vez decidido el cambio a implementar se creará una issue mencionando la mejora o cambio que se va a desarrollar para que el resto del grupo lo pueda ver y no haya solapamiento de trabajos. Dicha issue deberá llevar la/s correspondiente/s etiquetas según la [guía de etiquetas](https://github.com/juandelaoliva/decideEuropa/wiki/Guia-de-uso-de-las-etiquetas) acordadas previamente y reflejadas en la [wiki](https://github.com/juandelaoliva/decideEuropa/wiki) del proyecto. Ejemplo: [Creación de Bot informativo en la plataforma de mensajería telegram](https://github.com/juandelaoliva/decideEuropa/issues/10)
3. En caso de tener algún problema a la hora de implemntear los cambios en nuestra rama de desarrollo podemos comentarlo en la anterior issue (paso 2) o se creará una nueva issue (si el problema es de mayor magnitud) relacionada con la issue anteriormente mencionada la cual indica la tarea que estamos realizando. En la issue del problema se comentará y se pueden asignar a compañeros a los que les solicitamos ayuda. Deberán llevar las correspondientes etiquetas según el documento de la wiki.
4. Una vez finalizada la tarea o cambio propuesto en nuestra rama se hará un merge de la rama master a nuestra rama para no machacar posibles cambios que se hayan subido anteriormente y se creará una issue de aviso y petición de comprobación. Irá con sus respectivas etiquetas y tendrá que estar relacionada con la issue principal de la tarea (paso 2). En el título y la descripción debe quedar claro dónde se puede encontrar la implementación para que uno de los compañeros compruebe que no da ningún error. Se dará el visto bueno mediante un comentario. Ejemplo[Petición de subida Bot de telegram](https://github.com/juandelaoliva/decideEuropa/issues/35)
5. Ya habiendo recibido la confirmación de algún componente del grupo de que nuestro cambio o mejora no da ningun error cerraremos la issue de petición (paso 4) y se hacce un commit a la rama master.
6.Se cerrará la issue que indicaba la tarea a realizar (paso 2).


Gestión de la construcción e integración continua
-
Para la integración y build se usa principalmente Travis CI, un servicio para la automatización de la misma en contenedores. Este principalmente divide la tarea de integración en jobs que se ejecutan al principio del git clone de un repositorio.

Travis CI sigue una linea de procesos estipulada en el travis.yml que incluye la modificación de local_settings a local_settings.travis.py y cada job se encarga de recorrerlo cada vez que se ejecuta la bajada del repositorio.

También uno puede entrar en la pagina web de Travis CI asociada al proyecto para comprobar si la build en cuestión se ha ejecutado bien o no.

Gestión de liberaciones, despliegue y entregas
-
El software utilizado ha sido en algunos casos gratuito y open-source y en el resto de casos con la licencia que nos ha otorgado la Universidad de Sevilla para trabajar con ello.

El despliegue se realiza mediante heroku, usando la cuenta proporcionada por el coordinador del grupo, a traves de la rama master.
Las entregas se realizara colocando la URL en el formulario estipulado en la Wiki de EGC

En cuanto al nombrado de los entregables, se usa una política de nombrado de versiones compuesto el numero de version, indicado el primer numero las version, seguido de los cambios realizados segun su tamaño, seguido de una barra y el año de la versión.
Finalmente se añadiría el nombre de la versión, en el caso de que la entrega no sea final, la versión tendrá como nombre "beta".

Ejemplo: version 1.1.0 /2019 beta

Mapa de herramientas
-
1. La máquina virtual que carga Ubuntu utiliza la tecnología de git.
2. Cuando se utiliza clone en GitHub, el script de Travis se ejecuta.
3. El repositorio se despliega en Heroku.
4. Docker almacena en un contenedor todo lo anterior (incluyendo Heroku para su posterior despliegue) y lo ejecuta cuando sea necesario, utilizando django como framework y postgresql y base de datos.

![Optional Text](../master/MapadeHerramientas02.jpg)
Figura 1:Mapa Herramientas



Ejercicio de propuesta de cambio
-
Inclusion de css en el subsistema visualizacion

Se comienza mediante la creacion de una issue en git con la tarea asignada, relacionandola a aquellos desarrolladores que esten incluidos en la misma, seleccionando y/o creando aquellos labels que sean necesarios como se ve en la figura 2. Se referenciara el proyecto asi como el Milestone asociado.
Se describira brevemente la tarea a realizar , asi como la relacion a otras issues.

![Optional Text](../master/Issue.png)
Figura 2:Issue inicio tarea

Una vez generada la issue pasaremos al desarrollo de la tarea.

Para la implementacion de css en el projecto necesitaremos crear una carpeta static en la carpeta decide/decide/.
En ella generaremos el documento css common, donde incluiremos los estilos a implementar en las vistas como se aprecia en la figura 3.

![Optional Text](../master/rama-trabajo.png)
Figura 3:Ejemplo rama proyecto

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
        
 Comprobamos que los cambios se han subido con exito en la rama del desarrollador. Si no hay errores generamos un pull request de la rama master, abriendo con ella una nueva issue pidiendo la revision del codigo por otro desarrolador como se aprecia en la figura 4.

![Optional Text](../master/IssuePush.png)
Figura 4:Issue commit

Esperando su visto bueno para realizar el merge con la rama master. El merge se realiza mediante los siguientes comandos:
 
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
