from django.core.management.base import BaseCommand
from seminar2_app2.models import Post


class Command(BaseCommand):
    help = 'Get posts by author name'

    def add_arguments(self, parser):
        parser.add_argument('name')
        parser.add_argument('-s', '--sort', action='store_true', default=False, help='Sort by ID')
        parser.add_argument('-c', '--count', type=int, help='Numbers required post to output')

    def handle(self, *args, **options):
        posts = Post.objects.filter(author__name=options['name'])
        if options['sort']:
            posts = sorted(posts, key=lambda x: x.id)
        if options['count'] is not None:
            posts = posts[:options['count']]

        return self.stdout.write(f"{posts}")
