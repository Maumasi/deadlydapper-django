import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
  '''Command to pause execution until DB is ready'''

  def handle(self, *args, **options):
    self.stdout.write('Waiting on database...')
    db_connection = None

    while not db_connection:
      try:
        db_connection = connections['default']
      except OperationalError:
        self.stdout.write('Database unavailable, waiting one second...')
        time.sleep(1)

    self.stdout.write(self.style.SUCCESS('Database available!'))
