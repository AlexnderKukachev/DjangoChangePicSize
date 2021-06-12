from django.db import models


class Pic(models.Model):
    pic = models.CharField('Путь до изображения', max_length=50, null=True)
    url = models.URLField('URL ссылка на изображение', max_length=300, null=True)
    name = models.CharField('Название изображения', max_length=50, null=True)
    width = models.IntegerField(null=True)
    height = models.IntegerField(null=True)

    def __str__(self):
        return self.name
