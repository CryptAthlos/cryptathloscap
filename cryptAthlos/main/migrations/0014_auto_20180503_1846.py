# Generated by Django 2.0.4 on 2018-05-03 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20180503_1845'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='main',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='main',
            name='updated_at',
        ),
    ]
