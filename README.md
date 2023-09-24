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
- [Docker](https://www.docker.com/).
- [Docker Compose](https://docs.docker.com/compose/install/).
- [Poetry](https://python-poetry.org/) para la gestión de paquetes y entornos de Python.
- `ruff` + `black` para el formateo y linting de Python.

### Frontend

- Node.js (con [pnpm](https://pnpm.io/es/installation)).

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>

## Desarrollo Local

Las rutas estandar para el desarrollo local son:

- Frontend, construido con Docker: http://localhost:3000
- Backend, fast api: http://localhost:8000/
- Documentación interactiva con Swagger UI: http://localhost:8000/docs
- PGAdmin, administración web de PostgreSQL: http://localhost:5050 (Opcional)

### Con Docker

Inicia el stack con Docker Compose:

```bash
docker compose up -d
```

**Nota**: La primera vez que inicies tu stack, podría tardar un minuto. Puedes revisar los logs con `docker-compose logs` o para un servicio específico `docker-compose logs backend`. Y puedes acceder a la consola de un servicio con `docker-compose exec backend bash`.

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
