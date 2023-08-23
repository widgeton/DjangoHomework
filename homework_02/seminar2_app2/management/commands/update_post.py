from django.core.management.base import BaseCommand
from seminar2_app2.models import Post, Author


class Command(BaseCommand):
    help = 'Update Post'

    def add_arguments(self, parser):
        parser.add_argument('id', type=int)
        parser.add_argument('-t', '--title')
        parser.add_argument('-c', '--content', nargs='*')
        parser.add_argument('-d', '--pub_date')
        parser.add_argument('-C', '--category')
        parser.add_argument('-a', '--author_id', type=int)

    def handle(self, *args, **options):
        post = Post.objects.filter(pk=options['id']).first()
        if post is not None:
            if options['title'] is not None:
                post.title = options['title']
            if options['content'] is not None:
                post.content = ' '.join(options['content'])
            if options['pub_date'] is not None:
                post.pub_date = options['pub_date']
            if options['category'] is not None:
                post.category = options['category']
            if options['author_id'] is not None:
                author = Author.objects.filter(pk=options['category']).first()
                if author is not None:
                    post.author = author
            post.save()

