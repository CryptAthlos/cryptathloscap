# Generated by Django 2.0.4 on 2018-05-03 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20180503_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]