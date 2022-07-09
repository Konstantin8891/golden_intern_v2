# pull official base image
FROM python:3.8-slim
# set work directory
WORKDIR /app/

# docker-compose
COPY memories/ .

# stand-alone
# COPY . .

RUN pip3 install --upgrade pip

RUN pip3 install --upgrade setuptools

RUN apt-get update &&\
    apt-get install -y binutils libproj-dev gdal-bin

RUN pip3 install -r requirements.txt

# Выполнить запуск сервера разработки при старте контейнера.
CMD ["gunicorn", "memories.wsgi:application", "--bind", "0:8000" ] 
