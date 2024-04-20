Paso 1:
Descargar o clonar el proyecto.

Paso2:
Renombar el archivo .env.sample a .env o crear archivo .env

Paso 3:
Crear un entorno virtual => $ python -m venv nombre_entorno

Paso 4:
Activar el entorno virtual 
En windows => $ source nombre_entorno/Scripts/activate 
En linux => $ source nombre_entorno/bin/activate

Paso 5:
Instalar las dependencia: $ pip install -r requirements.txt

Paso 6:
Realizar el archivo de migraciones => $ python manage.py makemigrations

Paso 7:
Aplicar las migraciones a la base de datos actual => python manage.py migrate

Paso 8:
Por último lanzar el servidor => python manage.py runserver
