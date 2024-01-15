from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "Initilize sysadmin user"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        if User.objects.all().count() == 0:
            User.objects.create_superuser(username='sysadmin', password='password', email='hiroshifuu@outlook.com', first_name='Hao', last_name='FENG')
            print('sysadmin user created')
        else:
            print('sysadmin user already exists')
