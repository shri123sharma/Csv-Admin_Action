from django.core.management.base import BaseCommand
from drf_task.models import Doctor

class Command(BaseCommand):
    help='this command for email in unique '

    def handle(self, *args, **options):
        doctor=Doctor.objects.all()
        for doc in doctor:
          doc_name_email=f'{doc.doc_name}@gmail.com'
          doc.doc_email=doc_name_email
          doc.save()
        return doc_name_email

  
