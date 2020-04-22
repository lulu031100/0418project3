from django.db import models
from django.utils import timezone
app_name = 'blog'
class Category(models.Model):
    name = models.CharField('カテゴリー名', max_length=200)
    created_at = models.DateTimeField('作成日',default=timezone.now)

    def __str__(self):
        return self.name

class Post(models.Model):

    title = models.CharField('タイトル', max_length=100)
    text = models.TextField('本文')
    created_at = models.DateTimeField('作成日',default=timezone.now)
    category = models.ForeignKey(
        Category, verbose_name = 'カテゴリ', on_delete = models.PROTECT
    )

    def __str__(self):
        return self.title
