# Generated by Django 2.0.5 on 2018-06-13 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_auto_20180611_2122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dialog',
            name='chapter',
        ),
        migrations.DeleteModel(
            name='Dialog',
        ),
    ]
