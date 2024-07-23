<h1 align="center"> Modul.os </h1>

<p align="center">
  <a href="#Descripción">Descripción</a> •
  <a href="#Requisitos">Requisitos</a> •
  <a href="#Desarrollo-local">Desarrollo Local</a> •
  <a href="#Contribuir">Contribuir</a> •
  <a href="#Contacto">Contacto</a> •
  <a href="#Créditos">Créditos</a> •
  <a href="#Licencia">Licencia</a>
</p>

---

## Descripción

[Por definir]

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>

## Requisitos

### Backend

- [Python](https://www.python.org/downloads/) >= 3.10 (idealmente 3.11)
- [Poetry](https://python-poetry.org/) para la gestión de paquetes y entornos de Python.
- `ruff` + `black` para el formateo y linting de Python.

### Frontend

- Node.js (con [pnpm](https://pnpm.io/es/installation)).

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>

## Desarrollo Local

### Con Docker (Altamente recomendado)

Para comenzar el desarrollo con un contenedor docker debes seguir las siguientes instrucciones:

1. Descargar docker desktop en este [link](https://www.docker.com/products/docker-desktop/).

2. Al tener docker instalado correctamente debes correr el siguiente comando para 

```shell
docker-compose up --build
```
3. Ante cualquier error en la configuracion o cambios en el archivo docker-compose.yml ejecutar:

```shell
docker-compose down
```
Este comando eliminara el contenedor para que puedas hacer cambios a este archivo (docker-compose.yml). Luego de un cambio, vuelve a ejecutar el comando del inciso 2.

Las rutas estándar para el desarrollo local son:

- Frontend: http://localhost:3000
- Backend: http://localhost:8000
- Documentación: http://localhost:8000/docs

### Con Poetry

1. Instala las dependencias:

```shell
poetry install
```

2. Inicia una sesión shell con el nuevo entorno:

```shell
poetry shell
```

3. Ejecuta la API:

```shell
poetry run uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

La API estará disponible en [localhost:8000](http://localhost:8000) y la documentación en [localhost:8000/docs](http://localhost:8000/docs).

#### Agregar dependencias

Para agregar nuevas dependencias, utiliza:

```shell
poetry add <nombre-del-paquete>
```

Y para actualizar las dependencias existentes:

```shell
poetry update
```

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>

## Contribuir

### Reporte de Bugs y Feature Requests

Utiliza la sección de **issues** para reportar problemas o proponer nuevas características.

### Flujo de Trabajo

1. Realiza un Pull Request (PR) a la rama `development`.
2. Revise el _preview_ y verifica que todos los checks hayan pasado.
3. Asigna revisores al PR.
4. Una vez aprobado, realiza el merge a `development`.

📖 Consulta [contributing.md](contributing.md) para más detalles.

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>

## Contacto

Para consultas o comunicaciones, contáctanos a través de [osuc.dev](https://links.osuc.dev/).

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>

## Créditos

### Mantenedores

<!-- - [USERNAME](https://www.github.com/USERNAME) -->

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>

## Licencia

[Por definir]

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>
