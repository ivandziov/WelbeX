FROM python:3.10.5-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /welbex/

RUN apt-get update && apt-get install libpq-dev gcc -y

ADD requirements.txt /welbex/
RUN pip install -r requirements.txt

ADD . /welbex/

ADD entrypoint.sh /welbex/
ENTRYPOINT ["./entrypoint.sh"]