from django.core.management.base import BaseCommand
from seminar2_app2.models import Post


class Command(BaseCommand):
    help = 'Delete post by ID'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int)

    def handle(self, *args, **options):
        post = Post.objects.filter(pk=options['pk']).first()
        if post is not None:
            post.delete()