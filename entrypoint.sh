#!/usr/bin/env bash

echo "entrypoint.sh"

if [[ "$1" ]]; then
    python3 /app/manage.py makemigrations
    python3 /app/manage.py migrate
    python3 /app/manage.py collectstatic --noinput
    python3 /app/manage.py init_sysadmin
	eval "$@"
fi
