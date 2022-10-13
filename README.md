# FastAPI Template

### Useful and multifunction FastApi template

![FastApi](https://img.shields.io/badge/FastApi-black?style=flat&logo=fastapi)
[![CodeFactor](https://www.codefactor.io/repository/github/rodion-gudz/telegram-bot-template/badge?s=5c628f092285245c2cbab683d2509317bcca48c9)](https://www.codefactor.io/repository/github/rodion-gudz/telegram-bot-template)
![CodeStyle](https://img.shields.io/badge/code%20style-black-black)
![PythonVersions](https://img.shields.io/pypi/pyversions/FastApi)

## Features

* ![aiogram 3](https://img.shields.io/badge/0.85.0-aiogram-blue) as a main library
* ![pyrogram](https://img.shields.io/badge/0.19.2-tortoise--orm-orange) as a database library
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

* 🚀 Run bot via `python -m app`

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
$ tree app
app
├── __main__.py  # Startup script. Starts uvicorn.
├── api # Package with all handlers.
│   └── __init__.py
├── db # module contains db models
│   └── __init__.py
├── settings.py # Main configuration settings for project.
├── static  # Static content.
│   └── docs
│       ├── redoc.standalone.js
│       ├── swagger-ui-bundle.js
│       └── swagger-ui.css
└── web # Package contains web server. Events, Middlewares, startup config.
    ├── __init__.py
    ├── application.py  # FastAPI application configuration.
    ├── events  # Package contains events.
    │   ├── __init__.py
    │   ├── shutdown.py
    │   └── startup.py
    └── middlewares # Package contains middlewares.
        ├── __init__.py
        └── main.py
```


## Pre-commit

To install pre-commit simply run inside the shell:

```bash
pre-commit install
```

pre-commit is very useful to check your code before publishing it.
It's configured using .pre-commit-config.yaml file.

By default it runs:

* black (formats your code);
* flake8 (spots possibe bugs);

You can read more about pre-commit here: https://pre-commit.com/
