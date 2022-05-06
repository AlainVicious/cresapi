# Descripcion
Webservice en python con `Flask` implementando seguridad con `JWT`

# instalacion
## crear entorno virtual
se debe instalar el virtualenv para poder crear un entorno virtual

    pip3 install virtualenv

crear entorno virtual

    python -m virtualenv .

ejecutar entorno virtual

    source .\scripts\activate


## instalar paquetes necesarios

instalar las siguientes dependencias

    pip3 install flask python-dotenv pyjwt

# Ejecucion
correr el archivo main

    py main.py

## prueba /api/login
Request:
`POST /api/login`


    {
        "username": "fer.alain@live.com",
        "password": "P4$$w0rd*1"
    }

Response

    {token}

## prueba /api/test
Request:
`POST /api/test`

    Headers
    Authorization: Bearer {token}

    {
        "nombre": "mundo"
    }

Response

    hola mundo!