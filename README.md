# Tecnicatura Superior en Desarrollo web y Aplicaciones Digitales

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
