# Libroteka Backend

Este repositorio contiene el código backend del proyecto **Libroteka**, desarrollado con **Django** y **Django REST Framework**. 

Aquí se gestiona la lógica del servidor, la base de datos, la autenticación y las API REST utilizadas por el frontend y la aplicación móvil.


## ⚙️ Librerías y dependencias

- Python 3.8+
- Django 4.2
- Django REST Framework
- JWT
- Cloudinary
- MySQL 9+


## 🛠 Correr Localmente

### Requisitos:
- Python 3.8+
- Base de datos MySQL vacía

### Pasos:

1. Clonar proyecto localmente
```bash
  git clone https://github.com/ISPC-TSDW/libroteka-backend.git
``` 

2. Levantar una base de datos MySQL vacía

Recomendado usar Docker (docker compose ya incluido en el proyecto)

```sh
docker compose up -d --build
```

3. Ingresar al directorio del proyecto
```sh
  cd libroteka-backend
```

*(Opcional) Crear el entorno virtual* 

```sh
  python -m venv venv
```
*(Opcional) Activar el entorno virtual*
```sh
.\venv\bin\activate #Windows
```
```sh
source venv/bin/activate #Linux
```
4. Instalar dependencias
```bash
  pip install -r requirements.txt
```
5. Crear la base de datos
```bash
  python manage.py migrate
```

6. Configuración archivo .env (se podrá pasar por mensajeria privada)
    - Crear un archivo .env en el directorio del proyecto
    - Copiar el archivo .env.example a .env
    - Completar los siguientes valores:
        - MYSQL_PUBLIC_URL
        - DJANGO_SECRET_KEY
        - CLOUDINARY_CLOUD_NAME
        - CLOUDINARY_API_KEY
        - CLOUDINARY_API_SECRET
7. Levantar el servidor

```bash
  python manage.py runserver
```

---
Hasta acá, el servicio backend tiene un entorno local y se puede acceder a través de la dirección http://127.0.0.1:8000/, la base de datos esta vacía y se recomienda hacer una carga inicial de datos de prueba.

---



## 📊 Cargar datos de prueba

Para cargar datos de prueba, se puede utilizar cuaqluier adminsitrador de base de datos (DBEaver, MySQL Workbench, etc)

1. Conectarse a la base de datos

La url de la db (si se levantó con Docker) es:

```bash
mysql://root:root@localhost:3306/libroteka
```

2. Cargar datos de prueba

Se corre el script "initial_data_test.sql" en la base de datos.


---

## 📝 Licencia
Este proyecto está licenciado bajo licencia **MIT**.