# Generated by Django 3.2.4 on 2021-06-10 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TestTask', '0012_alter_pic_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pic',
            name='url',
        ),
    ]
