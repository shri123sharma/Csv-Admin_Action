from django.core.management.base import BaseCommand,CommandError
from drf_task.models import *

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

class Command(BaseCommand):
    help = 'Create random users'

    def handle(self, *args,**options):
      import pdb;pdb.set_trace()
      patient=Patient.objects.all()
      for i in patient:
       pat_email=f'{i.pat_name}@gmail.com'
       i.pat_email=pat_email
       i.save()
      return pat_email