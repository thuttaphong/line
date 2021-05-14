FROM python:3.6-alpine3.7

RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip

RUN apk add --no-cache --update \
    python3 python3-dev gcc \
    gfortran musl-dev

RUN apk add --no-cache libressl-dev musl-dev libffi-dev

RUN python3.6 -m pip install --upgrade pip

RUN apk --no-cache add git

RUN apk add mariadb-dev

WORKDIR /line

COPY . /line

EXPOSE 8080

ENTRYPOINT ["python3"]
CMD ["inwbot.py"]