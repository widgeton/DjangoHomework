from django.core.management.base import BaseCommand
from seminar2_app2.models import Author


class Command(BaseCommand):
    help = 'Create Author'

    def add_arguments(self, parser):
        parser.add_argument('-n', '--name')
        parser.add_argument('-s', '--surname')
        parser.add_argument('-e', '--email')
        parser.add_argument('-b', '--biography', nargs='*')
        parser.add_argument('-d', '--birthdate')

    def handle(self, *args, **options):
        Author(name=options['name'], surname=options['surname'], email=options['email'],
               biography=' '.join(options['biography']), birthdate=options['birthdate']).save()
