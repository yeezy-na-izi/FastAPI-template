FROM python:3.9.6-slim-buster

RUN pip install --no-cache-dir poetry==1.2.1

# Copying requirements of a project
COPY pyproject.toml poetry.lock /app/src/
WORKDIR /app/src

# Installing requirements
RUN poetry install

# Copying actuall application
COPY . /app/src/
RUN poetry install

CMD ["/usr/local/bin/python", "-m", "app"]

# Uncommit this line if you want to use expose port
#EXPOSE 80
