from django.core.management.base import BaseCommand
from seminar2_app2.models import Comment


class Command(BaseCommand):
    help = 'Get comments by author name'

    def add_arguments(self, parser):
        parser.add_argument('name', help='Author name')
        parser.add_argument('-s', '--sort', action='store_true', default=False, help='Sort by ID')
        parser.add_argument('-c', '--count', type=int, help='Numbers required to output')

    def handle(self, *args, **options):
        comments = Comment.objects.filter(author__name=options['name'])
        if options['sort']:
            comments = sorted(comments, key=lambda x: x.id)
        if options['count'] is not None:
            comments = comments[:options['count']]

        return self.stdout.write(f"{comments}")
