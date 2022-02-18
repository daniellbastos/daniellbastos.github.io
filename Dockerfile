FROM python:3.4.10
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app

RUN : "---------- install generic build container deps ----------" \
    && set -x \
    && apt-get update \
    && apt-get install -y \
        git \
        vim

RUN : "---------- install GEO libs container deps ----------" \
    && apt-get install -y \
        make \
        gcc \
        python3-dev \
        python-dev \
        python3-lxml \
        libxml2-dev \
        libxslt-dev \
        libxslt1-dev \
        build-essential

COPY . /app/
RUN pip install -U pip
RUN pip install -r requirements.txt

EXPOSE 9090

ENTRYPOINT ["sh", "./docker-entrypoint.sh"]
