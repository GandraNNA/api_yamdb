# Generated by Django 2.2.16 on 2022-07-21 22:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20220722_0221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='title',
            name='description',
        ),
    ]