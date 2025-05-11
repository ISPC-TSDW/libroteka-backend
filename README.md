# Tecnicatura Superior en Desarrollo web y Aplicaciones Digitales

## Repositorio Backend (Django)

Este repositorio contiene el código backend del proyecto **Libroteka**, desarrollado con **Django** y **Django REST Framework**. Aquí se gestiona la lógica del servidor, la base de datos, la autenticación y las API REST utilizadas por el frontend y la aplicación móvil.


## ⚙️ Tecnologías

- Python 3.8+
- Django 4.2
- Django REST Framework
- MySQL
- JWT (SimpleJWT)


## 🔐 Autenticación
Se implementó autenticación con JWT usando SimpleJWT. Los endpoints incluyen:

/api/token/ → login y generación de token

/api/token/refresh/ → renovación del token


## 🧪 Endpoints principales
/api/productos/ → CRUD de libros

/api/carrito/ → gestión de carrito

/api/users/ → registro y login de usuarios

/api/mercadopago/ → simulación de pagos (sandbox)


## Correr Localmente

<table>
<tr>
<th> BackEnd </th>
<td>
Clone the project

```bash
  git clone https://github.com/ISPC-TSDW/libroteka-backend.git
``` 

Go to the project directory

```bash
  cd Backend/Libroteka
```

Activate Virtual environment & install Libraries

```bash
.\backendLibroteka-env\bin\activate # Windows users
source backendLibroteka-env/bin/activate # Linux users

```
```bash
 cd Libroteka/Backend/Libroteka
```
```bash
  pip install -r requirements.txt
```

Start the server

```bash
  python manage.py runserver
```
</td>
</tr>
</table>

<table>
<tr>
<th> Docker <br> (Optional) </th>
<td>
Clone the project

```bash
  git clone https://github.com/ISPC-TSDW/libroteka-frontend.git
``` 

Go to the project directory

```bash
  cd Frontend
```

Install dependencies

```bash
  npm install
```

Go back and Start the Docker Compose

```bash
  cd ..
```
```bash
  sudo docker compose up --build
```
</td>
</tr>
</table>
<table>
