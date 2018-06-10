# Generated by Django 2.0.5 on 2018-06-10 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_auto_20180610_1750'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dialog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('dialog', models.TextField(max_length=20000)),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dialogs', to='books.Chapter')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('text', models.TextField(max_length=20000)),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='texts', to='books.Chapter')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]