# Generated by Django 3.2.4 on 2021-06-10 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestTask', '0018_pic_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pic',
            name='pic',
            field=models.BinaryField(null=True),
        ),
    ]
