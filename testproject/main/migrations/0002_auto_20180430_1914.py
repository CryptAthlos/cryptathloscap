# Generated by Django 2.0.4 on 2018-04-30 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crypto',
            name='rank',
            field=models.CharField(max_length=10),
        ),
    ]