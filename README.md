# FastAPI Template

### Useful and multifunction FastApi template

![FastApi](https://img.shields.io/badge/FastApi-black?style=flat&logo=fastapi)
[![CodeFactor](https://www.codefactor.io/repository/github/yeezy-na-izi/fastapi-template/badge)](https://www.codefactor.io/repository/github/yeezy-na-izi/fastapi-template)
![CodeStyle](https://img.shields.io/badge/code%20style-black-black)
![PythonVersions](https://img.shields.io/pypi/pyversions/FastApi)

## Features

* ![aiogram 3](https://img.shields.io/badge/0.85.0-aiogram-blue) as a main library
* ![pyrogram](https://img.shields.io/badge/0.19.2-tortoise--orm-orange) as a database library
* ![poetry](https://img.shields.io/badge/1.2.1-poetry-yellow) as a dependency manager
* 🎨 OpenAPI docs on `api/docs` and `api/redoc`
* 🛠 Docker support with `docker-compose`

## Usage

### Create project

* 📌 [Create](https://github.com/yeezy-na-izi/FastAPI-template/generate) and clone repo from this template
* 🔑 Rename `example.toml` to `config.toml` and change api settings

### Install dependencies

* 🐍 Install poetry with command `pip install poetry`
* 📎 Install dependencies with command `poetry install`

### Run project

* 🚀 Run project via `python -m app`

## Docker

You can start the project with docker using this command:

```bash
docker-compose -f deploy/docker-compose.yml --project-directory . up --build
```

But you have to rebuild image every time you modify `poetry.lock` or `pyproject.toml`
with this command:

```bash
docker-compose -f deploy/docker-compose.yml --project-directory . build
```

## Project structure

```bash
$ tree "app"
app
├── __init__.py
├── __main__.py  # Startup script. Starts uvicorn.
├── application.py  # FastAPI application configuration.
├── settings.py  # Main configuration settings for project.
├── api  # Package with all handlers.
│   ├── __init__.py
│   └── router.py  # Main router.
├── db  # module contains db models
│   └── __init__.py
├── events
│   ├── __init__.py
│   ├── shutdown.py  # Shutdown event.
│   └── startup.py  # Startup event.
├── middlewares  # Package contains middlewares.
│   ├── __init__.py
│   └── main.py  # Main middleware.
└── static  # Static content.
    └── docs
        ├── redoc.standalone.js
        ├── swagger-ui-bundle.js
        └── swagger-ui.css

```

## Pre-commit checker

To install pre-commit simply run inside the shell:

```bash
pre-commit install
```

pre-commit is very useful to check your code before publishing it.
It's configured using .pre-commit-config.yaml file.

By default, it runs:

* black (formats your code);
* flake8 (spots possible bugs);

You can read more about pre-commit here: https://pre-commit.com/
