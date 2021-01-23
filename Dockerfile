FROM python:3.8.5-alpine as baseimage

ENV APP_USER=appuser
ENV UID=1000
ENV GID=1000

#https://stackoverflow.com/questions/36217250/cannot-install-uwsgi-on-alpine
#RUN apk add python3-dev build-base linux-headers pcre-dev
RUN apk update && apk add gcc python3-dev musl-dev libffi-dev
RUN addgroup \
    -g $UID \
    $APP_USER && \
    adduser \
    --disabled-password \
    --gecos "" \
    --shell "/bin/sh" \
    --home "/app" \
    --uid $UID \
    --ingroup $APP_USER \
    $APP_USER
COPY . /app
RUN chown -R $APP_USER:$APP_USER /app

WORKDIR /app
USER $APP_USER

RUN pip install --upgrade pip && pip install --user -r requirements.txt

FROM baseimage
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
USER $APP_USER

CMD ["/app/run-server.sh"]