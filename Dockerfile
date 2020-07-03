FROM python:3.7.1

MAINTAINER yugojim <yugojim@gmail.com>

ADD . /server
WORKDIR /server
RUN apt-get update
RUN apt-get install -y --no-install-recommends \
        libatlas-base-dev gfortran nginx supervisor nano

RUN pip3 install uwsgi
RUN pip3 install --no-cache-dir -r requirements.txt

COPY nginx.conf /etc/nginx/sites-enabled/
COPY uwsgi.ini /etc/
COPY supervisord.conf /etc/

CMD ["/usr/bin/supervisord"] 
#	python manage.py migrate &&\
#	python manage.py createsuperuser &&\
#   python manage.py runserver 0:8500 &

# expose port 8000
#EXPOSE 8500