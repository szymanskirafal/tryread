# Generated by Django 2.0.5 on 2018-06-10 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_chapter_slug_chapter'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='nr',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
    ]