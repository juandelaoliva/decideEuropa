% prepara el repositorio para su despliegue. 
release: sh -c 'cd decide && pip3 install -r requirements.txt && python3 manage.py migrate'

% especifica el comando para lanzar Decide
web: sh -c 'cd decide && gunicorn decide.wsgi --log-file -'
