from django.core.management.base import BaseCommand
from seminar2_app2.models import Post, Author


class Command(BaseCommand):
    help = 'Create Post'

    def add_arguments(self, parser):
        parser.add_argument('-t', '--title', required=True)
        parser.add_argument('-c', '--content', nargs='*', required=True)
        parser.add_argument('-C', '--category', required=True)
        parser.add_argument('-a', '--author_id', type=int, required=True)

    def handle(self, *args, **options):
        author = Author.objects.filter(pk=options['author_id']).first()
        Post(title=options['title'], content=' '.join(options['content']),
             category=options['category'], author=author).save()
