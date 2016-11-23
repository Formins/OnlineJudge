from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models

from account.models import User
# Create your models here.


class Category(models.Model):
    name = models.CharField('cate_name', max_length=50)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class ArticleManager(models.Manager):
    def query_by_time(self):
        query = self.get_queryset().order_by('-pub_date')
        return query


class Article(models.Model):
    objects = ArticleManager()
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, blank=True, null=True)
    author = models.ForeignKey(User, null=True)
    # user = models.ManyToManyField(User, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True, editable=True)
    content = models.TextField(blank=True, null=True)
    poll_num = models.IntegerField(default=0)
    comment_num = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, null=True)
    article = models.ForeignKey(Article, null=True)
    content = models.TextField(blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    poll_num = models.IntegerField(default=0)

    class Meta:
        ordering = ['pub_date']

    def __str__(self):
        return "%s's Comment" % self.user.username


class Poll(models.Model):
    user = models.ForeignKey(User, null=True)
    article = models.ForeignKey(Article, null=True)
    comment = models.ForeignKey(Comment, null=True)
