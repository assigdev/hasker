FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN \
  apt-get -y update && \
  apt-get install -y gettext && \
  apt-get clean
RUN pip install uwsgi

ADD . /opt/hasker
WORKDIR /opt/hasker

RUN pip install pipenv && pipenv install --system --deploy

EXPOSE 8000
ENV PORT 8000

#CMD ["uwsgi", "/opt/hasker/settings/uwsgi.ini"]