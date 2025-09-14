import time

from django.core.management.base import BaseCommand
from django.db import connection
from django.db.utils import OperationalError


class Command(BaseCommand):
    """Wait command for check if database ready to connect."""

    def handle(self, *args, **options):
        print("Waiting for database...", flush=True)
        conn = False
        delay = 5
        while not conn:
            try:
                cursor = connection.cursor()
                if cursor:
                    conn = True
            except OperationalError:
                print(
                    f"Database is not ready. Next try after {delay} seconds",
                    flush=True
                )
                time.sleep(delay)
        print("Database is ready. Starting app...", flush=True)
