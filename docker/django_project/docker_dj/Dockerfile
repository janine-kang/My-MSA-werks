FROM python:3.7.9-stretch

WORKDIR /mydjango


RUN apt-get update
RUN pip install django
RUN pip install mysqlclient
RUN apt-get install -y vim

COPY bookmark /mydjango/bookmark
COPY docker_dj /mydjango/docker_dj
COPY db.sqlite3 /mydjango/db.sqlite3
COPY manage.py /mydjango/manage.py



EXPOSE 8000

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
