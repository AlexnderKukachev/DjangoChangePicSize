# Generated by Django 3.2.4 on 2021-06-10 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestTask', '0007_pic_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pic',
            name='pic',
            field=models.ImageField(default='', upload_to=''),
        ),
        migrations.AlterField(
            model_name='pic',
            name='url',
            field=models.URLField(default='', max_length=30, verbose_name='URL ссылка на изображение'),
        ),
    ]