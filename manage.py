#!/usr/bin/env python
import os
import sys
import environ

if __name__ == '__main__':
    env = environ.Env(Debug=(bool, False))
    environ.Env.read_env(env_file=os.path.join(os.getcwd(), '.env'))
    DOCKER_ENV = os.environ.get('DOCKER_ENV', None)
    RUN_ENV = DOCKER_ENV if DOCKER_ENV else os.environ.get('RUN_ENV', 'local')
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'configuration.settings.' + RUN_ENV)
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError("Couldn't import Django. Are you sure it's installed and " "available on your PYTHONPATH environment variable? Did you " "forget to activate a virtual environment?") from exc

    # This allows easy placement of apps within the interior core directory.
    # current_path = os.path.dirname(os.path.abspath(__file__))
    # sys.path.append(os.path.join(current_path, 'core'))

    execute_from_command_line(sys.argv)
