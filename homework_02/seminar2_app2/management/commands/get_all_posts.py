from django.core.management.base import BaseCommand
from seminar2_app2.models import Post


class Command(BaseCommand):
    help = 'Get all posts'

    def handle(self, *args, **options):
        return self.stdout.write(f'{Post.objects.all()}')
