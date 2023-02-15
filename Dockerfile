# syntax=docker/dockerfile:1

FROM python:3.10.8

WORKDIR /app

RUN apt-get -y update

RUN apt-get -y install git gcc python3-dev

RUN ffmpeg-python
RUN apt-get install -y ffmpeg python3-pip curl

COPY requirements.txt requirements.txt

RUN pip3 install -U -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "ZeroTwo"]
