from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    biography = models.TextField()
    birthdate = models.DateField()
    full_name = f'{name} {surname}'


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    pub_date = models.DateField(auto_now=True)
    category = models.CharField(max_length=100)
    views = models.IntegerField(default=0)
    pub_flag = models.BooleanField(default=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f'Title: {self.title}; Date: {self.pub_date}'


class Comment(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateField(auto_now=True)
    changed_at = models.DateField(null=True)
