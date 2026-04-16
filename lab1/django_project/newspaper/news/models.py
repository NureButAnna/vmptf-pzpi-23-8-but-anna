from django.db import models


class Article(models.Model):
    title = models.CharField('Назва', max_length=250)
    text = models.TextField('Текст статті')
    date = models.DateTimeField('Дата публікації')
    author = models.TextField('Автор статті', default="Admin")

    def __str__(self):
        return self.title
