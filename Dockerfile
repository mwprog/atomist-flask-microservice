FROM alpine:3.4

RUN apk add --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    rm -r /root/.cache

COPY flask_service /tmp/service/flask_service
COPY requirements.txt /tmp/service/requirements.txt
COPY setup.py /tmpservice/setup.py

WORKDIR /tmp
RUN pip install --no-cache-dir -r requirements.txt && \
    python setup.py install && \
    rm -rf /tmp/service

ENTRYPOINT ["uwsgi", "--http", ":9090", "--mount", "/=wp.runserver:app", "--enable-threads"]