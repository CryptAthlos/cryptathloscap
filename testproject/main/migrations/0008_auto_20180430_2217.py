# Generated by Django 2.0.4 on 2018-04-30 22:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20180430_2113'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='crypto',
            unique_together={('name', 'symbol')},
        ),
    ]
