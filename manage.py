#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import socket
from django.core.management.commands.runserver import Command as runserver

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'paleteria.settings')
    runserver.default_port = "8080"
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    host = s.getsockname()[0]
    s.close()
    runserver.default_addr = host

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
