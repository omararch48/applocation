Este proyecto usa una autenticación por medio de la función authenticate de django en cada petición, tiene malas practicas sobre el manejo de autenticación pero fue hecha asi para poder facilitar el uso el algun cliente rest o por medio de comandos

# Instalación

La api fue desarrollada con la version 3.10 de python, se necesita crear un amiente virtual para instalar las dependencias, lo pasos son los siguientes

* Crear un ambiente virtual (python -m venv env)
* Activar el ambiente virtual (source env/bin/activate)
* Instalar las dependencias (pip install -r requerimets.txt)
* Crear una archivo secret.json con el mismo contenido del archivo example_secret.json (cp example_secret.json secret.json) y modificar las credenciales en caso de usar algun motor de bases de datos que no sea sqlite, en dicho caso se debe modificar el archivo location/settings/local.py comentando el bloque de mysql y modificando el otro bloque para bases de datos, como por ejemplo para postrges
* Ejecutar las migraciones
* python manage.py makemigrations
* python manage.py migrate
* Crear un superusuario (python manage.py createsuperuser)
* Ejecutar el servidor de desarrollo (python manage.py runserver)

La api tiene un bug, ya que al crear nuevos usuarios desde el panel de administrador, la contraseña se guarda en texto plano, para cambiar contraseñas para nuevos usuarios debe ejecutarse manualmente 
* python manage.py shell
* from apps.users.model import User
* usuario = User.objects.get(id=usuario_id)
* usuario.set_password('nueva contraseña')
* usuario.save()

También es posible probar la api desplegada desde el enalce https://apilocation.omardanielesquivel.com y consultar la documentación minima en https://apilocation.omardanielesquivel.com/redocs, https://apilocation.omardanielesquivel.com/docs, algunos ejemplos de como ejecutar peticiones con el comando curl se encuentran en el archivo request.sh