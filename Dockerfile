# docker build -t

FROM python:3.9.16-alpine3.17

RUN apk add --no-cache curl supervisor
RUN #locale-gen ru_RU.UTF-8
ENV LANG ru_RU.UTF-8
ENV LANGUAGE ru_RU:ru
ENV LC_ALL ru_RU.UTF-8
ENV PYTHONUNBUFFERED 1

# copy source
WORKDIR /opt/project
COPY requirements.txt ./


RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

#COPY supervisor/supervisord.conf /etc/supervisor/supervisord.conf
#COPY supervisor/prod.conf /etc/supervisor/conf.d/yatube.conf

EXPOSE 8000

#VOLUME /data/
#VOLUME /conf/
#VOLUME /static/

#RUN addgroup djos && adduser -G djos -s /bin/sh -D djos
#RUN chown -R djos:djos /app
#USER djos

#CMD /usr/bin/supervisord -c /etc/supervisor/supervisord.conf --nodaemon
#CMD python yatube/manage.py runserver 0.0.0.0:8000
#CMD ["sh"]
