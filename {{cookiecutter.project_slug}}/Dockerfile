# ===== BUILD IMAGE =====

# Setup system environment.
FROM alpine:latest AS build
ENV LANG="en_US.utf-8" DJANGO_SETTINGS="production" DJANGO_KEY="change_me" DJANGO_DOMAIN="{{cookiecutter.project_domain_name}}" DJANGO_DATABASE="/app/db/database.sqlite3" DJANGO_WEBROOT="/app/web/" DJANGO_TIMEZONE="{{cookiecutter.production_timezone}}"

# Update system and install dependencies.
RUN apk update && apk upgrade
RUN apk add --no-cache python3
RUN pip3 --no-cache-dir install pipenv

# Create app directories.
RUN mkdir -p /app/src/
RUN mkdir -p /app/db/
RUN mkdir -p /app/web/static/
RUN mkdir -p /app/web/media/

# Setup app environment.
WORKDIR /app/src/
COPY Pipfile ./
COPY Pipfile.lock ./
COPY manage.py ./
COPY wsgi.py ./
COPY settings/ settings/
COPY apps/ apps/
COPY templates/ templates/
COPY static/ static/
RUN pipenv sync

# Prepare website.
RUN pipenv run python3 manage.py makemigrations
RUN pipenv run python3 manage.py migrate
RUN pipenv run python3 manage.py populatedb

# ===== FINAL IMAGE =====

# Reset system environment.
FROM alpine:latest
ENV LANG="en_US.utf-8" DJANGO_SETTINGS="production" DJANGO_KEY="change_me" DJANGO_DOMAIN="{{cookiecutter.project_domain_name}}" DJANGO_DATABASE="/app/db/database.sqlite3" DJANGO_WEBROOT="/app/web/" DJANGO_TIMEZONE="{{cookiecutter.production_timezone}}"

# Update system and install dependencies.
RUN apk update && apk upgrade
RUN apk add --no-cache python3
RUN pip3 --no-cache-dir install pipenv

# Restore built application.
COPY --from=build /app/ /app/
COPY --from=build /root/.local/share/virtualenvs/ /root/.local/share/virtualenvs/

# Expose interfaces.
VOLUME /app/db/
VOLUME /app/web/static/
VOLUME /app/web/media/
EXPOSE 80

# Collect static resources, update database, and start website.
WORKDIR /app/src/
CMD rm -rf /app/web/static/* \
	&& pipenv run python3 manage.py collectstatic --ignore=*.scss \
	&& pipenv run python3 manage.py migrate \
	&& pipenv run python3 manage.py serve 0.0.0.0 80
