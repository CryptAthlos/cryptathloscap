# Generated by Django 2.0.4 on 2018-05-04 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_auto_20180504_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main',
            name='created_at',
            field=models.DateTimeField(editable=False),
        ),
        migrations.AlterField(
            model_name='main',
            name='updated_at',
            field=models.DateTimeField(),
        ),
    ]
